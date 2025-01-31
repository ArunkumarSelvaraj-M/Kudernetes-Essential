# Kubernetes Deployment, Pod, and Service Guide

This document explains how to deploy and manage Kubernetes Deployments, Pods, and Services in the `v-cluster` namespace.

## Overview
This setup includes:
1. A **Deployment** (`depl`) running an Ubuntu-based container.
   - Uses environment variables from a ConfigMap.
   - Includes resource limits and probes for health monitoring.
   - Mounts a volume using `hostPath`.
   - Includes an `initContainer` that runs before the main container starts.
2. A **Service** (`depl-svc`) that exposes the Deployment via a `NodePort`.
3. Explanation of Kubernetes **Pods, Deployments, and Services**.

## Kubernetes Concepts

### **What is a Pod?**
A **Pod** is the smallest deployable unit in Kubernetes. It represents a single instance of a running process.

- A Pod contains one or more containers.
- Containers in the same Pod share networking and storage.
- Pods are ephemeral; when deleted, they cannot be restored.

### **What is a Deployment?**
A **Deployment** is a higher-level abstraction that manages the lifecycle of Pods.

- Ensures the desired number of Pod replicas are running.
- Supports rolling updates and rollback.
- Allows scaling Pods up or down.

### **What is a Service?**
A **Service** exposes a set of Pods as a network service.

- Ensures communication between different components.
- Provides stable network access to Pods using labels.
- `NodePort` type allows external access to a service via a node’s IP and port.

## Deployment YAML

### Deployment Definition
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: depl
  namespace: v-cluster
  labels:
    app: depl
spec:
  selector:
    matchLabels:
      app: depl
  replicas: 1
  strategy:
    rollingUpdate:
      maxSurge: 25%
      maxUnavailable: 25%
    type: RollingUpdate
  template:
    metadata:
      labels:
        app: depl
    spec:
      initContainers:
      - name: init-container
        image: ubuntu:latest
        command: ["/bin/bash", "-c", "echo Initializing Deployment; sleep 10"]
      containers:
      - name: depl-con
        image: ubuntu:latest
        command: ["/bin/bash", "-c", "while true; do echo $ROLE; sleep 5 ; done"]
        resources:
          requests:
            cpu: 100m
            memory: 100Mi
          limits:
            cpu: 200m
            memory: 200Mi
        livenessProbe:
          tcpSocket:
            port: 80
          initialDelaySeconds: 5
          timeoutSeconds: 5
          successThreshold: 1 
          failureThreshold: 3
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /_status/healthz
            port: 80
          initialDelaySeconds: 5
          timeoutSeconds: 2
          successThreshold: 1
          failureThreshold: 3
          periodSeconds: 10
        env:
        - name: ROLE
          valueFrom:
            configMapKeyRef:
              name: cm
              key: env
        ports:
        - containerPort: 80
          name: depl-port
        volumeMounts:
        - name: nginx-pv-storage
          mountPath: /usr/share/nginx/html
      volumes:
      - name: nginx-pv-storage
        hostPath:
          path: /usr/share/zoneinfo/Asia/Shanghai
  restartPolicy: Always
```

## Service YAML
```yaml
apiVersion: v1
kind: Service
metadata:
  name: depl-svc
  namespace: v-cluster
spec:
  selector:
    app: depl
  type: NodePort
  ports: 
  - port: 99
    targetPort: 80
    nodePort: 30099
```

## Kubernetes Commands Explained

1. **Apply the Deployment:**
```sh
   kubectl apply -f deployment.yaml
```
2. **Get all deployments:**
```sh
   kubectl get deployments -n v-cluster
```
3. **Describe the deployment:**
```sh
   kubectl describe deployment depl -n v-cluster
```
4. **Scale the deployment (change replicas count):**
```sh
   kubectl scale deployment depl --replicas=3 -n v-cluster
```
5. **Delete the deployment:**
```sh
   kubectl delete deployment depl -n v-cluster
```

### **Pod Commands**
1. **Get all pods in the namespace:**
```sh
   kubectl get pods -n v-cluster
```
2. **View pod logs:**
```sh
   kubectl logs -f deployment/depl -n v-cluster
```
3. **Describe a specific pod:**
```sh
   kubectl describe pod <pod-name> -n v-cluster
```
4. **Delete a pod:**
```sh
   kubectl delete pod <pod-name> -n v-cluster
```

### **Service Commands**
1. **Apply the Service:**
```sh
   kubectl apply -f service.yaml
```
2. **Get all services in the namespace:**
```sh
   kubectl get svc -n v-cluster
```
3. **Describe the service:**
```sh
   kubectl describe svc depl-svc -n v-cluster
```
4. **Access the service externally:**
```sh
   curl http://<NODE_IP>:30099
```
   Replace `<NODE_IP>` with the IP of any worker node.

### **Delete the Entire Namespace (Removes all resources inside it)**
```sh
kubectl delete namespace v-cluster
```

---

This guide provides a detailed explanation of Kubernetes Deployments, Pods, and Services along with relevant commands to deploy, manage, and troubleshoot them. 🚀


# Kubernetes Service Guide

This document explains how to configure and manage **Kubernetes Services**. A **Service** is an abstraction that defines a logical set of pods and a policy to access them. Services enable communication between different parts of an application.

## **Service YAML Definition**

### **LoadBalancer Service Example**
```yaml
apiVersion: v1
kind: Service
metadata:
  name: myapp-svc
  namespace: v-cluster
spec:
  selector:
    app: myapp
  type: LoadBalancer
  ports:
  - port: 90
    targetPort: 80
```

## **Service Types**
Kubernetes provides different types of Services:

1. **ClusterIP (Default):** Exposes the service internally within the cluster.
2. **NodePort:** Exposes the service on a static port on each node.
3. **LoadBalancer:** Provisions an external load balancer (Cloud environments only).
4. **ExternalName:** Maps the service to an external DNS name.

## **Commands for Managing Services**

### **Create a Service from a YAML File**
```sh
kubectl apply -f svc.yaml
```

### **Create a Service from CLI (Without YAML)**
```sh
kubectl expose deployment myapp --type=LoadBalancer --name=myapp-svc --port=90 --target-port=80 -n v-cluster
```

### **Get the List of Services**
```sh
kubectl get services -n v-cluster
```

### **Describe a Service**
```sh
kubectl describe service myapp-svc -n v-cluster
```

### **Check Service Endpoints**
```sh
kubectl get endpoints myapp-svc -n v-cluster
```

### **Delete a Service**
```sh
kubectl delete service myapp-svc -n v-cluster
```
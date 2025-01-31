# Kubernetes DaemonSet Guide

This document explains how to configure and manage **DaemonSet** in Kubernetes. A **DaemonSet** ensures that a copy of a pod runs on every node in the cluster or a specific subset of nodes. It is useful for running system services like log collectors, monitoring agents, or security scanners on all nodes.

## **DaemonSet YAML Definition**

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: fluentd
  namespace: logging
  labels:
    app: fluentd-logging
spec:
  selector:
    matchLabels:
      name: fluentd
  template:
    metadata:
      labels:
        name: fluentd
    spec:
      containers:
      - name: fluentd-elasticsearch
        image: quay.io/fluentd_elasticsearch/fluentd:v2.5.2
        resources:
          limits:
            memory: 200Mi
          requests:
            cpu: 100m
            memory: 200Mi
        volumeMounts:
        - name: varlog
          mountPath: /var/log
      terminationGracePeriodSeconds: 30
      volumes:
      - name: varlog
        hostPath:
          path: /var/log
```

## **Commands for Managing DaemonSet**

### **Apply the DaemonSet**
```sh
kubectl apply -f daemonset.yaml
```

### **Get the List of DaemonSets**
```sh
kubectl get daemonset -n logging
```

### **Describe the DaemonSet**
```sh
kubectl describe daemonset fluentd -n logging
```

### **Delete the DaemonSet**
```sh
kubectl delete daemonset fluentd -n logging
```

### **Delete the Namespace (Removes All Resources Inside It)**
```sh
kubectl delete namespace logging
```

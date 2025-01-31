# Kubernetes ResourceQuota Guide

This document explains how to configure and manage a **ResourceQuota** in Kubernetes for controlling resource allocation in a namespace.

## Overview
A **ResourceQuota** sets hard limits on the amount of compute resources (CPU & Memory) that can be requested or used in a namespace. This ensures fair resource distribution among different applications.

### **Why Use ResourceQuota?**
- Prevents a single application from consuming all resources.
- Ensures fair resource distribution.
- Helps with efficient cluster management.

## **ResourceQuota YAML Definition**

The following YAML file defines a **ResourceQuota** named `mem-cpu-quota` in the `v-cluster` namespace.

```yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: mem-cpu-quota
  namespace: v-cluster
spec:
  hard:
    requests.cpu: "500m"
    requests.memory: "1Gi"
    limits.cpu: "2"
    limits.memory: "2Gi"
```

### Explanation:
- `requests.cpu: "500m"` → Maximum of **0.5 CPU cores** can be requested.
- `requests.memory: "1Gi"` → Maximum of **1GiB** memory can be requested.
- `limits.cpu: "2"` → Total **CPU limit** for all pods in the namespace is **2 cores**.
- `limits.memory: "2Gi"` → Total **Memory limit** for all pods in the namespace is **2GiB**.

## **Commands for Managing ResourceQuota**

### **Create the ResourceQuota**
```sh
kubectl apply -f resourceQuota.yaml
```

### **List ResourceQuotas in a Namespace**
```sh
kubectl get resourcequota -n v-cluster
```

### **Describe a Specific ResourceQuota**
```sh
kubectl describe resourcequota mem-cpu-quota -n v-cluster
```

### **Check Resource Usage Against Quota**
```sh
kubectl get resourcequota mem-cpu-quota -n v-cluster --output=yaml
```

### **Delete the ResourceQuota**
```sh
kubectl delete resourcequota mem-cpu-quota -n v-cluster
```

### **Delete the Entire Namespace (Removes All Resources Inside It)**
```sh
kubectl delete namespace v-cluster
```

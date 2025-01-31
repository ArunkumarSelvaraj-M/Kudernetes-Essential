# Kubernetes Persistent Volume (PV) and Persistent Volume Claim (PVC) Guide

This document explains how to configure and manage **Kubernetes Persistent Volumes (PVs) and Persistent Volume Claims (PVCs)**. A **Persistent Volume (PV)** is a storage resource in Kubernetes that exists independently of any individual pod, while a **Persistent Volume Claim (PVC)** is a request for storage by a user.

## **Persistent Volume YAML Definition**

### **Persistent Volume (PV) Example**
```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: nginx-pv
spec:
  capacity:
    storage: 1Gi
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  storageClassName: local-host
  hostPath:
    path: /app/akilan
```

### **Persistent Volume Claim (PVC) Example**
```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: nginx-pvc
  namespace: v-cluster
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
  storageClassName: local-host
  volumeName: nginx-pv
```

## **Commands for Managing PVs and PVCs**

### **Create PV and PVC from a YAML File**
```sh
kubectl apply -f pv.yaml
kubectl apply -f pvc.yaml
```

### **Get the List of Persistent Volumes**
```sh
kubectl get pv
```

### **Get the List of Persistent Volume Claims**
```sh
kubectl get pvc -n v-cluster
```

### **Describe a Persistent Volume**
```sh
kubectl describe pv nginx-pv
```

### **Describe a Persistent Volume Claim**
```sh
kubectl describe pvc nginx-pvc -n v-cluster
```

### **Delete a Persistent Volume and PVC**
```sh
kubectl delete pv nginx-pv
kubectl delete pvc nginx-pvc -n v-cluster
```
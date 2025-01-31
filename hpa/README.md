# Kubernetes Horizontal Pod Autoscaler (HPA) Guide

This document explains how to configure and manage a **HorizontalPodAutoscaler (HPA)** in Kubernetes. HPA automatically scales the number of pod replicas in a **Deployment** based on CPU utilization or other metrics.

## **HorizontalPodAutoscaler YAML Definition**

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: utility-api
spec:
  minReplicas: 1
  maxReplicas: 5
  metrics:
    - resource:
        name: cpu
        target:
          averageUtilization: 70
          type: Utilization
      type: Resource
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: utility-api
```

## **Commands for Managing Horizontal Pod Autoscaler**

### **Apply the HPA**
```sh
kubectl apply -f hpa.yaml
```

### **Get the List of HPAs**
```sh
kubectl get hpa
```

### **Describe the HPA**
```sh
kubectl describe hpa utility-api
```

### **Check the Scaling Events**
```sh
kubectl get events --sort-by=.metadata.creationTimestamp
```

### **Delete the HPA**
```sh
kubectl delete hpa utility-api
```

### **Check Metrics Server Status (Required for HPA to Work)**
```sh
kubectl get deployment -n kube-system | grep metrics-server
```

### **Manually Increase Load for Testing**
```sh
kubectl run -it --rm load-generator --image=busybox -- sh -c "while true; do wget -q -O- http://utility-api-service; done"
```

---

This guide provides a complete explanation of **HorizontalPodAutoscaler (HPA)**, its purpose, configuration, and management commands in Kubernetes. 🚀


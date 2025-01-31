# Kubernetes Vertical Pod Autoscaler (VPA) Guide

This document explains how to configure and manage a **VerticalPodAutoscaler (VPA)** in Kubernetes. VPA automatically adjusts the CPU and memory resource requests and limits for containers in a **Deployment** based on their usage.

## **VerticalPodAutoscaler YAML Definition**

```yaml
apiVersion: autoscaling.k8s.io/v1
kind: VerticalPodAutoscaler
metadata:
  name: utility-api
spec:
  targetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: utility-api
  updatePolicy:
    updateMode: "Off"
```

## Commands for Managing Vertical Pod Autoscaler

### Apply the VPA

```sh
    kubectl apply -f vpa.yaml
    Get the List of VPA
```
### Get the List of VPA

```sh
    kubectl get vpa
```
Describe the VPA

```bash
    kubectl describe vpa utility-api
```

### Check Metrics Server Status (Required for VPA to Work)

```sh
    kubectl get deployment -n kube-system | grep metrics-server
```

### Delete the VPA

```sh
    kubectl delete vpa utility-api
```

### View VPA Recommendations

```sh
    kubectl get vpa utility-api -o yaml
```


# Kubernetes Job Guide

This document explains how to configure and manage **Kubernetes Jobs**. A **Job** creates one or more pods to run a task to completion. Jobs are useful for batch processing, data transformation, and running periodic workloads.

## **Job YAML Definition**

### **Simple Job Example**
```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: example-job
spec:
  template:
    metadata:
      name: example-pod
    spec:
      containers:
      - name: example-container
        image: busybox
        command: ["echo", "Hello from the job pod"]
      restartPolicy: Never
  backoffLimit: 4
```

### **Data Processing Job Example**
```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: data-processing-job
spec:
  template:
    spec:
      containers:
      - name: data-processing-container
        image: arunakilan/process_data:01
      restartPolicy: OnFailure
  backoffLimit: 2
```

## **Commands for Managing Jobs**

### **Apply the Jobs**
```sh
kubectl apply -f job.yaml
```

### **Get the List of Jobs**
```sh
kubectl get jobs
```

### **Describe a Job**
```sh
kubectl describe job example-job
```
```sh
kubectl describe job data-processing-job
```

### **Check Job Logs**
```sh
kubectl logs -l job-name=example-job
```
```sh
kubectl logs -l job-name=data-processing-job
```

### **Delete a Job**
```sh
kubectl delete job example-job
```
```sh
kubectl delete job data-processing-job
```

### **Restart a Job (After Deletion)**
```sh
kubectl delete job example-job --cascade=foreground
kubectl apply -f job.yaml
```

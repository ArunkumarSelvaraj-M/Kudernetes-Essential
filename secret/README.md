# Kubernetes Secret Guide

This document explains how to configure and manage **Kubernetes Secrets**. A **Secret** is an object that stores sensitive data such as passwords, OAuth tokens, and SSH keys. Secrets are base64-encoded and can be referenced by pods securely.

## **Secret YAML Definition**

### **Opaque Secret Example**
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: mysecret
  namespace: v-cluster
type: Opaque
data:
  dep: RGV2T3BzCg==  # Base64 encoded value of "DevOps"
```

## **Secret Types**
Kubernetes supports different types of Secrets:

1. **Opaque** (Default): Stores arbitrary key-value pairs (e.g., API keys, credentials).
2. **kubernetes.io/service-account-token**: Stores service account tokens.
3. **kubernetes.io/dockerconfigjson**: Stores Docker registry credentials.
4. **kubernetes.io/tls**: Stores TLS certificates.
5. **bootstrap.kubernetes.io/token**: Used for cluster bootstrapping.

## **Commands for Managing Secrets**

### **Create a Secret from a YAML File**
```sh
kubectl apply -f secret.yaml
```

### **Create a Secret from CLI (Without YAML)**
```sh
kubectl create secret generic mysecret --from-literal=dep=DevOps -n v-cluster
```

### **Get the List of Secrets**
```sh
kubectl get secrets -n v-cluster
```

### **Describe a Secret**
```sh
kubectl describe secret mysecret -n v-cluster
```

### **Decode Secret Value**
```sh
kubectl get secret mysecret -n v-cluster -o jsonpath="{.data.dep}" | base64 --decode
```

### **Delete a Secret**
```sh
kubectl delete secret mysecret -n v-cluster
```

# Kubernetes ConfigMap Guide

A **ConfigMap** is used to store configuration data as key-value pairs, which can be used by pods to manage their configurations dynamically.

### **ConfigMap YAML Definition**

The following YAML file defines a **ConfigMap** named `cm` in the `v-cluster` namespace.

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: cm
  namespace: v-cluster
data:
  env: dev
```

### Explanation:
- `data` → Holds key-value pairs.
- `env: dev` → Defines an environment variable named `env` with the value `dev`.

## **Commands for Managing ConfigMap**

### **Create the ConfigMap**
```sh
kubectl apply -f configmap.yaml
```

### **List ConfigMaps in a Namespace**
```sh
kubectl get configmap -n v-cluster
```

### **Describe a Specific ConfigMap**
```sh
kubectl describe configmap cm -n v-cluster
```

### **Get ConfigMap Data**
```sh
kubectl get configmap cm -n v-cluster -o yaml
```

### **Delete the ConfigMap**
```sh
kubectl delete configmap cm -n v-cluster
```

### **Delete the Entire Namespace (Removes All Resources Inside It)**
```sh
kubectl delete namespace v-cluster
```

---


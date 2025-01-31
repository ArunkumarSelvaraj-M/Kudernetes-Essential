# Kubernetes Objects Repository

This repository contains detailed explanations, example configurations, and best practices for various Kubernetes objects. Each object has a dedicated folder containing:

- Example YAML configurations
- A separate `README.md` with explanations and usage details

## Kubernetes Objects Covered

| Object           | Description |
|-----------------|-------------|
| **Pod**         | The basic deployable unit in Kubernetes. |
| **ConfigMap**   | Stores configuration data separately from application code. |
| **DaemonSet**   | Ensures that a pod runs on all (or some) nodes in a cluster. |
| **Deployment**  | Manages stateless applications with rolling updates and rollback capabilities. |
| **HPA (Horizontal Pod Autoscaler)** | Scales pods based on CPU or custom metrics. |
| **VPA (Vertical Pod Autoscaler)** | Adjusts resource requests and limits for pods dynamically. |
| **Job**         | Runs batch processes to completion. |
| **Namespace**   | Provides logical separation within a Kubernetes cluster. |
| **ResourceQuota** | Limits resource consumption within a namespace. |
| **Secrets**     | Securely stores sensitive data like passwords and API keys. |
| **Service**     | Exposes a set of pods as a network service. |
| **Volume**      | Manages persistent and ephemeral storage for pods. |
| **StatefulSet** | Manages stateful applications like databases. |
| **Ingress**     | Manages external access to services. 
| **NetworkPolicy** | Controls network access between pods. 
| **PersistentVolume (PV)** | Manages storage at the cluster level. 
| **PersistentVolumeClaim (PVC)** | Requests storage from a PV. 
| **StorageClass** | Defines storage types for dynamic provisioning. 
| **ClusterRole & ClusterRoleBinding** | Cluster-wide RBAC permissions. 
| **Role & RoleBinding** | Namespace-specific RBAC permissions. 
| **CronJob** | Schedules recurring jobs. |

## How to Use

1. Navigate to the relevant directory for the Kubernetes object.
2. Read the `README.md` file for an explanation.
3. Use the `<FILENAME>.yaml` file as a reference for your deployments.
4. Apply configurations using:
```sh
   kubectl apply -f <FILENAME>.yaml
```

## Contributing
If you'd like to contribute, feel free to submit a pull request or open an issue.
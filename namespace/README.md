# Kubernetes Namespace Guide

This document explains Kubernetes namespaces and provides commands to manage them.

## What is a Namespace?

A Kubernetes namespace is a logical partition that allows you to group and isolate resources within a cluster. Namespaces are useful in multi-team environments where different teams need their own isolated resources.

## Creating a Namespace

To create a namespace, use the following YAML definition:

### YAML Definition:
```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: v-cluster
```

Apply the namespace using:
```sh
kubectl apply -f namespace.yaml
```

Alternatively, create a namespace using the command:
```sh
kubectl create namespace v-cluster
```

## Listing Namespaces

To view all available namespaces in the cluster:
```sh
kubectl get namespaces
```

## Viewing Namespace Details

To describe a namespace and view detailed information:
```sh
kubectl describe namespace v-cluster
```

## Using a Specific Namespace

To run commands within a specific namespace, use the `-n` flag:
```sh
kubectl get pods -n v-cluster
```

To set a default namespace for `kubectl` commands in the current context:
```sh
kubectl config set-context --current --namespace=v-cluster
```

## Deleting a Namespace

To delete a namespace and all its resources:
```sh
kubectl delete namespace v-cluster
```

## Troubleshooting

If a namespace deletion is stuck in `Terminating` state, you can force delete it:
```sh
kubectl get namespace v-cluster -o json | jq '.spec.finalizers=[]' | kubectl replace --raw "/api/v1/namespaces/v-cluster/finalize" -f -
```

---

This guide provides essential namespace management commands to help you efficiently work with Kubernetes namespaces. 🚀


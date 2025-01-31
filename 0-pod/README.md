# Kubernetes Pod Examples

These examples cover multi-container pods, simple single-container pods, and namespace-specific pods.

## Table of Contents

- [Multi-Container Pod](#Multi-Container-Pod)

- [Simple Nginx Pod](#Simple-Nginx-Pod)

- [Web Server Pod in a Namespace](#Web-Server-Pod-in-a-Namespace)

- [How to Apply These Pods](#How-to-Apply-These-Pods)

- [Verifying Pods](#Verifying-Pods)

- [Deleting Pods](#Deleting-Pods)

## Multi-Container Pod

This pod runs two containers:

- server-1: Runs an Nginx web server on port 80.

- server-2: Runs a Ubuntu container that prints "Cloud Garage" every 5 seconds.

```yaml
    apiVersion: v1
    kind: Pod
    metadata:
    namespace: v-cluster
    name: multi-con-pod
    labels:
        app: multi-server
        environment: production
    spec:
    containers:
    - name: server-1
        image: nginx:1.14.2
        ports:
        - containerPort: 80
    - name: server-2
        image: ubuntu
        command: ["/bin/bash", "-c", "while true; do echo 'Cloud Garage'; sleep 5; done"]
```

## Simple Nginx Pod

A basic pod running an Nginx web server.

### YAML Definition:

```yaml
    apiVersion: v1
    kind: Pod
    metadata:
    namespace: v-cluster
    name: nginx-pod
    labels:
        run: nginx-pod
    spec:
    containers:
    - name: nginx
        image: nginx:1.14.2
        ports:
        - containerPort: 80
    dnsPolicy: ClusterFirst
    restartPolicy: Always
```

## Web Server Pod in a Namespace

This pod runs an Nginx web server inside the v-cluster namespace.

### YAML Defination

```yaml
    apiVersion: v1
    kind: Pod
    metadata:
    name: web-server-pod
    namespace: v-cluster
    labels:
        app: web-server
        environment: production
    spec:
    containers:
    - name: web-server
        image: nginx:1.14.2
        ports:
        - containerPort: 80
```

## How to Apply These Pods

Create the v-cluster namespace (for the third pod):

```bash
    kubectl create namespace v-cluster
```

### Apply the YAML files:

```bash
    kubectl apply -f multi-con-pod.yaml
    kubectl apply -f nginx-pod.yaml
    kubectl apply -f web-server-pod.yaml
```

## Verifying Pods

Check if the pods are running:

```bash
    kubectl get pods -A  # To check all namespaces
    kubectl get pods -n v-cluster  # To check in 'v-cluster' namespace
```

## View pod logs:

```bash
    kubectl logs multi-con-pod -c server-2  # Check logs of 'server-2'
    kubectl logs nginx-pod  # Check logs of the nginx pod
```

## Deleting Pods

To delete all pods:

```bash
    kubectl delete pod multi-con-pod
    kubectl delete pod nginx-pod
    kubectl delete pod web-server-pod -n v-cluster
```
# Helm Chart for Python-mongo-flask example

## Requirements
* k8s cluster(minikube)
* Helm
* MongoDB(already been deployed to k8s or accessable to k8s cluster)

### Usage:

```
$ helm init
$ helm install -n python-example --set env.DB_URL=MONGODB_URL . --namespace namespace_name
```
```
$ kubectl get pods -n namespace_name
$ kubect get svc -n namespace_name
```

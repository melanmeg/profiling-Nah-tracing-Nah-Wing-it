# scylladb

## Install ScyllaDB Manager Agent
```bash
#!/bin/bash
set -x

sudo mkdir -p /etc/apt/keyrings
sudo gpg --homedir /tmp --no-default-keyring --keyring /etc/apt/keyrings/scylladb.gpg --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys A43E06657BAC99E3

sudo wget -O /etc/apt/sources.list.d/scylla-manager.list https://downloads.scylladb.com/deb/ubuntu/scylladb-manager-3.3.list

sudo apt-get update
sudo apt-get install scylla-manager-server scylla-manager-client

sudo wget -O /etc/apt/sources.list.d/scylla-manager.list https://downloads.scylladb.com/deb/ubuntu/scylladb-manager-3.3.list

sudo apt-get update
sudo apt-get install scylla-manager-agent
```

## Install Scylladb

- ※失敗

### k apply の場合

```bash
git clone --branch v1.14.0 https://github.com/scylladb/scylla-operator.git
cd scylla-operator

k apply -f examples/common/cert-manager.yaml
k apply -f deploy/operator.yaml

scyllamgr_auth_token_gen
k create namespace scylla
# k create secret -n scylla generic scylla-agent-config --from-literal=token=pT8kU3tJP5DdKPhBQu61llVJQUbaxxyvxlHTPEUrz5v6K9VPiJvjYFHkKYGj7qcYr8TOyGQWKh5syz8p9kH7UtRlEXHHniYV1cpB7WNIlPubPXYPyDU8czMZl2G4LwqK
k create secret -n scylla generic scylla-agent-config --from-file scylla-manager-agent.yaml
# kubectl -n scylla get secret scylla-agent-config -o yaml
# k delete secret -n scylla generic scylla-agent-config

k apply -f examples/generic/cluster.yaml
k -n scylla get ScyllaCluster
k -n scylla get pods

cd ~/scylla-operator
k delete -f examples/generic/cluster.yaml
k create namespace scylla
cd ..
k create secret -n scylla generic scylla-agent-config --from-file t.yaml
cd ~/scylla-operator
k apply -f examples/generic/cluster.yaml
k9s
```


### Helm の場合

- 検証中

- nfs

```bash
# vim values.yaml
replicaCount: 1
nfs:
  server: 192.168.11.12
  path: /mnt/nfsshare/k8s/share
  reclaimPolicy: Retain
storageClass:
  name: nfs-share
  defaultClass: true
  allowVolumeExpansion: true
  accessModes: ReadWriteOnce
  volumeBindingMode: WaitForFirstConsumer
accessModes: ReadWriteMany
```

```bash
helm repo add nfs-subdir-external-provisioner https://kubernetes-sigs.github.io/nfs-subdir-external-provisioner
helm install nfs nfs-subdir-external-provisioner/nfs-subdir-external-provisioner --create-namespace -n kube-system --version 4.0.18 -f values.yaml
```

- 手順
```bash
scyllamgr_auth_token_gen
vim scylla-manager-agent.yaml
k create namespace scylla && \
k create secret -n scylla generic scylla-agent-config --from-file scylla-manager-agent.yaml

k create configmap scylla-config -n scylla --from-file scylla-config.yaml

git clone --branch v1.14.0 https://github.com/scylladb/scylla-operator.git
cd scylla-operator

helm repo add scylla https://scylla-operator-charts.storage.googleapis.com/stable && helm repo update
kubectl apply -f examples/common/cert-manager.yaml

# vim scylla-operator-values.yaml
helm install scylla-operator scylla/scylla-operator --create-namespace -n scylla-operator --version 1.14.0 -f scylla-operator-values.yaml
# vim scylla-manager-values.yaml
helm install scylla-manager scylla/scylla-manager --create-namespace -n scylla-manager --version 1.14.0 -f scylla-manager-values.yaml
# vim scylla-values.yaml
helm install scylla scylla/scylla --create-namespace -n scylla --version 1.14.0 -f scylla-values.yaml
```

# Opensearch

## コマンド

```bash
helm repo add opensearch-operator https://opensearch-project.github.io/opensearch-k8s-operator/
helm install opensearch-operator opensearch-operator/opensearch-operator --version 2.6.1 -n opensearch --create-namespace
k apply -f opensearch-v2-cluster.yaml

```

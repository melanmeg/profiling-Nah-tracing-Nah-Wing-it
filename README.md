# profiling-Nah-tracing-Nah-Wing-it

```bash
# ref: https://github.com/melanmeg/k8s_1-31_on_nobel
# ./composeは検証用

# ref: https://kubernetes.io/docs/tasks/debug/debug-cluster/resource-metrics-pipeline/
# リソース メトリック パイプライン
```

```bash
タスク
・otel, istio
```

- マイグレーションコマンド
```bash
kubeadm config migrate --old-config /tmp/init_kubeadm.yaml --new-config new_init_kubeadm.yaml
kubeadm config migrate --old-config /tmp/join_kubeadm_cp.yaml --new-config new_join_kubeadm_cp.yaml
kubeadm config migrate --old-config /tmp/join_kubeadm_wk.yaml --new-config new_join_kubeadm_wk.yaml
```

- Memo1(v1.30)
- ref: https://v1-30.docs.kubernetes.io/docs/setup/production-environment/tools/kubeadm/high-availability/#steps-for-the-rest-of-the-control-plane-nodes-1
- ref: https://v1-30.docs.kubernetes.io/docs/setup/production-environment/tools/kubeadm/high-availability/#manual-certs
- ref: https://www.server-world.info/query?os=Ubuntu_24.04&p=kubernetes&f=8
```bash
$ kubeadm init phase upload-certs --upload-certs
1e6ddeb7e0f1899e2272f69c13c8fa4bc3d4c9cd4f8f33837f210ae2ac889587

$ kubeadm token create --print-join-command
kubeadm join 192.168.11.110:6443 --token ey544l.7gvqjml99v08t5k9 --discovery-token-ca-cert-hash sha256:cfd36a88a78d469cf521998a4891a0317a75889f2e73c338ddbcba9dcee47754

```

`kubectl auth can-i list configmaps --as system:kube-scheduler`
`kubectl auth can-i list nodes --as=kubernetes-admin -A`

```bash
# istio


### ref: https://istio.io/latest/docs/ambient/install/helm/
helm repo add istio https://istio-release.storage.googleapis.com/charts
helm repo update

helm install istio-base istio/base \
  --version 1.23.1 \
  -n istio-system \
  --create-namespace

kubectl get crd gateways.gateway.networking.k8s.io &> /dev/null || \
  { kubectl apply -f https://github.com/kubernetes-sigs/gateway-api/releases/download/v1.1.0/standard-install.yaml; }

helm install istiod istio/istiod \
  --version 1.23.1 \
  -n istio-system \
  --create-namespace \
  --set profile=ambient

helm install istio-cni istio/cni \
  --version 1.23.1 \
  -n istio-system \
  --set profile=ambient

helm install ztunnel istio/ztunnel \
  --version 1.23.1 \
  -n istio-system

helm install istio-ingress istio/gateway \
  --version 1.23.1 \
  -n istio-ingress \
  --create-namespace

# $ helm ls -n istio-system
# $ helm status istio-base -n istio-system
# $ helm get all istio-base -n istio-system


### ref: https://istio.io/latest/docs/ambient/getting-started/deploy-sample-app/
kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.23/samples/bookinfo/platform/kube/bookinfo.yaml
kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.23/samples/bookinfo/platform/kube/bookinfo-versions.yaml
# kubectl get pods

kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.23/samples/bookinfo/gateway-api/bookinfo-gateway.yaml
kubectl annotate gateway bookinfo-gateway networking.istio.io/service-type=ClusterIP --namespace=default
# kubectl get gateway
kubectl port-forward svc/bookinfo-gateway-istio 8080:80
# http://localhost:8080/productpage


### ref: https://istio.io/latest/docs/ambient/getting-started/secure-and-visualize/
kubectl label namespace default istio.io/dataplane-mode=ambient
kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.23/samples/addons/prometheus.yaml
kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.23/samples/addons/kiali.yaml


#
kubectl label namespace default istio-injection=enabled
kubectl port-forward -n istio-system svc/kiali 20001:20001
```

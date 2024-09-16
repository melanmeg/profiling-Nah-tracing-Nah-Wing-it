# profiling-Nah-tracing-Nah-Wing-it

```bash
# ref: https://github.com/melanmeg/k8s_1-31_on_nobel
# ./composeは検証用

# ref: https://kubernetes.io/docs/tasks/debug/debug-cluster/resource-metrics-pipeline/
# リソース メトリック パイプライン
```

```bash
タスク
・otel
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

- Memo2
```bash
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: kube-scheduler-configmap-reader
rules:
- apiGroups: [""]
  resources: ["configmaps"]
  verbs: ["list", "get"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: kube-scheduler-binding
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: kube-scheduler-configmap-reader  # 新しい ClusterRole に変更
subjects:
- apiGroup: rbac.authorization.k8s.io
  kind: User
  name: system:kube-scheduler
```

`kubectl auth can-i list configmaps --as system:kube-scheduler`


- Memo3
```bash
kubectl create clusterrolebinding kubernetes-admin-binding \
  --clusterrole=cluster-admin --user=kubernetes-admin

kubectl get clusterrolebinding
kubectl get rolebinding --all-namespaces
```

`kubectl auth can-i list nodes --as=kubernetes-admin -A`

```bash
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: kubernetes-admin-binding
subjects:
- kind: User
  name: kubernetes-admin
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: cluster-admin
  apiGroup: rbac.authorization.k8s.io
```

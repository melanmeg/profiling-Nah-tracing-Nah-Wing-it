# Hey yo

- profiling-Nah-tracing-Nah-Wing-it

```bash
# ref: https://github.com/melanmeg/k8s_1-31_on_nobel
# ./composeは検証用

# ref: https://kubernetes.io/docs/tasks/debug/debug-cluster/resource-metrics-pipeline/
# リソース メトリック パイプライン
```

```bash
タスク
・grafana
・minio
・loki
・otel
```

- マイグレーションコマンド
```bash
kubeadm config migrate --old-config /tmp/init_kubeadm.yaml --new-config new_init_kubeadm.yaml
kubeadm config migrate --old-config /tmp/join_kubeadm_cp.yaml --new-config new_join_kubeadm_cp.yaml
kubeadm config migrate --old-config /tmp/join_kubeadm_wk.yaml --new-config new_join_kubeadm_wk.yaml
```

- Memo
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

```bash
kubectl label node k8s-wk-4 node-role.kubernetes.io/worker=
kubectl label node k8s-wk-5 node-role.kubernetes.io/worker=
```

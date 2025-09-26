kubectl delete -f ./dataSaver/k8s.yml
kubectl delete -f ./frontend/searchQuery/k8s.yml
# kubectl delete -f db.yml

kubectl apply -f ./dataSaver/k8s.yml
kubectl apply -f ./frontend/searchQuery/k8s.yml
kubectl apply -f db.yml

kubectl apply -f ingress.yml
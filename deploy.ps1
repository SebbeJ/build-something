kubectl apply -f ./dataSaver/k8s.yml
kubectl apply -f ./frontend/addBook/k8s.yml
kubectl apply -f ./frontend/searchQuery/k8s.yml

kubectl apply -f ingress.yml
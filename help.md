#Commande pour créer l'image docker

docker build -t jsquaremay/admin:latest .
docker build -t jsquaremay/agent:latest .

#Commande pour pusher les images

docker push jsquaremay/admin:latest
docker push jsquaremay/agent:latest

#Voir la rendue sur kubernetes

kubectl get all --all-namespaces

#Commande Kubernetes

kubectl apply -f rabbitmq.yaml
kubectl apply -f apps.yaml

#Voir les pods 
kubectl get pods

#commande pour lancer les consommeurs
kubectl exec -it name_pode -- bash

#consommer
Pyhton manage.py consumer

#Restart 
kubectl get deployments
kubectl rollout restart deployments/name : restart un deploiement
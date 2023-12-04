export FLASK_APP=app.py

flask run

pytest

docker build -t py-test-image:tag .
docker run -p 5000:5000 py-test-image:tag

minikube start

kubectl apply -f dp-sv01.yaml




kubectl expose deployment web-app --type=NodePort --port=5000

minikube ip
kubectl get services

minikube service web-app-service --url

http://<minikube-ip>:<NodePort>

http://192.168.49.2:80


kubectl get pods
kubectl describe deployment web-app
kubectl get svc web-app-service
kubectl logs <pod-name>

minikube profile list


docker tag your-docker-image:tag ibrezm1/test-kube-img:tag1

docker push ibrezm1/test-kube-img:tag1

kubectl delete deploy  web-app
kubectl delete secret web-app-secret
kubectl delete svc web-app-service


helm create web-app-chart

helm package web-app-chart
helm install web-app-release web-app-chart-0.1.0.tgz
minikube service web-app-release-web-app-chart --url
# QA Test Deployment on Minikube

## Prerequisites
- Docker
- Minikube
- kubectl
- Python with `pytest` and `requests` modules

## Steps

1. Start Minikube:
   bash
   minikube start --driver=docker
   eval $(minikube docker-env)

2. deploy both the frontend and backend services using "kubectl"

3. To access the frontend service in Minikube, expose it using:
	* minikube service frontend-service

4. After Run above command, we will get new page in browser, in this url "https://***.**.**.*:30145"

5. We will get info "Hello from the Backend!"

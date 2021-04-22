install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

build:
	docker build -t flask-change:latest .

run:
	docker run -p 80:80 flask-change

run-kube:
	kubectl apply -f kube-hello-change.yaml

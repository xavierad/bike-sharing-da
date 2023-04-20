build:
	docker build . -t london

run: build
	docker run london -p 8080:8080
.PHONY: help install build build-front build-back dev-front dev-back docker-build docker-run clean

BINARY_NAME=subs4r-server
DOCKER_IMAGE=subs4r:latest

help: ## Show available commands
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  install       Install frontend dependencies"
	@echo "  build         Build both frontend and Go backend"
	@echo "  build-front   Build React production bundle"
	@echo "  build-back    Build Go server binary"
	@echo "  dev-front     Run Vite dev server (port 5173)"
	@echo "  dev-back      Run Go backend in dev mode (port 8080)"
	@echo "  docker-build  Build multi-stage Docker image"
	@echo "  docker-run    Run Docker container on port 8080"
	@echo "  clean         Remove build artifacts"

install:
	npm install

build-front:
	npm run build

build-back:
	cd backend && go build -trimpath -ldflags="-s -w" -o ../$(BINARY_NAME) .

build: build-front build-back ## Build full production stack

dev-front:
	npm run dev

dev-back:
	cd backend && go run .

docker-build: ## Build Docker container
	docker build -t $(DOCKER_IMAGE) .

docker-run: ## Run Docker container
	docker run --rm -p 8080:8080 $(DOCKER_IMAGE)

clean: ## Clean build outputs
	rm -rf dist $(BINARY_NAME) $(BINARY_NAME).exe backend/$(BINARY_NAME) backend/$(BINARY_NAME).exe

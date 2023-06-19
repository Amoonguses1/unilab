PROJECT_NAME=template
FILE_NAME=python_3_10
USER=haruki
IMAGE_NAME=${USER}_${PROJECT_NAME}
CONTAINER_NAME=${USER}_${PROJECT_NAME}
PORT=8887
SHM_SIZE=2g
FORCE_RM=true

build:
	docker build \
		-f $(FILE_NAME)/Dockerfile \
		-t $(IMAGE_NAME) \
			--no-cache \
		--force-rm=$(FORCE_RM) \
		.
restart: stop start

run:
	docker run \
		-dit \
		-v C:\Users\1019k\Desktop\lab\unilab:/workspace \
		-p $(PORT):$(PORT) \
		--name $(CONTAINER_NAME) \
		--rm \
		--shm-size $(SHM_SIZE) \
		$(IMAGE_NAME)

stop:
	docker stop $(IMAGE_NAME)

exec:
	docker exec \
		-it \
		$(CONTAINER_NAME) bash 
---
title: docker publish Gitlab CI/CD jobs Template
description: How to use No Fuss Computings gitlab-ci job template to publish a docker image to docker hub.
date: 2023-06-10
template: project.html
about: https://gitlab.com/nofusscomputing/projects/gitlab-ci
---

This GitLab CI template is designed to publish Docker images to Docker Hub. It contains a job called "Publish Docker Image to Docker Hub" that handles the image publishing process.


## Stage

- `publish`


## Variables

The following variables are used in the job:

- `DOCKER_IMAGE_BUILD_NAME`: The name of the Docker image to build. By default, it uses the GitLab CI project name.

- `DOCKER_IMAGE_BUILD_REGISTRY`: The registry for the Docker image build. By default, it uses the GitLab CI registry image.

- `DOCKER_IMAGE_BUILD_TAG`: The tag for the Docker image build. By default, it uses the GitLab CI commit SHA.

- `DOCKER_IMAGE_BUILD_TARGET_PLATFORMS`: A comma-separated list of available platforms for the Docker image build. Supported platforms include: `linux/amd64`, `linux/amd64/v2`, `linux/amd64/v3`, `linux/arm64`, `linux/riscv64`, `linux/ppc64`, `linux/ppc64le`, `linux/s390x`, `linux/386`, `linux/mips64le`, `linux/mips64`, `linux/arm/v7`, `linux/arm/v6`.

- `CI_REGISTRY_USER`: The username for logging in to the GitLab CI registry.

- `CI_REGISTRY_PASSWORD`: The password for logging in to the GitLab CI registry.

- `NFC_DOCKERHUB_USERNAME`: The username for logging in to Docker Hub.

- `NFC_DOCKERHUB_TOKEN`: The access token or password for logging in to Docker Hub.

- `DOCKER_IMAGE_PUBLISH_REGISTRY`: The registry for publishing the Docker image to Docker Hub.

- `DOCKER_IMAGE_PUBLISH_NAME`: The name of the Docker image for publishing to Docker Hub.

- `DOCKER_IMAGE_PUBLISH_URL`: The URL to access the published Docker image on Docker Hub.


## Services

- `docker:23-dind`: Runs Docker in Docker (DinD) service with version 23.


## Script

The job executes the following steps in the `script` section:

1. Logs in to the GitLab CI registry using the provided credentials (`CI_REGISTRY_USER` and `CI_REGISTRY_PASSWORD`).

2. If the `DOCKER_IMAGE_BUILD_TARGET_PLATFORMS` variable is specified, it iterates over the platforms and inspects the Docker image using `docker buildx imagetools inspect`.

3. If the `DOCKER_IMAGE_BUILD_TARGET_PLATFORMS` variable is not specified, it pulls the Docker image from the specified registry.

4. Logs in to Docker Hub using the provided credentials (`NFC_DOCKERHUB_USERNAME` and `NFC_DOCKERHUB_TOKEN`).

5. Lists the Docker images using `docker image ls`.

6. Determines the appropriate tag for the Docker image based on the pipeline source and commit tag.

7. If the `DOCKER_IMAGE_BUILD_TARGET_PLATFORMS` variable is specified, it creates multi-arch images using `docker buildx imagetools create` and tags them with the appropriate tag.

8. If the `DOCKER_IMAGE_BUILD_TARGET_PLATFORMS` variable is not specified, it tags the Docker image with the appropriate tag based on the pipeline source and commit tag.

9. Pushes the Docker image to Docker Hub.

10. Logs out of Docker Hub.


## Environment

The job sets the following environment variables:

- **Name**: DockerHub

- **URL**: The URL to access the published Docker image on Docker Hub.


## Rules

The job is controlled by the following rules:

- Runs when the pipeline is triggered by a Git tag and there is no associated branch.

- Runs when the pipeline is triggered by a push to the `master` branch and there is a Dockerfile present.

- Runs when the pipeline is triggered by a push to the `development` branch, there are changes in the Dockerfile or the `includes/` directory compared to the `master` branch, and it allows failure.

- Never runs explicitly.


## gitlab-ci.yml definition

``` yaml title=".gitlab-ci.yml" linenums="1"

--8<-- "docker/build.gitlab-ci.yaml"

```

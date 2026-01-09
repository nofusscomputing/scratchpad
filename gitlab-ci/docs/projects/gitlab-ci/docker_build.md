---
title: docker build Gitlab CI/CD jobs Template
description: How to use No Fuss Computings gitlab-ci template for auto creation of CI/CD joobs.
date: 2023-06-10
template: project.html
about: https://gitlab.com/nofusscomputing/projects/gitlab-ci
---

This documentation provides an overview and explanation of the GitLab CI/CD YAML template. The template defines a job named `.build_docker_container` that builds a Docker container using the specified configuration.


### Stage: build

This job builds a Docker container using the `nofusscomputing/docker-buildx-qemu:dev` image and the `docker:23-dind` service.


#### Variables

- `DOCKER_IMAGE_BUILD_NAME`: The name of the Docker image to be built (`$CI_PROJECT_NAME`).

- `DOCKER_IMAGE_BUILD_REGISTRY`: The registry where the Docker image will be pushed (`$CI_REGISTRY_IMAGE`).

- `DOCKER_IMAGE_BUILD_TAG`: The tag to be applied to the Docker image (`$CI_COMMIT_SHA`).


#### Rules

- Rule 1: The job runs if the pipeline is triggered by a git tag and a `dockerfile` or `dockerfile.j2` file exists.

- Rule 2: The job runs if the pipeline is triggered by a push to the `development` branch and a `dockerfile` or `dockerfile.j2` file exists. It also checks for changes in the `dockerfile`, `dockerfile.j2`, or `includes/` directory compared to the `master` branch.

- Rule 3: The job runs if the pipeline is triggered by a push to a branch other than `master` or `development` and a `dockerfile` or `dockerfile.j2` file exists. It also checks for changes in the `dockerfile`, `dockerfile.j2`, or `includes/` directory compared to the `development` branch.

- Rule 4: The job never runs.


#### Script

The script performs the following steps:

1. Updates the binary formats and enables execution of other binary formats in the kernel.

2. Creates a Docker buildx builder and sets it as the active builder.

3. Builds a multi-arch Docker image if the `DOCKER_IMAGE_BUILD_TARGET_PLATFORMS` variable is specified. It applies labels to the image and pushes it to the specified registry. It also inspects the image and performs cleanup by removing additional unknown images from the container registry.

4. Builds a Docker image if the `DOCKER_IMAGE_BUILD_TARGET_PLATFORMS` variable is not specified. It applies labels to the image and pushes it to the specified registry.


## gitlab-ci.yml definition

``` yaml title=".gitlab-ci.yml" linenums="1"

--8<-- "docker/build.gitlab-ci.yaml"

```

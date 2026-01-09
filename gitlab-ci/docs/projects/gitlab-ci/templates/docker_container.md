---
title: Docker Container CI Template
description: How to use No Fuss Computings gitlab-ci template for docker containers
date: 2023-05-13
template: project.html
about: https://gitlab.com/nofusscomputing/projects/gitlab-ci
---

- available tags `dev` for latest dev build

- latest matches latest git tag


- notate available platforms can be viewed in the job

- notate that resource groups are used. also mention that the resource group allows the git tag pipeline as forced to wait for the previous pipeline, tag push to build the image first

``` yaml

  # Available platforms: linux/amd64, linux/amd64/v2, linux/amd64/v3, linux/arm64, linux/riscv64, linux/ppc64, linux/ppc64le, linux/s390x, linux/386, linux/mips64le, linux/mips64, linux/arm/v7, linux/arm/v6
  # DOCKER_IMAGE_BUILD_TARGET_PLATFORMS: "linux/amd64,linux/arm64,linux/arm/v7"
  DOCKER_IMAGE_BUILD_NAME: $CI_PROJECT_NAME
  DOCKER_IMAGE_BUILD_REGISTRY: $CI_REGISTRY_IMAGE
  DOCKER_IMAGE_BUILD_TAG: $CI_COMMIT_SHA
  
  # DOCKER_IMAGE_PUBLISH_NAME: $CI_PROJECT_NAME
  # DOCKER_IMAGE_PUBLISH_REGISTRY: docker.io/nofusscomputing
  # DOCKER_IMAGE_PUBLISH_URL: https://hub.docker.com/r/nofusscomputing/$DOCKER_IMAGE_PUBLISH_NAME
  # JOB_STOP_CONVENTIONAL_COMMITS: 'any_value'
  # JOB_STOP_GIT_PUSH_MIRROR: 'any_value'
  # GIT_SYNC_URL: "https://$GITHUB_USERNAME_ROBOT:$GITHUB_TOKEN_ROBOT@github.com/NoFussComputing/config.git" # Must be defined for job to run
  # JOB_STOP_GITLAB_RELEASE: 'any value'

```

!!! Note
    Docs Still under development

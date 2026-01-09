---
title: MKDocs Static Site Build
description: How to use No Fuss Computings gitlab-ci job for MKDocs Static Site Build
date: 2021-08-11
template: project.html
about: https://gitlab.com/nofusscomputing/projects/gitlab-ci
---


Build a MKDocs site from the config specified in `mkdocs.yml`. _Only runs if `mkdocs.yml` exists in the repository root directory._ This job is designated to run on all branchs so that you can use the artifacts for deployment to `staging` and/or `production` as required.

This job provides the following badge:

- _None_

## Dependencies

- **Mandatory** file `mkdocs.yml` in the repository root directory with your MKDocs configuration

## your .gitlab-ci.yml changes

To use this job add the following to your `.gitlab-ci.yml` file

``` yaml

stages:
    - build

include:
    - local: CI/build/.gitlab-ci.yml

MKDocs build:
  variables:
    MKDOCS_BUILD_PATH: "build"
  extends:
    - .MKDocs_Build

```


## CI/CD Variables required

| var name | Description |
|:----:|:----|
| MKDOCS_BUILD_PATH | **Mandatory, if different from default** The path where MKDocs places the build files. Defaults to `build` |
| MKDOCS_INCLUDE_SOURCE | **Optional** Include the build source files in the artifacts. Default is Not set. Any value in this variable, will include the source files. |
| MKDOCS_SOURCE_PATH | **Optional, if source files are not to be included** Set to the path where mkdocs uses to build the static html. |


## Job Workflow

1. install mkdocs

    1. if file `requirements.txt` exists in the repository root directory, use this fill to also install additional dependencies.

    1. if no `requirements.txt` file exists, only install mkdocs.

1. run mkdocs to build the static pages

1. if variable `$MKDOCS_INCLUDE_SOURCE` is set, then copy `$MKDOCS_SOURCE_PATH` to the artifacts location.

1. copy directory `$MKDOCS_BUILD_PATH` to the artifacts location.


## Artifacts

- files in `"$CI_PROJECT_DIR/artifacts/$CI_JOB_STAGE/$CI_JOB_NAME"`


## Gitlab job Definition

When you include this definition the following makes up the job definition

``` yaml title=".gitlab-ci.yml" linenums="1"

--8<-- "mkdocs/.gitlab-ci.yml"

```

!!! Note
    Docs Still under development

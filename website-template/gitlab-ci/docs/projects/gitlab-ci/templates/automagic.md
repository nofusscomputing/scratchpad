---
title: Automatic Gitlab CI/CD jobs Template
description: How to use No Fuss Computings gitlab-ci template for auto creation of CI/CD joobs.
date: 2023-05-22
template: project.html
about: https://gitlab.com/nofusscomputing/projects/gitlab-ci
---

This template is designed to autodetect which jobs should be created. By including it within your project, the jobs will be automagically created for the pipeline.


## Docs ToDo

- document variables `PIPELINE_RUN_TRIGGER: 'false'` and `PIPELINE_RUN_SCHEDULE: 'false'` as being used as a gate to enable the jobs to run by the specified source.


!!! Note
    Docs Still under development



## gitlab-ci.yml definition

``` yaml title=".gitlab-ci.yml" linenums="1"

--8<-- "template/automagic.gitlab-ci.yaml"

```

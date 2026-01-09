---
title: Ansible
description: How to use No Fuss Computings gitlab-ci job for ansible
date: 2021-08-03
template: project.html
about: https://gitlab.com/nofusscomputing/projects/gitlab-ci
---

This job does ansible role/playbook linting when any commit is pushed to any branch.


This job provides the following badge:

- None


## Dependencies

- None


## your .gitlab-ci.yml changes

To use this job add the following to your `.gitlab-ci.yml` file

``` yaml

stages:
    - validation

include:
    - remote: https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/raw/development/ansible/.gitlab-ci.yml

Ansible Lint (python 3.6):
    variables:
        ANSIBLE_LINT_PATH: "roles/"
    extends:
        - .ansible_linter_defaults
    image: python:3.6-slim

```

> You can use any python version you wish.


## CI/CD Variables required

| var name | Description |
|:----:|:----|
| ANSIBLE_LINT_PATH | *The path you wish the linter to search for ansible roles/playbooks* |


## Job Workflow

- This job will lint any yml file in the specified directory using ansible rules.


## Artifacts

- `$CI_PROJECT_DIR/artifacts` - Root artifact directory

- `$CI_PROJECT_DIR/artifacts/$CI_JOB_STAGE/tests/$PYTHON_VERSION-ansible-lint.junit.xml` - JUnit Test report

- `$CI_PROJECT_DIR/artifacts/$CI_JOB_STAGE/$CI_JOB_NAME/$PYTHON_VERSION-ansible-lint.log` - Linter log

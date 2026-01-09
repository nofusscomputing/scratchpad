---
title: Python
description: How to use No Fuss Computings gitlab-ci job for Python
date: 2021-08-11
template: project.html
about: https://gitlab.com/nofusscomputing/projects/gitlab-ci
---


This folder (`python`) covers jobs for python development


These jobs provides the following badge:

- `PyLint` - code quality [![PyLint Score](https://img.shields.io/badge/dynamic/json?&style=plastic&logo=python&label=PyLint%20Score&query=%24.PyLintScore&url=https%3A%2F%2Fgitlab.com%2Fnofusscomputing%2Fprojects%2Fgitlab-ci%2F-%2Fjobs%2Fartifacts%2Fdevelopment%2Fraw%2Fartifacts%2Fvalidation%2FPyLint%2Fbadge_pylint.json%3Fjob%3DPyLint)](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/jobs/artifacts/development/file/artifacts/validation/tests/gl-code-quality-report.html?job=PyLint)

Use the following MD to add a badge adjusting the variables and ensuring everything is on one line.

``` md

[![PyLint Score](https://img.shields.io/badge/dynamic/json?&style=plastic&logo=python&label=PyLint%20Score&query=%24.PyLintScore&url=https%3A%2F%2Fgitlab.com%2F

{project path}

%2F-%2Fjobs%2Fartifacts%2F

{branch}

%2Fraw%2Fartifacts%2Fvalidation%2FPyLint%2Fbadge_pylint.json%3Fjob%3D

{Job Name}

)](https://gitlab.com/

{project path}

/-/jobs/artifacts/

{branch}

/file/

artifacts/validation/tests/gl-code-quality-report.html

?job=

{Job Name}
)

```

|  Variable  |  Description  |
|:----|:----|
| `{project path}` | *project path, what's after gitlab.com/* |
| `{branch}` | *git branch to fetch the score from* |
| `{Job Name}` | *name of the gitlab-ci job for the linting* |


## Dependencies

- None


## your .gitlab-ci.yml changes

To add the `PyLint` job, add the following to your `.gitlab-ci.yml` file

``` yaml

stages:
    - validation

include:
    - remote: https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/raw/master/python/.gitlab-ci.yml

PyLint:
    variables:
        PYLINT_PATH: "/*/*.py"
        PYLINT_RC_PATH: "."
    extends:
        - .PyLint
    image: python:3.6-slim

```


## CI/CD Variables required

| var name | Description |
|:----:|:----|
| PYLINT_PATH | *The path you wish the linter to search for python files* |
| PYLINT_RC_PATH | *The path to your `.pylintrc` file.* |


## Job Workflow

- This job will lint any yaml file in the specified directory using the specified rules.


## Artifacts

- `$CI_PROJECT_DIR/artifacts` - Root artifact directory

- `$CI_PROJECT_DIR/artifacts/$CI_JOB_STAGE/tests/gl-code-quality-report.json` - Gitlab code quality report (displays in merge request)

- `$CI_PROJECT_DIR/artifacts/$CI_JOB_STAGE/tests/gl-code-quality-report.html` - html code quality report


## Gitlab job Definition

When you include this definition the following makes up the job definition

``` yaml title=".gitlab-ci.yml" linenums="1"

--8<-- "python/.gitlab-ci.yml"

```

!!! Note
    Docs Still under development

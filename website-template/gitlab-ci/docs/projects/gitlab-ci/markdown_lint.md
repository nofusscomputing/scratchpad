---
title: Markdown File Linting
description: How to use No Fuss Computings gitlab-ci job for markdown linting
date: 2021-08-11
template: project.html
about: https://gitlab.com/nofusscomputing/projects/gitlab-ci
---

This job lints markdown files as part of the validation CI stage. It is designated to run on all branches. If any errors are found, the generated JUnit test report will let you know what errors were found.

You can include your linting rules in `.markdownlint.json` which should be within the root of your repository. for the available rules please see the [docs](https://github.com/DavidAnson/markdownlint/blob/main/README.md#rules--aliases).

This job provides the following badge:

- _None_


## Dependencies

- **Optional** file `.markdownlint.json` in repository root with any rules you wish to specify


## your .gitlab-ci.yml changes

To use this job add the following to your `.gitlab-ci.yml` file

``` yaml

stages:
    - validation

include:
    - local: CI/validation/.gitlab-ci.yml

Markdown Linting:
  extends:
    - .Lint_Markdown

```


## CI/CD Variables required

| var name | Description |
|:----:|:----|
| MDLINT_PATH | **Optional** specifies the path to lint. defaults to `"**/*.md"` |
| MDLINT_EXCLUDE_PATHS | **optional** Specifies the paths to exclude from linting. Defaults to `"!gitlab-ci"` |
| MD_LINT_CONFIG-PATH | **Optional** Specifies a path whenre the lint config file is. defaults to none. this variable enables you to specify a config that will be copied to the project root folder. ***Note:** if specified, the file will be deleted at the end of the linting job.*


## Job Workflow

1. installs the required job dependencies

1. Lints any markdow file found in `$MDLINT_PATH`, excluding paths `$MDLINT_EXCLUDE_PATHS`


## Artifacts

- JUnit test report located at `$CI_PROJECT_DIR/artifacts/$CI_JOB_STAGE/tests/*.junit.xml`


## Gitlab job Definition

When you include this definition the following makes up the job definition

``` yaml title=".gitlab-ci.yml" linenums="1"

--8<-- "lint/markdown.gitlab-ci.yaml"

```

!!! Note
    Docs Still under development

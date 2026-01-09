---
title: Git push mirror
description: How to use No Fuss Computings gitlab-ci job for repository mirrororing
date: 2021-08-03
template: project.html
about: https://gitlab.com/nofusscomputing/projects/gitlab-ci
---

This job does a git push to a remote git repo.


This job provides the following badge:

- None


## Dependencies

- None


## your .gitlab-ci.yml changes

To use this job add the following to your `.gitlab-ci.yml` file

``` yaml

stages:
    - sync

include:
    - remote: https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/raw/development/git_push_mirror/.gitlab-ci.yml

Github (Push --mirror):
    variables:
        GIT_SYNC_URL: "https://${username variable}:${pasword variable}@github.com/NoFussComputing/gitlab-ci.git"
    extends:
        - .git_push_mirror

```


## CI/CD Variables required

| var name | Description |
|:----:|:----|
| GIT_SYNC_URL | this is the remote git repositories https clone address. <br>***Note:** if the remote repository requires authentication, you will need to build the url. like above.* |


## Job Workflow

- This job is designed to run on successful completion of the validation tasks and only on the `development` and `master` branches. You can safely override the `rules` when creating the job with your own. i.e.

``` yaml

Github (Push --mirror):
    variables:
        GIT_SYNC_URL: "https://${username variable}:${pasword variable}@github.com/NoFussComputing/gitlab-ci.git"
    extends:
        - .git_push_mirror
    rules:
      - if: '$CI_COMMIT_BRANCH == "master"'
        when: never
      - if: '$CI_COMMIT_BRANCH == "development"'
        when: always

```

This will cause the job to only run on the `development` branch.


## Artifacts

- None


## Gitlab job Definition

When you include this definition the following makes up the job definition

``` yaml title=".gitlab-ci.yml" linenums="1"

--8<-- "git_push_mirror/.gitlab-ci.yml"

```

!!! Note
    Docs Still under development

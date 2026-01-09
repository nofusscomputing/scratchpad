---
title: No Fuss Computings Gitlab-CI Project
description: How to use No Fuss Computings gitlab-ci project within your CI/CD pipelines
date: 2023-05-22
template: project.html
about: https://gitlab.com/nofusscomputing/projects/gitlab-ci
---

!!! Note
    Docs Still under development


## Docs ToDo

- Templates folder is for `gitlab-ci.yaml` that automagically create the jobs if included

- other sub folders are for `` which **DO NOT** automagically create jobs, but are pure definitions only.

- notate how each of the stages run and under what circumstance. *i.e. gitlab-ci.yml rules.exist/rules.changes*

## CI Stages

The CI stages for these jobs are as follows, and in the order expected by the jobs:

- chores
    > automated tasks

- validation
    > validation of files, commits,  Merge Request titles, code quality, license checks.

- build
    > build any binaries or files that would be used in the later stages .

- prepare
    > any jobs that must run after build but before testing. for example a docker image build that includes artifacts from the build job

- test
    > unit, functional, integration and any other tests.

- release
    > git tagging and creating a gitlab release. Also includes adding build artifacts to gitlab registry.

- sync
    > repository synchronization, i.e. push mirror to github.

- publish
    > placement of build objects to external sources


## Git Sub-Module setup

It is recommended that you set-up this repo as a git sub-module to your repo and that you configure it to a set commit/tag. This ensures that any change to `gitlab-ci` repo, does not effect your CI/CD jobs.

run the following commands:

``` bash

git submodule add -b {ref} https://gitlab.com/nofusscomputing/projects/gitlab-ci.git gitlab-ci
git submodule update --remote

```

!!! Tip
    NOTE: `{ref}` should be replaced with the branch name, `master` is the stable branch and recommended. by default the sub-module will be created in folder `gitlab-ci`, it is recommended that you **don't** change this folder name.  

    You can also substitute the gitlab url with the github url `https://github.com/NoFussComputing/gitlab-ci.git` for the submodule if you desire. this repo is auto-synced with github on each change to the repo.

After each `git submodule update --remote` you will have to commit the sub-module update to your repo. Suggested commands as follows:

``` bash

git add .gitmodules 

git add gitlab-ci

git commit -m "ci(gitlab-ci): updated to use version x

{your reason here or explain what is provided/changed}"

```

Then push the changes to your source.


## .gitlab-ci.yaml example

example:

``` yaml

include:
  - project: nofusscomputing/projects/gitlab-ci
    ref: master
    file:
      - .gitlab-ci_common.yaml
      - $JOB_ROOT_DIR/{filepath to include here and is relative to the gitlab-ci repo root}

variables:
    MY_PROJECT_ID: "{your_project_id}"

```

!!! Tip
    Use a project import in your `.gitlab-ci.yml` file that is tied to a specific `ref`. for example a branch, commit or tag. Also ensure that the `gitlab-ci` `git sub-module` and the `ref` as part of the includes matches.*


## Artifacts

Any artifacts by jobs will be created in folders named after the stage.

preference is placed on jobs to output JUnit.xml test reports. This is because they are visible in merge requests.

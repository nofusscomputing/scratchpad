---
title: Conventional Commits
description: How to use No Fuss Computings gitlab-ci job for Conventional Commits
date: 2021-08-03
template: project.html
about: https://gitlab.com/nofusscomputing/projects/gitlab-ci
---

## User Manual

Commitizen is used to validate the format of commit messages. we use [Conventional Commit Messages](https://www.conventionalcommits.org/en/v1.0.0/) format for our validation jobs.

This repository may have two CI jobs to do with commitizen:

- **MR Title** *Checks the Merge Request Title*

- **Commit Messages** *Checks all commit messages*

These CI Jobs output a test report that can be viewed inside of the merge request and contain the error(s), if any.

To fix an error please refer to the titled sections below.


### MR Title

Ensure that the merge request title is in the [conventional message](https://www.conventionalcommits.org/en/v1.0.0/) format. NOTE: the title is case sensitive.


### Commit Messages

All commit messages that form part of your merge request must be in [conventional message](https://www.conventionalcommits.org/en/v1.0.0/) format.

To fix them go back and edit your commit messages.


#### fixing commit messages (suggestion)

If only the last commit is the commit with an error just use `git commit --amend` and edit your commit message to be in the correct format and save. now push your changes.

You will require the following information if the commit message with the error is further down the commit tree:

- Commit message SHA1 of your first commit message to the branch `{original_commit}`

- Commit message SHA1 prior to your first commit `{source_commit}`

Run these commands once you have the information above.

``` bash

git format-patch {original_commit}..HEAD -o ../diff-patches

git reset {source_commit} --hard

```

Now, navigate to the `diff-patches` folder, open up the offending patch (commit) and edit the `subject` or message body as appropriate and save. Once all the edits have been done, re-apply the patches to your tree with:

``` bash

git am ../diff-patches/*.patch

```

Now push your changes upstream.

| :notebook_with_decorative_cover: Note  |
|:-----:|
|  *As you have changed the commit SHA1(s), when you next push your changes upstream, you must force push. `git push --force`*  |

| :octagonal_sign: **WARNING**  |
|:-----:|
|  *Ensure that all of your commits were exported prior to reseting the branch and when re-applying, that all of your commits were applied correctly*  |


## GitLab CI Template - `.conventional_commit`

This GitLab CI template, named `.conventional_commit`, is designed to validate conventional commits within a GitLab CI/CD pipeline. It follows predefined rules to ensure that commit message conventions are met.


### your .gitlab-ci.yml changes

To use this job add the following to your `.gitlab-ci.yml` file

``` yaml

variables:
    GIT_SUBMODULE_STRATEGY: recursive
    MY_PROJECT_ID: "{yourproject id number}"

stages:
    - validation

include:
    - remote: https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/raw/development/conventional_commits/.gitlab-ci.yml

```


### Job Description

The `.conventional_commit` job performs various tasks related to validating conventional commits. It runs in the `validation` stage of the pipeline and uses the `python:3.6-slim` Docker image.


### Variables

- `DEFAULT_ROOT_DIR`: The default root directory is set as `./gitlab-ci`.

- `MR_ACCESS_TOKEN`: The access token for the merge request. If not defined, it falls back to `CI_JOB_TOKEN`.

- `JOB_ROOT_DIR`: The root directory for the job. If not defined, it falls back to `DEFAULT_ROOT_DIR`.

- `MY_PROJECT_ID`: The custom project ID. If not defined, it falls back to `CI_PROJECT_ID`.


### Stages

- `validation`: The job is assigned to the `validation` stage.


### Script

The script section contains the actions performed during the job execution. These actions include creating directories, setting up variables, preparing the Python environment, and executing commands related to validating conventional commits.

The complete script can be found in the GitLab CI template file.


### Artifacts

The job generates artifacts that are stored for a period of 3 days. The artifacts include the following paths:

- `$CI_PROJECT_DIR/artifacts/*`

- `$CI_PROJECT_DIR/artifacts/$CI_JOB_STAGE/tests/*.junit.xml`


### Rules

The job follows certain rules to determine when it should be executed:

- If the variable `$JOB_STOP_CONVENTIONAL_COMMITS` is true, the job will not run.

- If the branch is pushed and a commit is made, and there is no tag associated with the commit, and the pipeline source is "push", the job will run if `.cz.yaml` file exists.

- In all other cases, the job will not run.

This GitLab CI template provides a convenient way to validate conventional commits and enforce commit message conventions within your CI/CD pipelines.


## Gitlab job Definition

When you include this definition the following makes up the job definition

``` yaml title=".gitlab-ci.yml" linenums="1"

--8<-- "conventional_commits/.gitlab-ci.yml"

```

---
title: Gitlab Release / Commit Footer References
description: How to use No Fuss Computings gitlab-ci job for Gitlab Releases and commit footer messages
date: 2021-08-03
template: project.html
about: https://gitlab.com/nofusscomputing/projects/gitlab-ci
---


## User Manual

All commit messages must be in [conventional commit format](https://www.conventionalcommits.org/en/v1.0.0/) and have a footer with a gitlab reference. The reference **must** be either a merge request or a gitlab issue. (format i.e. `!1` or `#2` *using the correct reference number*).


### fixing commit messages

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


## GitLab CI Template - Developer Manual


## Job: gitlab_release

This job bumps the version, updates the changelog, creates a git tag and creates a gitlab release. The git tag and release title use [semantic versioning](https://semver.org/). for this job to function correctly a `.cz.yaml` is required in the root of the repository. this file contains the [commitizen](https://github.com/commitizen-tools/commitizen) config and the version details.

!!! Alert
    *If prior to merging to the master branch you do a version increment, and there are no commits prior to merging. the job will not increment the version and the job will fail. it is recommended that you only do a version increment on the `development` branch if you are going to commit further changes to the `development` branch*


### Stage

`release`


### Image

The job uses the `registry.gitlab.com/gitlab-org/release-cli:latest` image.


### Variables

The job does not use any additional variables.


### Explanation

The `gitlab_release` job is responsible for creating releases and tags for the GitLab repository. It follows a specific release workflow and utilizes the `release-cli` tool to automate the release process.


### Steps

1. Set ROOT_DIR variable: Sets the `ROOT_DIR` variable based on the value of `JOB_ROOT_DIR`.

2. Create necessary directories: Creates necessary directories for storing artifacts and tests.

3. Install dependencies: Updates the package manager and installs Git and Python 3. Sets up the Python environment by installing required packages.

4. Clone repository: Clones the repository using the provided authentication token and checks out the `development` branch.

5. Configure Git: Configures Git settings for the release process.

6. Perform release steps: Executes release-related steps, such as running a custom command (`$MY_COMMAND`), generating the release changelog, and tagging the release.

7. Push changes: Pushes the changes to the GitLab repository.

8. Cleanup: Removes the cloned repository.


### Rules

- The job is never triggered when `$JOB_STOP_GITLAB_RELEASE` is true.

- The job is never triggered when the commit author is `nfc_bot <helpdesk@nofusscomputing.com>`.

- If the commit is pushed to the `master` branch, the job is only triggered on successful pipeline execution and failure is not allowed.

- If the commit is pushed to the `development` branch, the job is triggered manually and failure is allowed.


### your .gitlab-ci.yml changes

To use this job add the following to your `.gitlab-ci.yml` file

CI Job `ci commit footer` is automatically set to run on all branches except `development` and `master`. This job checks the commits on the users branch that they contain a footer with gitlab references. i.e. `#1` for issue one or `!1` for merge request one.

``` yaml

stages:
    - validate
    - release

include:
    - remote: https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/raw/development/gitlab_release/.gitlab-ci.yml

Gitlab Release:
    variables:
        MY_COMMAND: "{your command here}"
    extends:
        - .gitlab_release

```

> if you wish to run any commands you can add them to variable `MY_COMMAND`. The custom command will run under shell `/bin/sh`. This command is set to run before the version bump commit is conducted so any changes you wish to add as part of the version bump, you can do here as long as you `git add {changed file name}`.


## Job: commit_footer_refs


### Stage

`validation`


### Image

The job uses the `python:3.6-slim` image.


### Variables

- `DEFAULT_ROOT_DIR`: The default root directory path.


### Explanation

The `commit_footer_refs` job validates the commit footer references in the GitLab repository. It checks if the commit messages adhere to the conventional commit format and generates a JUnit XML report.


### Conventional Commits

Conventional commits follow a specific format for commit messages, consisting of a type, optional scope, and a message. The format is as follows:

```
<type>(<scope>): <message>
```

- The `<type>` represents the nature of the changes, such as `feat` for a new feature, `fix` for a bug fix, `docs` for documentation changes, and so on.

- The `<scope>` (optional) provides additional context for the commit, indicating the module, component, or area of code being modified.

- The `<message>` contains a concise and descriptive summary of the changes.

The commit footer can contain additional information, such as references to issues, feature requests, or pull requests.


### Steps

1. Create necessary directories: Creates necessary directories for storing artifacts and test results.

2. Set ROOT_DIR variable: Sets the `ROOT_DIR` variable based on the value of `JOB_ROOT_DIR`.

3. Install dependencies: Updates the package manager and installs Git and the required Python packages for the commit footer validation.

4. Clone repository: Clones the repository and checks out the specified branch.

5. Run commit_footer script: Executes the `commit_footer` script to validate the commit footer references.

6. Generate artifacts: Generates a JUnit XML report for the test results.


### Rules

- The job is never triggered when `$JOB_STOP_CONVENTIONAL_COMMITS` is true.

- The job is never triggered when `CHANGELOG_FOOTER_REFERENCES` is false.

- The job is always triggered when the commit is not pushed to the master or development branch, and a .cz.yaml file is present, indicating the usage of conventional commits.

- The job is never triggered otherwise.


## Gitlab job Definition

When you include this definition the following makes up the job definition

``` yaml title=".gitlab-ci.yml" linenums="1"

--8<-- "gitlab_release/.gitlab-ci.yml"

```

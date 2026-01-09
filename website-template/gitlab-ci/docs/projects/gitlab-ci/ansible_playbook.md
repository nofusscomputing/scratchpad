---
title: Ansible Playbook
description: How to use No Fuss Computings gitlab-ci job for running Ansible Playbooks
date: 2023-05-29
template: project.html
about: https://gitlab.com/nofusscomputing/projects/gitlab-ci
---

This job enables you to run an Ansible playbook within the Gitlab CI/CD environment.


There is also an additional job defined that enables you to specify a project to run an automated update of it's git submodules. This is useful if the project you create the job in, is used as a git submodule in another project. On pushing to the development branch, this job triggers the `Git.Submodules.Update.Chores` job that updates the specified projects git submodules.



## your .gitlab-ci.yml changes

- **Mandatory** In addition to the previous dependency, this requirement is for the project specified in the trigger job. The following must be added to the `.gitlab-ci.yml` file in that project.

``` yaml
include:
  - project: nofusscomputing/projects/gitlab-ci
    ref: master
    file:
      - .gitlab-ci_common.yaml
      - automation/template/automagic.gitlab-ci.yaml
```

To use the ansible playbook job add the following to your `.gitlab-ci.yml` file.

``` yaml

stages:
    - chores

include:
  - project: nofusscomputing/projects/gitlab-ci
    ref: master
    file:
      - automation/.gitlab-ci-ansible.yaml

Ansible Job:
  extends: .ansible_playbook
  variables:
    ansible_playbook: 'git_configuration.yaml'
    ansible_tags: 'submodule'
    PIPELINE_RUN_TRIGGER: 'false'
    PIPELINE_RUN_SCHEDULE: 'false'

```

To run the trigger job to update another projects git submodules. add the following to your `.gitlab-ci.yml` file

``` yaml

stages:
    - publish

include:
  - project: nofusscomputing/projects/gitlab-ci
    ref: master
    file:
      - automation/.gitlab-ci-ansible.yaml

Docker_Mail.Submodule.Deploy:
  extends: .submodule_update_trigger
  variables:
    SUBMODULE_UPDATE_TRIGGER_PROJECT: nofusscomputing/projects/docker-mail

```

!!! Tip
    In addition to the variables below, you can also specify any additional Environment variables for use by Ansible within the container. Refer to the [Ansible configuration documentation](https://docs.ansible.com/ansible/latest/reference_appendices/config.html#common-options) for further details


## Job: `.ansible_playbook`

This job runs an Ansible playbook using the `nofusscomputing/ansible-ee:dev` Docker image.


### Stage: Chores

This job is responsible for executing an Ansible playbook. It can be customized by setting the following variables:


#### Variables

- `ansible_inventory`: The Ansible inventory file.

- `ansible_playbook`: The name of the Ansible playbook file.

- `ansible_tags`: The tags to be applied during playbook execution.


### Rules

- Rule 1: If the `NFC_AUTO_JOBS` variable is set to `"false"`, the job will never run.

- Rule 2: If the pipeline is triggered by a schedule and `PIPELINE_RUN_SCHEDULE` is set to `"true"`, the job will run only if the `.nfc_automation.yaml` file exists.

- Rule 3: If the pipeline is triggered by an API call, another pipeline, a trigger, or a parent pipeline, and `PIPELINE_RUN_TRIGGER` is set to `"true"`, the job will run only if the `.nfc_automation.yaml` file exists.

- Rule 4: If the pipeline is triggered by a push to the `development` branch, the job will run only if the `.nfc_automation.yaml` file exists. see [Documentation](../git_configuration/submodule/) for file details.

- Rule 5: This rule prevents the job from running under any circumstances.


## Job: `.ansible_playbook_git_submodule`

This job extends the `.ansible_playbook` job and is specifically used for running the `git_configuration.yaml` playbook with the `submodule` tags.


### Stage: Chores

This job is responsible for executing the `git_configuration.yaml` playbook with the `submodule` tags.


#### Variables

- `ansible_playbook`: The name of the Ansible playbook file (`git_configuration.yaml`).

- `ansible_tags`: The tags to be applied during playbook execution (`submodule`).


### Rules

- Rule 1: If the `NFC_AUTO_JOBS` variable is set to `"false"`, the job will never run.

- Rule 2: If the pipeline is triggered by a schedule and `PIPELINE_RUN_SCHEDULE` is set to `"true"`, the job will run only if the `.nfc_automation.yaml` file exists.

- Rule 3: If the pipeline is triggered by an API call, another pipeline, a trigger, or a parent pipeline, and `PIPELINE_RUN_TRIGGER` is set to `"true"`, the job will run only if the `.nfc_automation.yaml` file exists. see [Documentation](../git_configuration/submodule/) for file details.

- Rule 4: If the pipeline is triggered by a push to the `development` branch, the job will run only if the `.nfc_automation.yaml` file exists.

- Rule 5: This rule prevents the job from running under any circumstances.


## Job: `.submodule_update_trigger`

This job triggers a pipeline in another project.


### Stage: Publish

This job is responsible for triggering a pipeline in another project.


#### Variables

- `PIPELINE_RUN_TRIGGER`: The flag to indicate if the triggered pipeline should run (`true`).


### Rules

- Rule 1: If the pipeline is triggered by a push to the `master` or `development` branch, and there is no associated tag, the job will run on successful completion.

- Rule 2: This rule prevents the job from running under any other circumstances.


## Artifacts

- None


## gitlab-ci.yml definition

``` yaml title=".gitlab-ci.yml" linenums="1"

--8<-- "automation/.gitlab-ci-ansible.yaml"

```

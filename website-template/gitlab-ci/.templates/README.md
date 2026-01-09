# {CI Job Name}

Summary of job here

This job provides the following badge:

{A badge here}


## Dependencies

- {dependent job name}


## your .gitlab-ci.yml changes

To use this job add the following to your `.gitlab-ci.yml` file

``` yaml

variables:
    VARNAME: "a var value"

stages:
    - {new stage name}

include:
    - local: CI/{job name}/.gitlab-ci.yml

```


## CI/CD Variables required

| var name | Description |
|:----:|:----|
| NEW VAR | this var does this and bka |


## Job Workflow


## Artifacts


## License

To view the license for this folder and any sub-folders, refer [here](https://gitlab.com/nofusscomputing/projects/gitlab-ci)

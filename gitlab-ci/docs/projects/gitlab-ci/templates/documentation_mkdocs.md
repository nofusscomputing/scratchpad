---
title: mkdocs documentation Gitlab CI/CD Template
description: How to use No Fuss Computings gitlab-ci template for building docs with mkdocs
date: 2023-05-22
template: project.html
about: https://gitlab.com/nofusscomputing/projects/gitlab-ci
---

This template creates the jobs applicable to publishing pages to a website. The website in question is a static site built by MKDocs.


## Docs ToDo

- notate that var `PAGES_ENVIRONMENT_PATH:` can be set to the slug of the page to show and is used for launching the environment to the url that contains the docs index page.

- notate that resource groups are used.

## Dependencies

- **Mandatory** file `docs/index.md` this is the index page of your dcoumentation.


!!! Note
    Docs Still under development


## gitlab-ci.yml definition

``` yaml title=".gitlab-ci.yml" linenums="1"

--8<-- "template/mkdocs-documentation.gitlab-ci.yaml"

```
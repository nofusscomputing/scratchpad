#!/bin/sh

for D in *; do
    if [ -d "${D}" ]; then

      if [ "0${D}" != "0website-template" ] && [ "0${D}" != "0docs" ]; then
        echo "[DEBUG] Creating changelog for sub-folder: ${D}"

        CHANGELOG_DATA=$(git log --pretty="format:%ci [%h](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/%H) - %s  " --follow -- "${D}")

        echo "# Changelog" > ${D}/CHANGELOG.md

        echo "" >> ${D}/CHANGELOG.md
        echo "$CHANGELOG_DATA" >> ${D}/CHANGELOG.md

        git add ${D}/CHANGELOG.md

      fi
    fi
done

# Changelog

2023-05-28 10:31:26 +0930 [bade89c](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/bade89c5333ca853844e224f46a2d3dafab7179d) - fix(scheduled_pipelines): if scheduled pipeline only run schedualable jobs  
2023-05-24 04:40:52 +0000 [0a17fe1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/0a17fe1aa320c658c05d7a693ff76af4a54e6130) - build(version): bump version 0.6.1rc1 → 0.6.1rc2  
2023-05-21 01:48:53 +0930 [088c9fb](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/088c9fb04c80961f4de8d2b129955ae8cd0b9529) - feat(conventional_commits): ensure .cz.yaml exists  
2023-05-15 00:18:38 +0000 [a3fdca8](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/a3fdca83bf7acb58d47792a66d1cd0728747361c) - build(version): bump version 0.6.1rc0 → 0.6.1rc1  
2023-05-15 09:32:15 +0930 [93931cb](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/93931cb9076e0db238f4e297abe3d8f37bd71b80) - feat(conventional): job not to run when bot pushes change  
2023-05-15 09:23:02 +0930 [76db5b1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/76db5b17578d8585ed31e0728dbfb37ea2fae153) - fix(conventional_commits): never run on git tag  
2023-05-14 14:10:06 +0930 [02e9e5f](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/02e9e5f4f4cc0b93ae92c7ba3a2cfb38305af64c) - refactor(ci): inconsistant tabs  
2023-05-14 12:11:42 +0930 [d389d14](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/d389d14192e1e483fbd48fa9b5c5bee25db14a20) - fix: validation jobs on all except merge  
2023-05-14 09:56:35 +0930 [934a401](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/934a401a9620891b09a5fe9c9b0e50a97b43fa9b) - fix(ci): specify the commitizen version  
2023-05-13 15:35:28 +0930 [408e4ea](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/408e4eab9e1f61004f1e38af6d1531747b7da99b) - refactor: move docs as part of restructure  
2023-05-13 11:47:21 +0930 [9e7d357](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/9e7d357bab2b92704d37ad5621df9fe8d1e31a26) - feat(conventional_commits): ability to disable job with variable  
2022-01-25 00:08:05 +0000 [ce1cc01](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/ce1cc017e26ff7f6cee586cc7d98e4d292275672) - build(version): bump version 0.6.0 → 0.6.1rc0  
2022-01-24 06:33:24 +0000 [46cc1fb](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/46cc1fbb6a878e485af39e679b5184a9912c2e7f) - build(version): bump version 0.5.0 → 0.6.0  
2022-01-16 00:09:42 +0000 [1ef6c41](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/1ef6c41818c40183f8019ea5cde48b4278e4d694) - build(version): bump version 0.4.0 → 0.5.0  
2022-01-16 09:02:02 +0930 [31517b4](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/31517b4bf00c1f177ef925d09b1a6714577f62c5) - ci(MR_Title): save the merge request title as a variable and debug output in job log.  
2022-01-16 08:48:24 +0930 [73918f2](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/73918f2f5e19440d0e300da3a20712739c316d88) - fix(commit.py): filter merge request search to 'opened' and on current branch.  
2022-01-15 03:53:53 +0000 [5c9000a](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/5c9000a74859504ed64bbefa1fd193f80a2b69c2) - build(version): bump version 0.3.1 → 0.4.0  
2022-01-15 13:14:58 +0930 [e5531fc](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/e5531fc77b5bdb1ccc0741e388df2d8d25ba6ade) - feat(commit.py): throw an error if no token was supplied. i.e. empty variable.  
2022-01-15 13:07:56 +0930 [6b7ad95](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/6b7ad95fc0ccccf79ff645bad3f86660f5096a4e) - feat(commit.py): confirm a merge request was found, if not output 'ci: No Merge Request found'  
2022-01-15 13:05:30 +0930 [c543c47](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/c543c47af8c7c386ae57f5a7a50904d396758c3a) - feat(commit.py): try to us `CI_JOB_TOKEN` before the specified token, if any.  
2022-01-15 12:29:23 +0930 [99bdc2a](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/99bdc2a0929d4e7036e50e8ce22ce9b0f90f0736) - fix(commit.py): fix typo that caused exception  
2022-01-15 12:23:54 +0930 [d03d9fe](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/d03d9fefc916dd6730d9ffa778c11d48d621318e) - fix(conventional_commits): fetch all branches prior to check for parent branch  
2022-01-15 12:18:15 +0930 [b01550e](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/b01550e09f273edc8a57f4ad4b41ee2d67705d41) - feat(commit.py): removed ability to fetch first commit or target branch  
2022-01-15 12:04:07 +0930 [42ad02e](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/42ad02ee5db65c3c6c33ad14fe0371c9916897bf) - fix(conventional_commits): use git show-branch to find origin branch  
2022-01-11 07:03:09 +0000 [7751fd9](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/7751fd9494f610fff0ea16bd303bfe62d0034eec) - build(version): bump version 0.3.0 → 0.3.1  
2021-08-12 03:32:36 +0000 [389bc08](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/389bc08d7686153fb374aa83d440c35c9b4eac90) - build(version): bump version 0.3.0rc1 → 0.3.0  
2021-08-12 12:47:23 +0930 [3360a15](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/3360a15fde12682edfd9044d2541dc819615b838) - fix(commit_message): fixed commit message check if there is only one commit to the branch  
2021-08-11 13:47:34 +0930 [def31ef](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/def31ef562c0002713401652657d59320548ee85) - style(yaml_lint): fixed yaml lint errors  
2021-08-04 03:23:08 +0000 [eb5cc8a](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/eb5cc8a0e2885a9ed16a8d1a81611aec4d5a4d31) - build(version): bump version 0.3.0rc0 → 0.3.0rc1  
2021-08-04 03:13:54 +0000 [09dcb65](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/09dcb65b090f59e9f8a6bea5eba4bb98bddbad3d) - build(version): bump version 0.2.1 → 0.3.0rc0  
2021-08-04 02:49:45 +0000 [4453b43](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/4453b433c8966a334f02af592a6ce8092f2ac9de) - build(version): bump version 0.2.0 → 0.2.1  
2021-08-04 02:24:12 +0000 [856f2e1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/856f2e1770d0bda823996122ee70916dc0fe455b) - build(version): bump version 0.1.0 → 0.2.0  
2021-08-04 01:33:47 +0000 [6d34977](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/6d349774269bcd7c6e406cfe72c78b99f246df7b) - build(version): bump version 0.0.1 → 0.1.0  
2021-08-03 13:26:05 +0930 [392a200](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/392a200fd469c4161dbab5f2b59031a7a64f20a2) - feat(conventional_commits): Added conventional commit job  

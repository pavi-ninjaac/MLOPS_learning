# GitHub actions

The integrated tool in GitHub which is used for CI/CD Workflow.
- imported terminologies:
    - GitHub Events: All kind of tasks/events happens **IN OR TO the repo**. Ex: pull, push, MR, Clone, etc.
    - GitHub Actions: We can setup few/more sequential tasks to run when any on the GitHub events are happening.

- The places to note:
    - Our CI/CD code present inside the repo . path - repo/.github/workflows/pipeline_name.yaml
    - We have the example actions present in "Action" top tab of all the repo.
    - We have all the list of github events in: https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows
    - We have all the list of github pre-defined actions in: https://github.com/actions


## Syntax of the CI/CD yaml files.
```

name: Greetings

on: [pull_request_target, issues]

jobs:
  greeting:
    runs-on: ubuntu-latest
    permissions:
      issues: write
      pull-requests: write
    steps:
    - uses: actions/first-interaction@v1
      with:
        repo-token: ${{ secrets.GITHUB_TOKEN }}
        issue-message: "Message that will be displayed on users' first issue"
        pr-message: "Message that will be displayed on users' first pull request"
```

```
name: <some-name> (optional)

on: (required)                                                 --------------> # Events that triggers the following job.
    push:
        branches: <bran-name>
    pull_request:
        branches: <branch-name>

jobs:                                                          --------------> # One/more jobs : jobs.<job.id>
    first_job:

        runs-on: [ubuntu-latest, windows-latest]               --------------> # Talks about the os/env to run the job on.

        steps:                                                 --------------> # Sequence of tasks
            - name: <name-of-the-step>
                uses: actions/checkout@v2                      --------------> # uses is used to say we are using a pre-defined actions.
                with:                                          --------------> # This is the variables needed for the pre-defined actions.
                    java-versions: 1.8

            - name: <second-step>
                runs: chmod +x test_file.py                    --------------> # Used to run a cmd. any cmd Ex. linux cmd, docker cmd, etc.

    second_job:
        ...
```
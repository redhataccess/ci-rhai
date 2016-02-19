ci-rhai
============

JJB(Jenkins Job Builder) configuration files to be used to run robottelo tests for Red Hat Insights.

Installation
------------
Make sure you have pip installed on your system.
```
pip install -r requirements.txt
```

Update the Jenkins Job configuration file.
```
cp jenkins_jobs.ini.sample jenkins_jobs.ini
```

Make appropriate changes to the file.
```
[jenkins]
user=<jenkin-user>
password=<jenkins-api-key>
url=<jenkins-url>
```

Generating jobs
---------------
To test the generation of jobs:
```
jenkins-jobs --conf jenkins_jobs.ini test jobs
```

To update the jobs on Jenkins:
```
jenkins-jobs --conf jenkins_jobs.ini update jobs
```

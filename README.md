# Street Art Photography Website [![Build Status](https://travis-ci.com/simonhowlett/app-engine-ci.svg?branch=master)](https://travis-ci.com/simonhowlett/app-engine-ci) |  [![simonhowlett](https://circleci.com/gh/simonhowlett/app-engine-ci.svg?style=svg)](https://app.circleci.com/pipelines/github/simonhowlett/app-engine-ci)


Simple Workflow for a release architecture proven for a simple website app build.

Simple Application using:
- gCloud
- python 3 
- flask & jinja2
- Bootstrap
 Simple test automation - webdriver tests (python, selenium), Puppeteer Tests.
 - Google Analytics Tracking

Environment:
- appEngine
- CI/CD integration/reporting/unit tests etc (no real reason to build on both travis and circle, more than seeing the differences).
- Jira Integration

Notes:
 - /visit/ - Collects/Displays visitor timestamps, just a simple datastore write example.
 - /info/ - sample user contact form, commits comments to firestore/datastore, with confirmation and failure responses
 - ?debug=true URL Query String wil reveal a test menu, in time there will be more hidden functions.
 - Directory of helper files, some are unrelated examples that are for reference/working into something else.
 
 Todo:
- Image manipulation using gcloud's image framework, pulling from storage etc (tbd)
- Auto deploy on branch name
- Test output reporting
- GCloud notifications on new entity created
- Comments display API / View



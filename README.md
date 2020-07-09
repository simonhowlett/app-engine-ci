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

Todo:
- Image manipulation using gcloud's image framework, pulling from storage etc (tbd)
- Auto deploy on branch name
- Test output reporting
- Fake image ordering option, more for test examples than anything else.

Notes:
?debug=true URL Query String wil reveal a test menu, in time..



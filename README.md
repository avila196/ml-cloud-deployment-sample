# ml-cloud-deployment-sample

The current repository is the starting point for a Topics Classifier and its further deployment into a cloud environment.

### Structure
The overall structure for the repositiry is as follows:
* README.md: Current README file for the repo
* dummy_app/: This directory contains a dummy application (no ML model at all) just to test a lighter version
* full_app/: This directory contains the full application, using a TF NLP classifier. Docker image ~ 4.5gb

Both directories contain the same files:
* app/: Directory containing the main application (to be served using Flask). This is a topics classifier, so the app loads the model file and expose the needed API endpoints for it. 
* Dockerfile: Used to construct the docker image for the application
* Makefile: Used to run common instructions (`docker build` and `docker run` mainly)
* requirements.txt: Requirements needed for the docker image (model libs and serving framework mainly)
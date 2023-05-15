# ml-cloud-deployment-sample

The current repository is the starting point for a Topics Classifier and its further deployment into a cloud environment.

### Structure
The overall structure for the repositiry is as follows:
* app/: Directory containing the main application (to be served using Flask). This is a topics classifier, so the app loads the model file and expose the needed API endpoints for it. 
* Dockerfile: Used to construct the docker image for the application
* Makefile: Used to run common instructions (`docker build` and `docker run` mainly)
* README.md: Readme file for the repo
* requirements.txt: Requirements needed for the docker image (model libs and serving framework mainly)
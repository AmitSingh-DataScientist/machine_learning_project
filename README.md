## machine_learning_project
### This is my first machine learning project
#### Software and account login requirements:

1. [Github Account](https://github.com)
2. [Heroku Account](https://id.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT Cli](https://git-scm.com/downloads)
5. [Git Documentatio](https://git-scm.com/docs/gittutorial)

Creating conda environment
```
conda create -p venv python==3.7 -y
conda activate venv/
OR
conda activate venv

pip install -r requirements.txt
```
To Add files to git
```
git add .
OR
git add <file_name>
```
Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

To check the git status
```
git status
```
To check all version maintained by git
```
git log
```
To create version/commit all changes by git
```
git commit -m "message"
```
To send version/changes to github
```
git push origin main
```
To check remote url
```
git remote -v
```
To setup CI/CD pipeline in heroku we need 3 information
1. HEROKU_EMAIL = amitsingh.dataanalytics@gmail.com
2. HEROKU_API_KEY = e7c1b6a9-a423-4220-b7eb-cb5ad6bd3451
3. HEROKU_APP_NAME = ml-app-regression

BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname> .
```
Note: Image name for docker must be lowercase

To list docker image
```
docker images
Run docker image
docker run -p 5000:5000 -e PORT=5000 f8c749e73678
```
To check running container in docker
```
docker ps
```
To stop docker conatiner
```
docker stop <container_id>
```

To Run all the commands at one place, do not need to run any other file
```
python setup.py install
```

To install all dependencies within __init__ file under housing folder
```
pip install -e .
```
.py file is called as Module whereas folder that contains __init__ module file  is called Package

setup.py file is created for Build & Distribute purpose - Build the solution and distribute to others

install ipykernel
```
pip install ipykernel
```
Data Drift:
When your dataset stats gets change we call it as data drifts. We actually try to compare stats or graph of one dataset with other if there isn't any major chnage we say no data drift, if there is drastical changes then we say there is Data Drift.

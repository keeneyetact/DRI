# REFERENCE GUIDE

Document à destination des développeurs. Vous trouverez toutes les informations nécessaires pour reproduire un projet similaire.

# Table of contents
1. [Github](#github)
2. [Commandes utiles](#1)
3. [Pipenv](#2)
4. [Flask](#3)
5. [MongoDB](#4)
6. [Scrapy](#5)
7. [Pymongo](#6)
8. [Docker](#7)
	1. [Cheat sheet Docker](#2)

<a name="github"></a>
## Github

Créez un repository sur Github. Puis clonez-le sur votre machine :

```bash
git clone https://github.com/v-barbosavaz/DRIO4302C
```

## Commandes utiles

Se déplacer dans le répertoire de travail :

```bash
cd DRIO4302C/
```

Supprimer les fichiers cachés _DS_Store_ récursivement :

```bash
find . -name '.DS_Store' -type f -delete  
```

Créer un fichier _.gitignore_ :

```bash
touch .gitignore
```

Ouvrir le fichier : 

```bash
open .gitignore
```

Ecrivez dans ce fichier tout ce qui doit être ignoré par Git. Pour en savoir plus : https://github.com/github/gitignore

Regardez ce que contient le fichier :

```bash 
cat .gitignore
```

Un workflow assez simple d'utilisation de Git :

```bash
git add .
git commit -m "initial commit"
git push -u origin master
```

## Mac

Afficher les fichiers cachés sous macOS Mojave (utile pour éditer .gitignore par exemple) :

```bash
fn + CMD + Shift + .
```

```bash
chflags nohidden /path/to/dir/.gitignore
```

```bash
ls -al path/to/dir
```

```bash
defaults write com.apple.Finder AppleShowAllFiles YES
killall Finder
```

## Pipenv

http://sametmax.com/pipenv-solution-moderne-pour-remplacer-pip-et-virtualenv/
https://github.com/v-barbosavaz/DataEngineerTools
https://pipenv.readthedocs.io/en/latest/basics/

mise à jour de pip, au niveau utilisateur pour ne pas casser le système
```bash
python -m pip install pip --upgrade --user
```

installation de pipenv
```bash
python -m pip install pipenv --user
```

à la racine du projet
```bash
pipenv install
```

Lancer un terminal à l'interieur de cet environnment :
```bash
pipenv shell
```

Installer de nouvelles librairies :
```bash
pipenv install <votre_librairie>
```

Sortir du shell :
```bash
Ctrl + D
```

Produire une fichier requirements.txt qui contient toutes les librairies et dépendances nécessaires pour faire tourner le projet :
```bash
pipenv lock -r > requirements.txt
```

Une autre façon de le faire :
```bash
pipenv lock --requirements > requirements.txt
```

## Flask

```bash
pipenv install Flask  
pipenv run python app/__init__.py
```

## MongoDB

### Installation

https://treehouse.github.io/installation-guides/mac/mongo-mac.html

#### Install and Run MongoDB with Homebrew

```bash
brew update
brew install mongodb
mkdir -p /data/db
sudo chown -R `id -un` /data/db
mongod
mongo
quit()
ctrl-c
```

### Lancer mongo dans docker

```bash
docker-compose run mongo /bin/bash
mongo
```

## Scrapy

Ce framework va nous permettre de récupérer des données des sites web.

```bash
pipenv install scrapy
```

## Pymongo

```bash
pipenv install pymongo
```

### Get / Post

https://stackoverflow.com/questions/24892035/python-flask-how-to-get-parameters-from-a-url

## Et si on commençait les choses correctement ?

Ce repo va nous permettre à travers cookiecutter de créer tout un environnement pour notre application Flask.

Les dossiers nécessaires seront créés, les erreurs HTTP gérées etc. Il s'agit donc d'un environnement que vous pouvez utiliser pour démarrer toutes vos applications Flask.

https://github.com/konstantint/cookiecutter-flask-boilerplate

https://github.com/audreyr/cookiecutter

## Bien utile

https://medium.com/@greut/building-a-python-package-a-docker-image-using-pipenv-233d8793b6cc

http://exploreflask.com/en/latest/organizing.html

https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet

## À regarder

https://realpython.com/flask-by-example-part-1-project-setup/

https://code.tutsplus.com/tutorials/templating-with-jinja2-in-flask-essentials--cms-25571

https://stackoverflow.com/questions/30954599/what-is-the-significance-of-flask-bin-python-in-flask

https://getbootstrap.com/

https://code.tutsplus.com/tutorials/templating-with-jinja2-in-flask-essentials--cms-25571

https://github.com/svola/fantasticsearch

http://jsfiddle.net/vxvyvyer/1/

```bash
pipenv install elasticsearch --skip-lock
```

https://docs.docker.com/get-started/part2/

## Termes

Boilerplate

shebang

## ElasticSearch

```bash
pip install elasticsearch
```

## useiconic

https://useiconic.com/open

## jQuery

https://jquery.com/download/

## Popper

https://stackoverflow.com/questions/45661863/bootstrap-min-js6-uncaught-error-bootstrap-dropdown-require-popper-js

## Carousel

https://bootsnipp.com/snippets/zDQkr

## Lancer le projet

```bash
pipenv run python run.py
```

build l'image :

```bash
docker-compose up
``` 

run app :

```bash
docker run -p 5000:5000 -it drio4302c_app
```

http://0.0.0.0:5000/

http://localhost:9200/




## Problème pipenv install

Impossible d'installer twited : fatal error: 'stdio.h' file not found

```bash
xcode-select --install
```

```bash
open /Library/Developer/CommandLineTools/Packages/macOS_SDK_headers_for_macOS_10.14.pkg
```

```bash
pipenv lock --requirements > requirements.txt
pip install -r requirements.txt
```

## Docker

```bash
docker images -a
```

```bash
docker image prune -a
```

```bash
docker images -aq
```

```bash
docker images
```

```bash
docker images --help
```

```bash
docker ps -a
```

```bash
docker rm 5f4fb47a5716
```

```bash
docker-compose ps
```

```bash
docker-compose logs -f app
```

```bash
docker-compose ps -a
```

```bash
docker rmi $(docker images -aq)
```

```bash
docker rm $(docker ps -aq)
```

```bash
docker-compose up -d
```

Open bash in docker image :
```bash
docker run -it --entrypoint=/bin/bash drio4302c_app
```

### Cheat sheet Docker

List the running containers
```bash
docker ps
```

Stops containers and removes containers, networks, volumes, and images created by docker-compose up
```bash
docker-compose down
```

List all running containers
```bash
docker container ls
```

List all containers, even those not running
```bash
docker container ls -a
```

List all images on this machine
```bash
docker image ls -a
```

Remove specified image from this machine
```bash
docker image rm <image id>
```

Remove all images from this machine
```bash
docker image rm $(docker image ls -a -q)
```

Remove all containers
```bash
docker container rm $(docker container ls -a -q)
```

Remove specified container from this machine
```bash
docker container rm <hash> 
```

Gracefully stop the specified container
```bash
docker container stop <hash>
```

Force shutdown of the specified container
```bash
docker container kill <hash> 
```

```bash
docker build -t friendlyhello .  # Create image using this directory's Dockerfile
docker run -p 4000:80 friendlyhello  # Run "friendlyname" mapping port 4000 to 80
docker run -d -p 4000:80 friendlyhello         # Same thing, but in detached mode
docker login             # Log in this CLI session using your Docker credentials
docker tag <image> username/repository:tag  # Tag <image> for upload to registry
docker push username/repository:tag            # Upload tagged image to registry
docker run username/repository:tag                   # Run image from a registry
```
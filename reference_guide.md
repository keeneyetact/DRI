# REFERENCE GUIDE
Documentation du code. Répliquer le projet.  

## Github

On clone le projet :

```bash
git clone https://github.com/v-barbosavaz/DRIO4302C
```

cd DRIO4302C/  
find . -name '.DS_Store' -type f -delete  
touch .gitignore  
open .gitignore  
cat .gitignore  
git add .  
git commit -m "initial commit"  
git push -u origin master  

https://github.com/github/gitignore

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

lancer un terminal à l'interieur de cet environnment
```bash
pipenv shell
```

installer de nouvelles librairies
```bash
pipenv install <votre_librairie>
```

sortir du shell
```bash
Ctrl + D
```

Producing a requirements.txt file
```bash
pipenv lock -r > requirements.txt
```

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




## Scrapy

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

Bien quitter docker :

```bash
docker-compose down
```

```bash
docker container ls
```

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
docker ps
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

Ouvrir le bash de notre image docker :

```bash
docker run -it --entrypoint=/bin/bash drio4302c_app
```

```bash

```

```bash

```

```bash

```

```bash

```

```bash

```

```bash

```

```bash

```
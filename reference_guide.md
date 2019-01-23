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

## Pipenv

http://sametmax.com/pipenv-solution-moderne-pour-remplacer-pip-et-virtualenv/
https://github.com/v-barbosavaz/DataEngineerTools

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

## Flask

```bash
pipenv install Flask  
pipenv run python app/__init__.py
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


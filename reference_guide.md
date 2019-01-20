# REFERENCE GUIDE
Documentation du code. Répliquer le projet.  

## Github

git clone https://github.com/v-barbosavaz/DRIO4302C  
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
python -m pip install pip --upgrade --user

installation de pipenv
python -m pip install pipenv --user

à la racine du projet
pipenv install

lancer un terminal à l'interieur de cet environnment
pipenv shell

installer de nouvelles librairies
pipenv install <votre_librairie>

sortir du shell
Ctrl + D

Producing a requirements.txt file
pipenv lock -r > requirements.txt

## Flask

pipenv install Flask  
pipenv run python app/__init__.py

## Et si on commençait les choses correctement ?

Ce repo va nous permettre à travers cookiecutter de créer tout un environnement pour notre application Flask.

Les dossiers nécessaires seront créés, les erreurs HTTP gérées etc. Il s'agit donc d'un environnement que vous pouvez utiliser pour démarrer toutes vos applications Flask.

https://github.com/konstantint/cookiecutter-flask-boilerplate

https://github.com/audreyr/cookiecutter

## Bien utile

https://medium.com/@greut/building-a-python-package-a-docker-image-using-pipenv-233d8793b6cc

http://exploreflask.com/en/latest/organizing.html

## À regarder

https://realpython.com/flask-by-example-part-1-project-setup/

https://code.tutsplus.com/tutorials/templating-with-jinja2-in-flask-essentials--cms-25571

https://stackoverflow.com/questions/30954599/what-is-the-significance-of-flask-bin-python-in-flask

https://getbootstrap.com/

## Termes

Boilerplate

shebang

## ElasticSearch

pip install elasticsearch

## useiconic

https://useiconic.com/open

## Lancer le projet

pipenv run python run.py



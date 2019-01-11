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

## bien utile

https://medium.com/@greut/building-a-python-package-a-docker-image-using-pipenv-233d8793b6cc

## ElasticSearch

pip install elasticsearch



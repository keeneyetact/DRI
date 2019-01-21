# Image de base
FROM python:3.7

# Dépendances extraites de l'environnement pipenv
ADD requirements.txt /usr/local/
RUN pip install --upgrade pip &&  pip install -r /usr/local/requirements.txt

# Installation de la db mongo
RUN apt-get update
RUN apt-get install -y mongodb

# Démarrage de la db
RUN service mongodb start

# Ajout des fichiers de l'app
ADD app /usr/local/app
ADD run.py /usr/local/

# Mapping des ports
EXPOSE 5000:5000

RUN chmod -R 755 /usr/local/
RUN python /usr/local/run.py

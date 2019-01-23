# Image de base
FROM python:3.7

# Ajout des fichiers du projet
COPY /app ./app
COPY run.py .
COPY requirements.txt .

# Dependances extraites de l'environnement pipenv
RUN pip install --upgrade pip &&  pip install -r requirements.txt

# Lancement de l'app
ENTRYPOINT ["python"]
CMD ["run.py"]




#############################

# Installation de la db mongo
#RUN apt-get update
#RUN apt-get install -y mongodb

# Démarrage de la db
#RUN service mongodb start

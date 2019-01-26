# Use an official Python runtime as a parent image
FROM python:3.7

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

#ENV http_proxy http://147.215.1.189:3128
#@ENV https_proxy http://147.215.1.189:3128

#COPY run.py .
#COPY requirements.txt .

# Install any needed packages specified in requirements.txt
# Dependances extraites de l'environnement pipenv
RUN pip install --upgrade pip && pip install -r requirements.txt

# Lancement de l'app
ENTRYPOINT ["python"]
#CMD ["python", "run.py"]
CMD ["run.py"]




#############################

# Installation de la db mongo
#RUN apt-get update
#RUN apt-get install -y mongodb

# Démarrage de la db
#RUN service mongodb start

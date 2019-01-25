#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, \
request, url_for
from elasticsearch import Elasticsearch
from flask_pymongo import PyMongo

from app import app

app.config["MONGO_URI"] = "mongodb://localhost:27017/test"
mongo = PyMongo(app)

# @app.route("/")
# def hello():
#     return "Hello World!"

# @app.route('/<name>')
# def hello_name(name):
#     return "Hello {}!".format(name)

@app.route('/')#, methods=['GET', 'POST'])
def index():
    #if request.method == 'POST' or request.method == 'GET':
    #    print(request.form)
        # if request.form['btn_recommender']: #== 'Do Something':
        #     return redirect(url_for('recommender'))

    return render_template('index.html')

@app.route('/search')
def search():
    return render_template('index.html')

@app.route('/recommender')
def recommender():
    return render_template('recommender.html')

# #http://127.0.0.1:5000/movie/Friends
# @app.route('/movie/<title>')
# def movie(title):
#     return render_template('movie.html', title=title)



#http://127.0.0.1:5000/title/0108778
@app.route('/title/<title>')
def title(title):
    serie = mongo.db.tv_series.find_one({"IMDB_id": title})
    if serie is None:
        return render_template('404.html')

    w_title = serie["title"]
    w_desc = serie["description"]
    w_url = serie["image_url"]

    try:
        recommandations = [(mongo.db.tv_series.find_one({"IMDB_id": rec_id})["title"],rec_id) for rec_id in serie["recommandations"]]
    except Exception as e:
        print(e)
        recommandations = ""
    return render_template('movie.html', title=w_title, desc = w_desc, url = w_url, rec = recommandations)



#http://127.0.0.1:5000/movie?title=Friends&description=A+great+serie
@app.route('/movie', methods=['GET'])
def daily_post():
    #do your code here
    return render_template("movie.html",title=request.args.get('title'), desc=request.args.get('description'))

# Set up simple error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(505)
def page_not_found(e):
    return render_template('505.html'), 505

# if __name__ == "__main__":
#     app.run()

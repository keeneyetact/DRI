#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, \
request, url_for, make_response, redirect
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from flask_pymongo import PyMongo
import os
from app import app


#es = Elasticsearch('http://localhost:9200')
#es = Elasticsearch(hosts="localhost")
# es = Elasticsearch('10.0.1.10', port=9200)


# document = {
#     "name":"Decision Trees",
#     "description":"A decision tree is a decision support tool that uses a tree-like graph or model of decisions and their possible consequences, including chance-event outcomes, resource costs, and utility. Take a look at the image to get a sense of how it looks like.",
#     "algo_type":"Supervised Learning"
# }

# res = es.index(index="algorithms", doc_type='algo', id=1, body=document)
# print(res['result'])

#LOCAL = True

#es_client = Elasticsearch(hosts=["localhost" if LOCAL else "elasticsearch"])
#es_client = Elasticsearch('http://localhost:9200')

#print(es_client.ping())

# app.config["MONGO_URI"] = "mongodb://localhost:27018/test"
# mongo = PyMongo(app)

app.config["MONGO_URI"] = "mongodb://localhost:27017/test"
mongo = PyMongo(app)

@app.route('/search/results', methods=['GET', 'POST'])
def search_request():
    search_term = request.form["input"]
    res = es.search(
        index="scrape-sysadmins",
        size=20,
        body={
            "query": {
                "multi_match" : {
                    "query": search_term,
                    "fields": [
                        "url",
                        "title",
                        "tags"
                    ]
                }
            }
        }
    )
    return render_template('results.html', res=res )

@app.route('/searchh')
def home():
    return render_template('search.html')


@app.route('/')#, methods=['GET', 'POST'])
def index():
    top15 = [mongo.db.tv_series.find_one({"popularity_rank": str(k)}) for k in range(1,16)]
    return render_template('index.html',top = top15)

@app.route('/search')
def search():
    return render_template('index.html')

@app.route('/recommender')
def recommender():
    return render_template('recommender.html')


@app.route('/title/<title>')
def title(title):
    serie = mongo.db.tv_series.find_one({"IMDB_id": title})
    if serie is None:
        return render_template('404.html')

    try:
        l_recommandations = []
        for rec_id in serie["recommandations"]:
            rec = mongo.db.tv_series.find_one({"IMDB_id": rec_id})
            l_recommandations.append(rec)

    except Exception as e:
        print(e)
        recommandations = ""
    return render_template('movie.html', **serie, l_rec = l_recommandations)



@app.route('/movie', methods=['GET'])
def daily_post():
    return render_template("movie.html",title=request.args.get('title'), desc=request.args.get('description'))


@app.route('/title', methods= ['POST'])
def setcookie2():
    if request.method == 'POST':
        user = request.form['nm']

    resp = make_response(redirect(url_for('title', title=user)) )
    resp.set_cookie('userID', user)

    return resp

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['nm']

    resp = make_response("setting_cookie")
    resp.set_cookie('userID', user)

    return resp

@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userID')
    return '<h1>welcome '+name+'</h1>'

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(505)
def page_not_found(e):
    return render_template('505.html'), 505

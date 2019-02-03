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


#app.config['MONGO_URI'] = os.environ.get('DB')


#client = MongoClient('localhost', 27017)
#mongo = client['test']

# @app.route("/")
# def hello():
#     return "Hello World!"

# @app.route('/<name>')
# def hello_name(name):
#     return "Hello {}!".format(name)



# @app.route('/')
# def index():
#     return '<h1>welcome '+'test'+'</h1>'



# def unlike(id_title):
#     try:
#         like = request.cookies.get(id_title)
#     except Exception as e:
#         print(0)



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
    #if request.method == 'POST' or request.method == 'GET':
    #    print(request.form)
        # if request.form['btn_recommender']: #== 'Do Something':
        #     return redirect(url_for('recommender'))
    top15 = [mongo.db.tv_series.find_one({"popularity_rank": str(k)}) for k in range(1,16)]

    return render_template('index.html',top = top15)

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

    try:
        l_recommandations = []
        for rec_id in serie["recommandations"]:
            rec = mongo.db.tv_series.find_one({"IMDB_id": rec_id})
            l_recommandations.append(rec)

    except Exception as e:
        print(e)
        recommandations = ""
    return render_template('movie.html', **serie, l_rec = l_recommandations)



#http://127.0.0.1:5000/movie?title=Friends&description=A+great+serie
@app.route('/movie', methods=['GET'])
def daily_post():
    #do your code here
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

    #resp = make_response(redirect('/movie'))
    resp = make_response("setting_cookie")
    #resp = make_response(render_template('readcookie.html'))
    resp.set_cookie('userID', user)

    return resp
    #return render_template("movie.html",title=request.args.get('title'), desc=request.args.get('description'))

@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userID')
    return '<h1>welcome '+name+'</h1>'

# Set up simple error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(505)
def page_not_found(e):
    return render_template('505.html'), 505

# if __name__ == "__main__":
#     app.run()

from flask import Flask, render_template, \
request, url_for
#from elasticsearch import Elasticsearch
app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "Hello World!"

# @app.route('/<name>')
# def hello_name(name):
#     return "Hello {}!".format(name)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST' or request.method == 'GET':
        print(request.form)
        # if request.form['btn_recommender']: #== 'Do Something':
        #     return redirect(url_for('recommender'))

    return render_template('index.html')

@app.route('/search')
def search():
    return render_template('index.html')

@app.route('/recommender')
def recommender():
    return render_template('recommender.html')


# Set up simple error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(505)
def page_not_found(e):
    return render_template('505.html'), 505

# if __name__ == "__main__":
#     app.run()
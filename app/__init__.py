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

# #http://127.0.0.1:5000/movie/Friends
# @app.route('/movie/<title>')
# def movie(title):
#     return render_template('movie.html', title=title)

#http://127.0.0.1:5000/title/tt0108778
@app.route('/title/<title>')
def title(title):
    w_title = ""
    w_desc = ""
    w_url = ""
    if(title == "tt0108778"):
        w_title = "Friends"
        w_desc = "A great serie"
        w_url = "https://m.media-amazon.com/images/M/MV5BNDVkYjU0MzctMWRmZi00NTkxLTgwZWEtOWVhYjZlYjllYmU4XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_UY268_CR0,0,182,268_AL_.jpg"
    return render_template('movie.html', title=w_title, desc = w_desc, url = w_url)


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
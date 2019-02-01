#!flask/bin/python

from app import app

if __name__ == '__main__':
    print("###################################")
    print("#######       START       #########")
    print("###################################")
    app.run(debug=True,host='0.0.0.0')
    #app.run(debug=True)

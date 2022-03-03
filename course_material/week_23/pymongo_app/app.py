from flask import Flask, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)

#setup mongo connection with database
app.config['MONGO_URI']="mongodb://localhost:27017/shows_db"
mongo = PyMongo(app)

#connect to collection
tv_shows = mongo.db.tv_shows

#READ
@app.route("/")
def index():
    #find all items in db and save to a variable
    all_shows = list(tv_shows.find())

    return render_template('index.html',data=all_shows)

if __name__ == "__main__":
    app.run(debug=True)

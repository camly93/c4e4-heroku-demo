from flask import Flask, render_template
import mongoengine
from mongoengine import Document, StringField

host = "ds011893.mlab.com"
port = 11893
db_name = "c4e_rss"
user_name = "c4e"
password = "codethechange"

mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html", movie_list = Movie.objects)

@app.route("/ly")
def hello_ly():
    return "Hello Ly"

@app.route("/<name>")
def hello(name):
    return "Hello " + name

#Render HTML file
@app.route("/test-render")
def test_render():
    return render_template("movie.html")

#Render HTML file with data
@app.route("/movie")
def movie():
    return render_template("movie_2.html",
                           title = "Civil War",
                           img = "http://media.comicbook.com/2016/04/civil-war-cap-tony-179110.jpg")

#Render HTML file with list of data
# class Movie:
#     def __init__(self, title, img):
#         self.title = title
#         self.img = img
#
# m1 = Movie(title="Kungfu Panda", img = "https://upload.wikimedia.org/wikipedia/en/7/76/Kungfupanda.jpg")
# m2 = Movie(title="Inception", img = "http://ia.media-imdb.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_SX640_SY720_.jpg")
# m3 = Movie(title="House of Cards", img = "http://vignette2.wikia.nocookie.net/house-of-cards/images/a/a8/House_of_Cards_Season_1_Poster.jpg/revision/latest?cb=20140217231358")
# m_list = [m1, m2, m3]

class Movie(Document):
    title = StringField()
    img = StringField()

@app.route("/movies")
def get_movies():
    return render_template("movie_3.html", movie_list=Movie.objects)

#Now deploy to Heroku


#Render template, load data from data base
if __name__ == '__main__':
    app.run()
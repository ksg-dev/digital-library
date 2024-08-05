from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


class Base(DeclarativeBase):
    pass

#
# db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///library.db"

db = SQLAlchemy(app)
# # initialize the app with the extension
# db.init_app(app)


class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True, nullable=False)
    author: Mapped[str] = mapped_column(nullable=False)
    rating: Mapped[float] = mapped_column(nullable=False)


with app.app_context():
    db.create_all()

all_books = []


@app.route('/')
def home():
    return render_template('index.html', library=all_books)


@app.route('/add', methods=["GET", "POST"])
def add():
    if request.method == "POST":
        title = request.form["title"].title()
        author = request.form["author"].title()
        rating = request.form["rating"]
        new_book = {
            "title": title,
            "author": author,
            "rating": rating
        }
        all_books.append(new_book)
        print(all_books)
    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True)


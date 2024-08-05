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


app = Flask(__name__)
app.app_context().push()
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///collection.db"

db = SQLAlchemy(app)
# # initialize the app with the extension
# db.init_app(app)

# Create table
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)




    def __repr__(self):
        return f"<Book {self.title}>"

all_books = []

with app.app_context():
    db.create_all()

# CREATE RECORD
with app.app_context():
    new_book = Book(title="Harry Potter 2", author="J.K. Rowling", rating=9.3)
    db.session.add(new_book)
    db.session.commit()


@app.route('/')
def home():
    return render_template('show_all.html', library=Book.query.all())


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


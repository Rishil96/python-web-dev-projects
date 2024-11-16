import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(os.path.dirname(os.path.abspath(__file__)), 
                                                                  'books-collection.db')}"

# Some code that has to be used to create a DB object to use with Flask
class Base(DeclarativeBase):
    pass


# Create the extension
db = SQLAlchemy(model_class=Base)
# Initialise the app with the extension
db.init_app(app)


# Book model to be used as table in SQLite
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book: {self.title}>'

# Create table schema in the database.
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    # READ ALL RECORDS
    # Construct a query to select from the database. Returns the rows in the database
    result = db.session.execute(db.select(Book).order_by(Book.title))
    # Use .scalars() to get the elements rather than entire rows from the database
    all_books = result.scalars().all()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = Book(title=request.form.get("name"),
                        author=request.form.get("author"),
                        rating=request.form.get("rating"))
        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for("home"))
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)

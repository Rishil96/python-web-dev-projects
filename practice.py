# Higher Lower
from flask import Flask


def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper


def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper


def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper


app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to Home Page!"


@app.route("/users")
@make_bold
@make_emphasis
@make_underlined
def greet():
    return f"Hey Rishil!"


if __name__ == "__main__":
    app.run(debug=True, port=8000)

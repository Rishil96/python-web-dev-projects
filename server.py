# Higher or Lower URLs
import random
from flask import Flask

app = Flask(__name__)
random_number = random.randint(0, 9)


@app.route("/")
def home():
    return ("<h1>Guess the number between 0 to 9</h1>"
            "<img src=\"https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif\">")


@app.route("/<int:num>")
def guess(num: int):
    if num > random_number:
        return ("<h1 style=\"color:purple;\">Too high, try again!</h1>"
                "<img src=\"https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif\">")
    elif num < random_number:
        return ("<h1 style=\"color:red;\">Too low, try again!</h1>"
                "<img src=\"https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif\">")
    else:
        return ("<h1 style=\"color:green;\">You found me!</h1>"
                "<img src=\"https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif\">")


@app.route("/reset")
def reset():
    global random_number
    random_number = random.randint(0, 9)
    return "<h1>Game has been reset!</h1>"


if __name__ == "__main__":
    app.run(debug=True, port=8000)

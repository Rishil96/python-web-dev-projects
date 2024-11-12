import requests
from flask import Flask, render_template

# Load blogs
BLOG_URL = "https://api.npoint.io/99e68aa5bc1aec0bd3eb"
blog_response = requests.get(url=BLOG_URL)
all_blogs = blog_response.json()


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", blogs=all_blogs)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)

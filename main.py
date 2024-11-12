import requests
from flask import Flask, render_template

# Load blogs
BLOG_URL = "https://api.npoint.io/b0ebb78475df0f4c9d31"
blog_response = requests.get(url=BLOG_URL)
all_blogs = blog_response.json()
print(all_blogs)


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


@app.route("/post/<int:pid>")
def post(pid):
    current_post = {}
    for blog in all_blogs:
        if blog["id"] == pid:
            current_post = blog
            break
    return render_template("post.html", post=current_post)


if __name__ == "__main__":
    app.run(debug=True)

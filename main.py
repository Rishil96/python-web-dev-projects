import requests
from flask import Flask, render_template
from post import Post

BLOG_URL = "https://api.npoint.io/c790b4d5cab58020d391"
app = Flask(__name__)

response = requests.get(url=BLOG_URL)
all_posts = response.json()

# Load all posts from API
post_objects = []
for post in all_posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)


@app.route('/')
def home():
    return render_template("index.html", posts=post_objects)


@app.route("/post/<int:pid>")
def show_post(pid):
    requested_post: Post = Post()
    for current_post in post_objects:
        if current_post.pid == pid:
            requested_post = current_post
            break
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)

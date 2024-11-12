import requests
import smtplib
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request

load_dotenv()

# Load blogs
OWN_EMAIL = os.environ.get("USER_EMAIL_ID")
OWN_PASSWORD = os.environ.get("USER_EMAIL_PASSWORD")
BLOG_URL = "https://api.npoint.io/b0ebb78475df0f4c9d31"
blog_response = requests.get(url=BLOG_URL)
all_blogs = blog_response.json()


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", blogs=all_blogs)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


@app.route("/post/<int:pid>")
def post(pid):
    current_post = {}
    for blog in all_blogs:
        if blog["id"] == pid:
            current_post = blog
            break
    return render_template("post.html", post=current_post)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)
        print("Mail sent successfully!")


if __name__ == "__main__":
    app.run(debug=True)

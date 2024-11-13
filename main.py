from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField('Login')


app = Flask(__name__)
app.secret_key = 'my super secret key'.encode('utf8')


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    # Check validations added in our forms when form is submitted
    # validate on submit also acts like a POST request handling as form submit can only be done via POST request
    # in our login template form, the POST method is mentioned
    if login_form.validate_on_submit():
        email = login_form.email.data
        password = login_form.password.data
        print(f"Email: {email}\nPassword: {password}")
        if email == "admin@email.com" and password == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)

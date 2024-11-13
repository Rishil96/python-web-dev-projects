from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


app = Flask(__name__)
app.secret_key = 'my super secret key'.encode('utf8')


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login")
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        return redirect('/home')
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)

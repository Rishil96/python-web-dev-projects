import csv
from datetime import time
from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, TimeField, SelectField
from wtforms.validators import DataRequired

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField(label='Cafe name', validators=[DataRequired()])
    location = URLField(label='Location', validators=[DataRequired()])
    open = TimeField(label='Open', validators=[DataRequired()])
    close = TimeField(label='Close', validators=[DataRequired()])
    coffee = SelectField(label='Coffee',
                         choices=[(1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")],
                         validators=[DataRequired()])
    wifi = SelectField(label='Wifi',
                       choices=[(0, "0"), (1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")],
                       validators=[DataRequired()])
    power = SelectField(label='Power',
                        choices=[(1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")],
                        validators=[DataRequired()])
    submit = SubmitField('Submit')


def get_formatted_time(cafe_time: time):
    output_time = ""
    # Hours
    if cafe_time.hour == 0:
        output_time += "12"
    elif cafe_time.hour < 13:
        output_time += str(cafe_time.hour)
    else:
        output_time += str(cafe_time.hour - 12)
    # Minutes
    if cafe_time.minute != 0:
        output_time += f":{cafe_time.minute}"
    # AM or PM
    if cafe_time.hour >= 12:
        output_time += "PM"
    else:
        output_time += "AM"
    return output_time


COFFEE_EMOJI = "☕️"
WIFI_EMOJI = "💪"
POWER_EMOJI = "🔌"
CROSS_EMOJI = "✘"

# Exercise:
# add: Location URL, open time, closing time, coffee rating, Wi-Fi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        # Make a new entry in Cafe Data
        cafe_name = form.cafe.data
        cafe_location = form.location.data
        # Convert opening and closing time into string
        cafe_open_time = form.open.data
        cafe_open_time = get_formatted_time(cafe_open_time)
        cafe_close_time = form.close.data
        cafe_close_time = get_formatted_time(cafe_close_time)

        cafe_coffee_rating = form.coffee.data
        cafe_coffee_result = ""
        for _ in range(int(cafe_coffee_rating)):
            cafe_coffee_result += COFFEE_EMOJI

        cafe_wifi = form.wifi.data
        cafe_wifi_result = ""
        for _ in range(int(cafe_wifi)):
            cafe_wifi_result += WIFI_EMOJI
        if len(cafe_wifi_result) == 0:
            cafe_wifi_result = CROSS_EMOJI

        cafe_power_rating = form.power.data
        cafe_power_result = ""
        for _ in range(int(cafe_power_rating)):
            cafe_power_result += POWER_EMOJI

        # Make entry in CSV
        new_cafe = [cafe_name, cafe_location, cafe_open_time, cafe_close_time,
                    cafe_coffee_result, cafe_wifi_result, cafe_power_result]
        with open("cafe-data.csv", encoding="utf-8", mode="a", newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(new_cafe)
            print("Row was written successfully")
        return render_template('index.html')

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows[1:])


if __name__ == '__main__':
    app.run(debug=True)

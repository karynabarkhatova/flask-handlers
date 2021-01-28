from flask import Flask
from faker import Faker
import pandas as pd
import requests
import base58


app = Flask(__name__)
fake = Faker()


# Shows the content of requirements.txt

@app.route('/requirements/')
def open_file():
    doc = open(file='requirements.txt')
    output = doc.read()
    return f'<pre>{output}</pre>'


# Generate fake user names and emails

@app.route('/generate-users/<int:XX>')
def generate_users(XX):
    count = 0
    lst = list()
    while XX > count:
        count += 1
        data = fake.first_name() + ' ' + fake.email()
        lst.append(data)
    output = '\n'.join(lst)
    return f'<pre>{output}</pre>'


# Analyzes csv file

@app.route('/mean/')
def analysing_file():

    # open file
    data = pd.read_csv('hw05.csv', encoding='utf-8', delimiter=',')

    # put columns into variables
    height_values = data[' "Height(Inches)"']
    weight_values = data[' "Weight(Pounds)"']

    # find the amount of the strings
    index = data.index
    number_of_rows = len(index)

    # find an average height and convert it from inches to cm
    avrg_height = sum(height_values) / number_of_rows
    avrg_height_cm = round(avrg_height * 2.54)

    # find an average weight and convert it from pounds to kg
    avrg_weight = sum(weight_values) / number_of_rows
    avrg_weight_kg = round(avrg_weight * 0.453592)

    return f'<pre>Parsed file: "hw05.cvs" \nTotal values in file: {number_of_rows}\nAverage height: {avrg_height_cm} cm \nAverage weight: {avrg_weight_kg} kg</pre>'


# Shows the amount of people in the space

@app.route('/space/')
def spacemen_in_space():
    r = requests.get('http://api.open-notify.org/astros.json')

    return f'Amount of spacemen and spacewomen in the space right now: {r.json()["number"]}'


# Encode the input string

@app.route('/base58encode/<STRING>')
def base58_encode(STRING):
    encoded_str = base58.b58encode(STRING)
    return encoded_str


# Decode the input string encoded by base58

@app.route('/base58decode/<STRING_IN_BASE58>')
def base58_decode(STRING_IN_BASE58):
    decoded_str = base58.b58decode(STRING_IN_BASE58)
    return decoded_str


app.run()

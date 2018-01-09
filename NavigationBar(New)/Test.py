from flask import Flask, render_template
from wtforms import Form, StringField, validators
import Main

import TopUpUsers

app = Flask(__name__)


class topupUser(Form):
    firstname = StringField('Firstname', [validators.Length(min=1, max=150), validators.DataRequired()])
    lastname = StringField('Lastname', [validators.Length(min=1, max=150), validators.DataRequired()])
    age = StringField('Age', [validators.Length(min=1, max=150), validators.DataRequired()])


@app.route('/topup')
def TopUp():
    currentAmount = 0
    totalAmount = 0
    ll =[]
    ll = Main.processTopup('9 Feb 2017', 'Tom', 7)
    return render_template('TopUp.html', tt=ll)

@app.route('/layout')
def layout():
    return render_template('layout.html')

@app.route('/layout1')
def layout1():
    return render_template('layout1.html')


if __name__ == '__main__':
    app.run()

from random import choice

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    choice = True
    return render_template('index.html', title="Home", name='Aminjon',text="Do you interested in programming???", choice= choice)

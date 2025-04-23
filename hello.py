from random import choice

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    choice = True
    cs_professions = ["AI and ML", "Software Engineer", "Web Developer"]
    return render_template('index.html', title="Home", name='Aminjon',text="Are you interested in programming???", choice= choice, cs_professions= cs_professions)

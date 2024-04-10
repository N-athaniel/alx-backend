#!/usr/bin/env python3
'''a single / route that simply outputs “Welcome to Holberton” as page
'''

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    '''default route'''
    return render_template("0-index.html",)


if __name__ == "__main__":
    app.run(debug=True)

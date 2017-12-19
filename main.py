# -*- coding: utf-8 -*-

try:
    from os import getuid

except ImportError:
    def getuid():
        return 4000

from flask import Flask, request, render_template, Response, json

import sys
import os

app = Flask(__name__)


@app.route('/')
def get_index():
    return render_template('index.html')


@app.route('/faq')
def get_faq():
    return render_template('faq.html')


@app.route('/download')
def get_download():
    return render_template('download.html')


@app.route('/parser')
def get_parser():
    return render_template('parser.html')


"""@app.route('/predict/', methods=['GET', 'POST'])
def predict():
    text = request.get_data().decode('utf-8')
    text = text.replace("́", "")
    accented_text = accent.put_stress(text, "́")
    return accented_text"""


if __name__ == '__main__':
    app.run(debug=True)

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
    return render_template('starter.html')


@app.route('/faq')
def get_faq():
    return render_template('faq.html')


@app.route('/download')
def get_download():
    return render_template('download.html')


@app.route('/parser')
def get_parser():
    return render_template('parser.html')


@app.route('/pred/', methods=['GET', 'POST'])
def predict():
    text, model_name = request.get_data().decode('utf-8').split('///')
    response = text + ' ' + model_name + ' ' + '501 good'
    return response


if __name__ == '__main__':
    app.run(debug=True)

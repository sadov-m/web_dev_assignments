# -*- coding: utf-8 -*-

from flask import Flask, request, render_template, Response, json, \
    redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
import time
import warnings
#from ANAPHORA.RUN.anparser.run import AnaphoraParser
#from ANAPHORA.RUN.anparser.features import *
#from gensim.models import KeyedVectors
import os

UPLOAD_FOLDER = os.getcwd() + '/temp'
ALLOWED_EXTENSIONS = {'txt'}

app = Flask(__name__)
warnings.filterwarnings("ignore")
#ap = AnaphoraParser()
#ap.load_model('anparser/Models/model_3_0539.pkl')
#print('parser loaded')
#w2v_model = KeyedVectors.load_word2vec_format(os.getcwd() + '/anparser/araneum_1_600_2.bin', binary=True)
#print('w2v loaded')
app.secret_key = 'parser_anaphora'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#TEMP_FILE = os.getcwd() + '/temp/temp_text' + str(time.time()).replace('.', '_') + '.txt'


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


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


@app.route('/upload', methods=['POST', 'GET'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            print(request.files)
            print('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            print('No selected file')
            return redirect(request.url)
        print(file.filename)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            filetext = open('temp/' + filename, encoding='utf-8').read()
            newfilename = 'parsed_' + str(time.time()).replace('.', '') + '.txt'
            with open('temp/' + newfilename, 'w', encoding='utf-8') as a_file:
                a_file.write(filetext)
            return redirect(url_for('uploaded_file',
                                    filename=newfilename))
    return render_template('parser.html')


@app.route('/temp/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

@app.route('/pred/', methods=['GET', 'POST'])
def predict():
    text, model_name = request.get_data().decode('utf-8').split('///')
    filename = str(time.time()).replace('.', '') + '.txt'
    x = open('temp/' + filename, 'w', encoding='utf-8')
    x.write(text)
    x.close()
    response = text + ' ' + '<span style="background-color: #82E0AA">{}</span>'.format(model_name) + ' ' + '501 good'
    return response


if __name__ == '__main__':
    app.run(debug=True)

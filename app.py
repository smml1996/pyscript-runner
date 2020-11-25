from flask import Flask, jsonify
from flask import render_template, request
from forms import ScriptUploadForm
import tempfile

import random
import string
import subprocess
import os
from os.path import join, dirname, realpath

app = Flask(__name__)
UPLOAD_FOLDER = join(dirname(realpath(__file__)), 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "ponis"
ALLOWED_EXTENSIONS = {'py'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


@app.route('/', methods=['GET'])
def index():
    form = ScriptUploadForm()
    return render_template('index.html', form=form)


@app.route('/result')
def result():
    return render_template('result.html', output=request.args.get('output'), error=request.args.get('error'))


@app.route('/lint', methods=['POST'])
def lint_action():
    file = tempfile.NamedTemporaryFile(delete=False, mode='w')
    file.write(request.form['code'])
    file.close()
    command = "python " + file.name
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    os.remove(file.name)
    return jsonify({'output': output.decode('utf-8'), 'error': error.decode('utf-8')})


if __name__ == '__main__':
    app.run(host='0.0.0.0')


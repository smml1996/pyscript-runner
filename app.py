from flask import Flask
from flask import render_template, request, redirect, url_for
from forms import ScriptUploadForm
from werkzeug.utils import secure_filename

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


@app.route('/', methods=['GET', 'POST'])
def index():
    form = ScriptUploadForm()
    if request.method == 'POST' and form.validate_on_submit():
        file = request.files['archivo']
        if file and allowed_file(file.filename):
            filename = get_random_string(10) + ".py"
            #filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            command = "python " + app.config['UPLOAD_FOLDER'] + "/" + filename
            process = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = process.communicate()
            return redirect(url_for('result', output=output, error=error))
    return render_template('index.html', form=form)


@app.route('/result')
def result():
    return render_template('result.html', output=request.args.get('output'), error=request.args.get('error'))


if __name__ == '__main__':
    app.run(host='0.0.0.0')


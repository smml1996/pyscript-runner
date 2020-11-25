from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired


class ScriptUploadForm(FlaskForm):
    """ Form for Uploading a python script """
    archivo = TextAreaField('Py-script', validators=[DataRequired()])
    submit = SubmitField('<i class="fas fa-play"></i>')
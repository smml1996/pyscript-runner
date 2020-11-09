from flask_wtf import FlaskForm
from wtforms import SubmitField, FileField
from wtforms.validators import DataRequired


class ScriptUploadForm(FlaskForm):
    """ Form for Uploading a python script """
    archivo = FileField('Py-script', validators=[DataRequired()])
    submit = SubmitField('Aceptar')
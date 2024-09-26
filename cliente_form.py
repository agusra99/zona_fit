from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.numeric import IntegerField
from wtforms.fields.simple import SubmitField, HiddenField
from wtforms.validators import DataRequired


class ClienteForm(FlaskForm):
    id=HiddenField('id')
    nombre=StringField('Nombre',validators=[DataRequired()])
    apellido=StringField('Apellido',validators=[DataRequired()])
    membresia=IntegerField('Membresia',validators=[DataRequired()])
    guardar=SubmitField('Guardar')
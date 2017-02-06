from flask_wtf import Form
from wtforms import StringField, SubmitField, IntegerField, PasswordField
from wtforms.validators import InputRequired, Length, Email

class NewForm(Form):
    company = StringField('Empresa', validators=[InputRequired('Campo Empresa Obligatorio'),
                                               Length(1, 20, 'Texto inferior a 20 caracteres')])
    role = StringField('Puesto', validators=[InputRequired('Campo Puesto Obligatorio'),
                                             Length(1, 20, 'Texto inferior a 20 caracteres')])
    start = IntegerField('Inicio', validators=[InputRequired('Campo Inicio Obligatorio')])
    end = IntegerField('Finalización', validators=[InputRequired('Campo Fin Obligatorio')])
    submit = SubmitField('Add')

class EditForm(Form):
    company = StringField('Empresa', validators=[InputRequired('Campo Empresa Obligatorio'),
                                                 Length(1, 20, 'Texto inferior a 20 caracteres')])
    role = StringField('Puesto', validators=[InputRequired('Campo Puesto Obligatorio'),
                                             Length(1, 20, 'Texto inferior a 20 caracteres')])
    start = IntegerField('Inicio', validators=[InputRequired('Campo Inicio Obligatorio')])
    end = IntegerField('Finalización', validators=[InputRequired('Campo Fin Obligatorio')])
    submit = SubmitField('Editar')

class UserForm(Form):
    name = StringField('Nombre', validators=[InputRequired('Campo Nombre Obligatorio'),
                                                 Length(1, 100, 'Texto inferior a 100 caracteres')])
    email = StringField('Email', validators=[InputRequired('Campo Email Obligatorio'),
                                             Length(1, 100, 'Texto inferior a 100 caracteres'),
                                              Email('Correo incorrecto')])
    password = PasswordField('Contraseña', validators=[InputRequired('Por favor, escribe una contraseña')])
    submit = SubmitField('Login')
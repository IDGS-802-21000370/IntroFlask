from wtforms import Form
from wtforms import StringField, TextAreaField, SelectField, RadioField, TextField
from wtforms import EmailField

class UserForm(Form):
    nombre = StringField("nombre")
    email = EmailField("correo")
    apaterno = TextField("apaterno")
    materias = SelectField(choises=[('Español', 'Esp'), ('Mat', 'Matematicas'), ('Ingles', 'Ing')])
    radios = RadioField('Curso', choices=[("1", "1"), ("2", "2"), ("3", "3")])
    
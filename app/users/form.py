from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired

class UpdateImageProfileForm(FlaskForm):
    """ Form para actualizar la foto de perfil del usuario. """
    upload = FileField("Imagen de perfil", validators=[
        FileRequired(),
        FileAllowed(['jpg', 'jpge', 'png'], "Solo imagenes ('jpg', 'jpge', 'png')")
    ])

# -*- Coding: utf-8 -*-
from os import path, remove
import datetime

def get_dict_from_wftform(form):
    """ Método para obtener un diccionario a partir de un formulario de wtf forms. """
    dictionary = dict()
    try:
        for key in form.data.keys():
            if key in ['csrf_token', 'submit']:
                continue
            dictionary[str(key)] = form[key].data
    except AttributeError as error:
        dictionary = dict()
    finally:
        return dictionary

def path_url_exists(path_url):
    """ Método de verificación de ruta. """
    if path.exists(path_url):
        return True
    return False

def remove_pictute_profile(profile_name):
    """ Método para eliminar foto de perfil del usuario. """
    path_url = "app/uploads/profile_pictures/" + profile_name
    if path_url_exists(path_url):
        remove(path_url)

def random_name(name_base):
    """ Método para generar un nombre aleatorio. """
    suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
    filename = "_".join([name_base, suffix])
    return filename
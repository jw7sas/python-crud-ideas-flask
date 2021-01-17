from .database import *
from .serializer import *
from .utils import remove_pictute_profile

def get_user_by_username(username):
    """ Método para retornar el usuario a partir del username. """
    return User.query.filter_by(username=username).first()

def register_user(user_data):
    """ Método para registrar un usuario nuevo en la base de datos. """
    user = User(
        name=user_data['name'],
        lastName=user_data['lastName'],
        username=user_data['username'],
        email=user_data['email'],
        password=user_data['password'],
        cellphone=user_data['cellphone'],
    )
    user.set_password(user_data['password'])

    db.session.add(user)
    db.session.commit()

def get_Category_by_id(category_id):
    """ Método para busar categoria por id. """
    return Category.query.get(category_id)

def delete_category(category_id):
    category = get_Category_by_id(category_id)

    db.session.delete(category)
    db.session.commit()

def create_category(name):
    """ Método para crear una categoría. """
    category = Category(name=name)

    db.session.add(category)
    db.session.commit()

def list_categories():
    """ Método para obtener el listado de categorias. """
    schema = CategorySchema()
    data = Category.query.all()
    categories = [schema.dump(c) for c in data]

    return categories

def get_idea_by_id(idea_id):
    """ Método para obtener idea por id. """
    return Idea.query.get(idea_id)

def create_idea(idea_data):
    """ Método para crear una idea en la db. """
    user = get_user_by_username(
        idea_data['username']
    )

    category = get_Category_by_id(
        idea_data['category_id']
    )

    idea = Idea(
        title=idea_data["title"],
        description=idea_data["description"],
        is_public=idea_data["is_public"],
        category=category,
        user=user,
    )

    db.session.add(idea)
    db.session.commit()

def list_ideas_by_username(username):
    """ Método para listar ideas por nombre de usuario. """
    user = get_user_by_username(username)
    schema = IdeaSchema()
    data = Idea.query.filter_by(user=user)
    ideas = [schema.dump(i) for i in data]
    
    return ideas


def delete_idea_db(idea_id):
    """ Método para eliminar una idea. """
    idea = get_idea_by_id(idea_id)

    db.session.delete(idea)
    db.session.commit()

def update_state_idea_db(idea_id, state):
    """ Método apta cambiar el estado de la idea. """
    idea = get_idea_by_id(idea_id)
    idea.is_public = not bool(state)

    db.session.commit()

def update_idea_db(idea_data):
    """ Método para actualizar una idea. """
    category = get_Category_by_id(
    idea_data['category_id']
    )
    idea = get_idea_by_id(idea_data['id'])

    idea.title = idea_data["title"]
    idea.description = idea_data["description"]
    idea.is_public = idea_data["is_public"]
    idea.category = category

    db.session.commit()

def update_profile_picture(username, picture_name_new):
    """ Método para actualizar la foto de perfil del usuario. """
    user = get_user_by_username(
        username
    )
    if user.avatar is not None:
        remove_pictute_profile(user.avatar)
    
    user.avatar = picture_name_new

    db.session.commit()


def list_public_ideas():
    """ Método para obtener listado de ideas publicas, """
    data = Idea.query.filter_by(is_public=True).order_by(Idea.category_id)
    schema = IdeaSchema()
    public_ideas = [schema.dump(i) for i in data]

    return public_ideas
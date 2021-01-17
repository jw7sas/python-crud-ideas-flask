from .database import *

def create_db():
    """ Método de creación de la base de datos. """
    db.drop_all()
    db.create_all()

def init_db():
    """ Método de inicialización de nuestra base de datos. """
    create_db()
    # user admin app
    admin = User(
        name="Jose",
        lastName="Saavedra",
        username="jrsaavedra",
        email="jw7sas@gmail.com",
        is_admin=True,
        cellphone="743875847788",
    )
    admin.set_password("123Admin")
    db.session.add(admin)
    db.session.commit()
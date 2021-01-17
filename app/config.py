class Config:
    """ Clase de configuración de flask. """
    SECRET_KEY = 'ideas secreatas de youtube'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../ideas.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
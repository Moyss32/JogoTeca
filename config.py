from urllib.parse import quote_plus
import os

SECRET_KEY = 'AAAbbb123!@#'

senha = quote_plus('b4t3r14PEARL!@')

SQLALCHEMY_DATABASE_URI = \
    f"mysql+mysqlconnector://root:{senha}@127.0.0.1:3306/jogoteca"


UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'
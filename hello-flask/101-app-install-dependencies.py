from flask import Flask

from flask_sqlalchemy import SQLAlchemy
# este módulo es un ORM(Objet relacional-mappers). Permite hacer consultas a 
# bases de datos sin tener que programarlas en SQL

from flask_marshmallow import Marshmallow
# allows us to render JSON API and to have some very helpful tools
# for being able to wrap the code

# Marshmallow-SQLAlchemy es otro módulo que nos permite comunicar 
# los otros dos de manera sencilla.   

import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hey Flask"


if __name__ == '__main__':
    app.run(debug=True)

# Para terminar el programa es necesario teclear ctrl C en la terminal
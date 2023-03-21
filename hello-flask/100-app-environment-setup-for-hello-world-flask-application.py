# from os import system
# system('cls')

from flask import Flask

app = Flask(__name__)  #abrimos una instacia de Flask

@app.route('/') # creamos un decorator estableciendo la ruta base.

def hello():
    return "Hey Flask"


if __name__ == '__main__':
    app.run(debug=True)
    



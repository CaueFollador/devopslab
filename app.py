from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Hello world doesn't make you a great dev. Change my mind"

if __name__ == '__main__':
    app.run()
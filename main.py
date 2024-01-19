from flask import flask

app=Flak(__name__)

@app.route("/")
def hola():
    return "<p> Hola Mundo <p>"


if __name__ == "__main__":
    app.run()
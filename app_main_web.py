from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return"<H1>Hello World!,</H1>"

@app.route("/login")
def hello_2():
    return "<h2>Login - Inny tekst</h2>"


if __name__ == '__main__':
    app.run(debug=True)
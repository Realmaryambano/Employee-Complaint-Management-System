from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def login():
    return render_template("login.html")


@app.route("/it-support")
def it_support():
    return render_template("it_support.html")


if __name__ == "__main__":
    app.run(debug=True)
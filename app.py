from flask import (
    Flask,
    render_template,
    send_from_directory,
    jsonify,
    redirect,
    request,
    session,
    make_response,
    abort,
)

app = Flask(__name__)

@app.route("/")
def index():
    return "Hey there!"

@app.route("/main")
def main():
    return render_template("index.html")
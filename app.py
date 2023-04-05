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
from db_helper import DatabaseActions

app = Flask(__name__)

@app.route("/")
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/experience")
def experience():
    return render_template("experience.html")

@app.route("/send_message", methods=['POST'])
def send_message():
    if request.method == 'POST':
        requestor_name = request.form['Name']
        requestor_email = request.form['Email']
        requestor_subject = request.form['Subject']
        requestor_message = request.form['Message']
        db_action_obj = DatabaseActions('arsalan_site_db.db')
        requestor_message = (requestor_email, requestor_name, requestor_subject, requestor_message)
        db_action_obj.add_message(requestor_message)
        return render_template("dashboard.html")
    else:
        return render_template("dashboard.html")

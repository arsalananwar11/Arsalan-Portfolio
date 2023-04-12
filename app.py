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

ENV = 'prod' # development or production

@app.route("/")
@app.route("/dashboard")
def dashboard():
    db_action_obj = DatabaseActions('arsalan_site_db.db', ENV)
    featured_projects_list = db_action_obj.fetch_featured_projects()
    db_action_obj.close_db_connection()
    return render_template("dashboard.html", featured_projects_list = featured_projects_list)


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
        db_action_obj = DatabaseActions('arsalan_site_db.db', ENV)
        requestor_message = (requestor_email, requestor_name, requestor_subject, requestor_message)
        db_action_obj.add_message(requestor_message)
        db_action_obj.close_db_connection()

        # TBD: Send success op response
        return redirect("/dashboard")
    else:
        # TBD: Send error op response
        return redirect("/dashboard")

@app.route("/projects")
def projects():
    db_action_obj = DatabaseActions('arsalan_site_db.db', ENV)
    all_projects_list = db_action_obj.fetch_all_projects()
    db_action_obj.close_db_connection()

    return render_template("projects.html", all_projects_list = all_projects_list)

@app.route("/project/<project_id>", methods=['GET'])
def project(project_id):
    db_action_obj = DatabaseActions('arsalan_site_db.db', ENV)
    requested_project = db_action_obj.fetch_requested_project(project_id)
    db_action_obj.close_db_connection()

    return render_template("project_dashboard.html", project = requested_project, access = ENV)

@app.route('/save_project_description', methods=['POST'])
def save_project_description():
    if request.method == 'POST':
        project_details = request.get_json()
        project_id = project_details['project_id']
        project_description = project_details['project_description']
        db_action_obj = DatabaseActions('arsalan_site_db.db', ENV)
        project_update_status = db_action_obj.update_project_description(project_id, project_description)
        db_action_obj.close_db_connection()

        if(project_update_status):
            return jsonify(project_description)
        else:
            error_message = 'Some error occured while updating the project description. Please refresh.'
            return jsonify(error_message)
        
    return render_template("dashboard.html")
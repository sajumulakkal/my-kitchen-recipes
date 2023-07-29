

import os
import random
import string
from datetime import datetime
import ssl

from flask import Blueprint, render_template, redirect, url_for, session, request
from flask_dance.contrib.google import make_google_blueprint, google
from flask_dance.contrib.facebook import make_facebook_blueprint, facebook
from flask_dance.contrib.linkedin import make_linkedin_blueprint, linkedin
from firebase_admin import credentials, firestore, auth, initialize_app

chemlab_blueprint = Blueprint('chemlab', __name__)
chemlab_blueprint.secret_key = "your_secret_key"


google_client_id = os.environ['GOOGLE_CLIENT_ID']
google_client_secret = os.environ['GOOGLE_CLIENT_SECRET']

facebook_client_id = os.environ['FACEBOOK_CLIENT_ID']
facebook_client_secret = os.environ['FACEBOOK_CLIENT_SECRET']

linkedin_client_id = os.environ['LINKEDIN_CLIENT_ID']
linkedin_client_secret = os.environ['LINKEDIN_CLIENT_SECRET']

firebase_credentials = {
    "type": "service_account",
    "project_id": os.environ.get('FIREBASE_PROJECT_ID'),
    "private_key_id": os.environ.get('PRIVATE_KEY_ID'),
    "private_key": os.environ.get('FIREBASE_PRIVATE_KEY').replace('\\n', '\n'),
    "client_email": os.environ.get('FIREBASE_CLIENT_EMAIL'),
    "client_id": os.environ.get('CLIENT_ID'),
    "auth_uri": os.environ.get('AUTH_URI'),
    "token_uri": os.environ.get('TOKEN_URI'),
    "auth_provider_x509_cert_url": os.environ.get('AUTH_PROVIDER_X509_CERT_URL'),
    "client_x509_cert_url": os.environ.get('CLIENT_X509_CERT_URL')
}

initialize_app(credentials.Certificate(firebase_credentials))

db = firestore.client()

google_blueprint = make_google_blueprint(
    client_id=google_client_id,
    client_secret=google_client_secret,
    scope=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email",
           "openid"],
    redirect_to="google_callback"
)
chemlab_blueprint.register_blueprint(google_blueprint, url_prefix="/login")

facebook_blueprint = make_facebook_blueprint(
    client_id=facebook_client_id,
    client_secret=facebook_client_secret,
    scope="email",
    redirect_to="facebook_callback"
)
chemlab_blueprint.register_blueprint(facebook_blueprint, url_prefix="/login")

linkedin_blueprint = make_linkedin_blueprint(
    client_id=linkedin_client_id,
    client_secret=linkedin_client_secret,
    scope=["r_emailaddress"],
    redirect_to="linkedin_callback"
)
chemlab_blueprint.register_blueprint(linkedin_blueprint, url_prefix="/login")


def load_users():
    users_ref = db.collection('users')
    users = {}
    docs = users_ref.get()
    for doc in docs:
        user_data = doc.to_dict()
        users[user_data['email']] = user_data
    return users


def validate_password(email, password):
    users = load_users()
    if email in users and users[email]["password"] == password:
        return True
    return False


def is_user_logged_in():
    return "user" in session


def get_questions():
    questions = []
    collection_ref = db.collection("questions_and_answers")
    query = collection_ref.order_by("question").select(["question"])

    for doc in query.stream():
        question = doc.to_dict()["question"]
        questions.append(question)

    return questions


def get_answers():
    answers = []
    collection_ref = db.collection("questions_and_answers")
    query = collection_ref.order_by("question").select(["answer"])

    for doc in query.stream():
        answer = doc.to_dict()["answer"]
        answers.append(answer)

    return answers


@chemlab_blueprint.route("/")
def index():
    if not is_user_logged_in():
        return redirect(url_for("chemlab.login"))

    questions = get_questions()
    answers = get_answers()
    zipped_questions = zip(questions, answers)

    return render_template("index.html", questions=zipped_questions)


@chemlab_blueprint.route("/login", methods=["GET", "POST"])
def login():
    if is_user_logged_in():
        # If the user is already logged in, redirect to the index page
        return redirect(url_for("chemlab.index"))

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        users_ref = db.collection("users")
        query = users_ref.where("email", "==", email).limit(1)
        users = query.get()

        if len(users) == 1:
            user_data = users[0].to_dict()
            stored_password = user_data["password"]
            if stored_password == password:
                session["user"] = email
                session["login_via"] = "email"
                # After successful login, redirect to the index page
                return redirect(url_for("chemlab.index"))

        error = "Invalid email or password"
        return render_template("login.html", error=error)

    # Instead of redirecting, just render the login template
    return render_template("login.html")






def save_user_answer_audit(user_email, answers):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    closing_key = generate_closing_key()
    login_via = session.get("login_via")

    record = {
        "timestamp": timestamp,
        "user_email": user_email,
        "answers": answers,
        "closing_key": closing_key,
        "login_via": login_via
    }
    audit_ref = db.collection("user_answer_audit")
    audit_ref.add(record)


def generate_closing_key():
    letters_and_digits = string.ascii_letters + string.digits
    closing_key = ''.join(random.choice(letters_and_digits) for _ in range(10))
    return closing_key


@chemlab_blueprint.route("/submit", methods=["POST"])
def submit():
    if not is_user_logged_in():
        return redirect(url_for("chemlab.login"))

    answers = []
    for i in range(1, 10):
        answer = request.form.get(f"q{i}")
        answers.append(answer)

    save_user_answer_audit(session["user"], answers)

    return redirect(url_for("chemlab.index"))


@chemlab_blueprint.route("/logout", methods=["GET", "POST"])
def logout():
    session.clear()
    return redirect(url_for("chemlab.login"))


@chemlab_blueprint.route("/google-login")
def google_login():
    if not google.authorized:
        return redirect(url_for("chemlab.google.login"))
    return redirect(url_for("chemlab.index"))


@chemlab_blueprint.route("/signup", methods=["GET", "POST"])
def signup():
    if is_user_logged_in():
        return redirect(url_for("chemlab.index"))

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        date_of_birth = request.form.get("date_of_birth")
        country = request.form.get("country")

        users_ref = db.collection("users")
        user_data = {
            "email": email,
            "password": password,
            "first_name": first_name,
            "last_name": last_name,
            "date_of_birth": date_of_birth,
            "country": country
        }
        users_ref.document(email).set(user_data)

        session["user"] = email
        return redirect(url_for("chemlab.index"))

    return render_template("signup.html")


@chemlab_blueprint.route("/google-login/callback")
def google_callback():
    if not google.authorized:
        return redirect(url_for("chemlab.google.login"))
    resp = google.get("/oauth2/v1/userinfo")
    session["user"] = resp.json()["email"]
    session["login_via"] = "google"
    return redirect(url_for("chemlab.index"))


@chemlab_blueprint.route("/facebook-login")
def facebook_login():
    if not facebook.authorized:
        return redirect(url_for("chemlab.facebook.login"))
    return redirect(url_for("chemlab.index"))


@chemlab_blueprint.route("/facebook-login/callback")
def facebook_callback():
    if not facebook.authorized:
        return redirect(url_for("chemlab.facebook.login"))
    user_info = facebook.get("/me?fields=email")
    session["user"] = user_info.json().get("email")
    session["login_via"] = "facebook"
    return redirect(url_for("chemlab.index"))


@chemlab_blueprint.route("/linkedin-login")
def linkedin_login():
    if not linkedin.authorized:
        return redirect(url_for("chemlab.linkedin.login"))
    return redirect(url_for("chemlab.index"))


@chemlab_blueprint.route("/linkedin-login/callback")
def linkedin_callback():
    if not linkedin.authorized:
        return redirect(url_for("chemlab.linkedin.login"))

    resp = linkedin.get("/v2/emailAddress?q=members&projection=(elements*(handle~))")
    if resp.ok:
        user_data = resp.json()
        email_address = user_data.get("emailAddress")
        session["user"] = email_address if email_address else "linkedin"
        session["login_via"] = "linkedin"
    else:
        return "Failed to retrieve user data from LinkedIn."

    return redirect(url_for("chemlab.index"))


@chemlab_blueprint.route("/save_user_key", methods=["POST"])
def save_user_key():
    if not is_user_logged_in():
        return redirect(url_for("chemlab.login"))

    user_email = session["user"]
    closing_key = request.json.get("closing_key")
    login_via = session.get("login_via")

    user_key_ref = db.collection("user_key")

    key_data = {
        "timestamp": firestore.SERVER_TIMESTAMP,
        "user_email": user_email,
        "closing_key": closing_key,
        "login_via": login_via
    }

    user_key_ref.add(key_data)

    return "User Key saved successfully"


@chemlab_blueprint.route("/save_user_answers", methods=["POST"])
def save_user_answers():
    if not is_user_logged_in():
        return redirect(url_for("chemlab.login"))

    user_email = session["user"]
    login_via = session.get("login_via")

    answers = request.json.get("answers")
    audit_ref = db.collection("user_answer_audit")

    doc_data = {
        "timestamp": firestore.SERVER_TIMESTAMP,
        "user_email": user_email,
        "answers": answers,
        "login_via": login_via
    }

    audit_ref.add(doc_data)
    return "User answers saved successfully"



if __name__ == "__main__":
    load_users()

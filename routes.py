import googlemaps
import geojsonio
from flask import Flask, render_template, redirect, request, flash, session
from app import db
from app.main import bp
from SQLAlchemy.sql import func, exists
from model import User, Rating, BubbleTeaStore, connect_to_db, db

dp = Flask(_name_)
dp.secret_key = "boba"

def get_state(session):
    return {
        'logIn': bool(session.get('log_in_user')),
    }

@dp.route('/')
def index():
    return render_template("Home.html")

@dp.route("/view_users")
def find_BubbleTeaStores():
    query=request.args.get("query")
    location=request.args.get("location")
    return render_template("bubbletea_map.html")

@dp.route("/about-bubbletea")
def generate_about_tea():
    url = "https://www.googleapis.com/geolocation/v1/geolocate?key=" + GOOGLE_PLACES_KEY
    response=requests.get(url,payload)
    print(response)
    data = response.json()
    bubbleteastores=[]
    return render_template("about.html", data=pformat(data), results=bubbleteastores)

@dp.route("/register", methods = ["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("registration_form.html")
    email = request.form.get("email")
    password = request.form.get("password")

    if User.query.filter(User.email == email).first():
        flash("This email is already in use!")
        return render_template("registration_form.html")
    user = User(email=email, password=password)
    db.session.add(user)
    db.session.commit()

    session["log_in_user"] = user.user_id
    flash("You have sucessfully created an account")
    return redirect("/view_users")

@dp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    else:
        email = request.form.get("email")
        password = request.form.get("password")

        q=User.query
        if q.flter((User.email == email), (User.password == password).first():
            session["log_in_user"] =q.filter(User.email == email).one().user_id
            flash("Logged In!")
            return redirect("/view_users")
        else:
            flash("The email or password is wrong.")
            return render_template("login.html")

@dp.route("/logout")
def logout():
    print("Checking", session.get("log_in_user"))
    del session["log_in_user"]
    flash("You are successfully logged out!")
    return redirect("/")

@dp.route("/bubble-tea-store-ratings/<name>/<store_id>/<address>", methods=["GET", "POST"])
def ratings(name, store_id, address):
    print(session)
    new_score = (request.form.get("input_rating"))
    print('score: ', new_score)

    if not session.get("log_in_user"):
        flash("You are not logged into an account!")
        return redirect("/")

    user_id = session["log_in_user"]
    bubble_tea_store = BubbleTeaStore.query.filter(BubbleTeaStore.store_id==store_id).first()

    if request.method == "GET:
        average_rate = (db.session.query(func.average(rating.number)).filter(rating.bubble_tea_store_id = bubble_tea_store.store_id).scalar())
        return render_template("rating_store.html", name=name, store_id=store_id, address=address, average_rate=f"{average_rate:0.1f}", state=get_state(session),)
    else:
        rating = Rating.query.filter(rating.user_id=user_id, rating.bubble_tea_store_id=bubble_tea_store.store_id).first()
        print("Existing Score: ", rating)
        print("Bubble Tea Store: ", bubble_tea_store)

        if rating:
            rating.score = new_score
            flash("Your Score has been updated. Thank You!")
        else:
            rating = Rating(bubble_tea_store_id=bubble_tea_store.store_id, user_id=user_id, score=new_score)
            flash("Yay!")
        db.session.add(rating)
        db.session.commit()
        return redirect("/view-users")

if _name_ == "_main_":
    dp.debug = True
    connect_to_db(app)

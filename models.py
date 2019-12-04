from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class BubbleTeaStore(db.Model):
    _tablename_ = "BubbleTeaStores"

    store_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    ratings = db.Column(db.Integer)

class User(db.Model):
    _tablename_ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(100), nullable=True)
    name = db.Column(db.String(100), nullable=True)
    password = db.Column(db.String(50), nullable=True)
    age = db.Column(db.Integer, nullable=True)

class Ratings(db.Model):
    _tablename_ = "ratings"

    rating_number = db.Column(db.Integer, autoincrement=True, primary_key=True)
    bubble_tea_store_id = db.Column(db.Integer, db.ForeignKey('bubbleteastores.store_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    score = db.Column(db.Integer)
    user = db.relationship("User", backref=db.backref("ratings", order_by=rating_number))
    bubble_tea_store = db.relationship("BubbleTeaStore", backref=db.backref("ratings", order_by=rating_number))

def connect_to_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///ratings'
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
	db.app = app
	db.init_app(app)

if _name_ == "_main_":
    from server import app
    connect_to_db(app)
    print("Connected to DB.")

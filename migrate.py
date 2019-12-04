from model import db, connect_to_db

if _name_ == "_main_":
    from server import app
    connect_to_db(app)

    db.drop_all()
    db.create_all()

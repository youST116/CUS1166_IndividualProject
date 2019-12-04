from sqlalchemy import func
from model import (BubbleTeaStore)
from model import connect_to_db, db
from server import app
from datetime import datetime

def load_bubble_tea_stores():
    print(BubbleTeaStores)
    BubbleTeaStores.query.delete()
    for row in open("seed_data/bubble_tea_store.txt")
    row = row.strip()
    store_id,name, address, latitude, longitute, bubble_tea_store_id = row.split("|")
    name = name.rstrip()
    bubble_tea_store=BubbleTeaStore(store_id=store_id, name=name, address=address, latitude=latitude, longitude=longitude)
    db.session.add(bubble_tea_store)
    db.session.commit()
def set_value_bubble_tea_store_id():
    result = db.session.query(func.max(BubbleTeaStore.store_id)).one()
    max_id = int(result[0])

    query = "Select setValue(bubbleteastores_store_id_seq', :new_id)"
    db.session.execute(query, {'new_id':max_id+1})
    db.session.commit()

if _name_ == "_main_":
    connect_to_db(app)
    db.create_all()
    load_bubble_tea_stores()
    set_value_bubble_tea_store_id()

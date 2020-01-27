from flask import current_app, g
import sqlite3
import os

DATABASE= '../myDB.db'

def get_db():
    db= sqlite3.connect(DATABASE, check_same_thread=False)
    db.row_factory = sqlite3.Row
    return db


def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    db = get_db()
    with open (os.getcwd()+'/models/schema.sql') as f:
        file = f.read()
        db.executescript(file)

def insert_bid(petID, userID , money):
    db = get_db()
    db_cursor=db.cursor()
    db_cursor.execute('insert into BIDS (petID,userID,money) values (?,?,?)',(petID,userID,money) )
    db.commit()
    db.close()

def get_bids():
    db=get_db()
    rows= db.cursor().execute('SELECT * FROM BIDS')
    return_rows=[]
    for row in rows:
        dictionary = {
            'petID': row['petID'],
            'userID': row['userID'],
            'money': row['money']
        }
        return_rows.append(dictionary)
    db.close()
    return return_rows
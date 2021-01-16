# Fernando Jose Lavarreda Urizar
# Basic DataBase Manipulation

import math
import pyperclip
import sqlite3 as sql
from datetime import date

def addWebsite(name, password):
    """Add a new website and its correspondig password to the database"""
    db = sql.connect("data.db")
    cr = db.cursor()
    cr.execute("INSERT INTO w3b VALUES(?, ?, ?)", (name, password, str(date.today())))
    db.commit()
    db.close()

def viewAll():
    """See the contents from the database"""
    db = sql.connect("data.db")
    cr = db.cursor()
    cr.execute("SELECT * FROM w3b")
    info_from_db = "ID\tWebsite\t\t\t\tPassword\t\t\tDate\n"+"-"*95+"\n"
    counter = 1
    for row in cr.fetchall():
        nmb_tabs = math.floor(len(row[0])/8)
        nmb_tabs2 = math.floor(len(row[1])/8)
        info_from_db += str(counter)+".\t"+row[0]+"\t"*(4-nmb_tabs)+row[1]+"\t"*(4-nmb_tabs2)+row[2]+"\n"
        counter+=1
    db.close()
    info_from_db = info_from_db.replace("(", "")
    info_from_db = info_from_db.replace(")", "")
    info_from_db = info_from_db.replace(", ", "\t")
    return info_from_db

def deleteWebsite(name):
    """Delete a row with the matching name"""
    if 'M4IN' != name:
        db = sql.connect("data.db")
        cr = db.cursor()
        cr.execute("DELETE FROM w3b WHERE site=?", (name, ))
        db.commit()
        db.close()

def changePassword(name, new_password):
    """Alter database column password"""
    db = sql.connect("data.db")
    cr = db.cursor()
    cr.execute("UPDATE w3b SET pwd=?, date=? WHERE site=?", (new_password, str(date.today()), name))
    db.commit()
    db.close()

def copyToClipboard(number):
    """Enter row number to copy password to clipboard"""
    db = sql.connect("data.db")
    cr = db.cursor()
    content = cr.execute("SELECT pwd FROM w3b WHERE rowid=?", (number,)).fetchall()
    if content:
        pyperclip.copy(content[0][0])
    db.close()

def viewOne(name):
    """See the password corresponding to one row"""
    db = sql.connect("data.db")
    cr = db.cursor()
    content = cr.execute("SELECT pwd FROM w3b WHERE site=?", (name,)).fetchone()
    if content:
        return content
    else:
        return ""

if __name__ == "__main__":
    print(viewAll())
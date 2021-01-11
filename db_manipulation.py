import sqlite3 as sql

def addWebsite(name, password):
    """Add a new website and its correspondig password to the database"""
    db = sql.connect("data.db")
    cr = db.cursor()
    cr.execute("INSERT INTO w3b VALUES(?, ?)", (name, password))
    db.commit()
    db.close()

def viewAll():
    """See the contents from the database"""
    db = sql.connect("data.db")
    cr = db.cursor()
    cr.execute("SELECT * FROM w3b")
    info_from_db = ""
    counter = 1
    for row in cr.fetchall():
        info_from_db += str(counter)+".\t"+row+"\n"
        counter+=1
    db.close()
    return info_from_db

def deleteWebsite(name):
    """Delete a row with the matching name"""
    db = sql.connect("data.db")
    cr = db.cursor()
    cr.execute("DELETE FROM w3b WHERE site=?", (name, ))
    db.commit()
    db.close()

def changePassword(name, new_password):
    """Alter database column password"""
    db = sql.connect("data.db")
    cr = db.cursor()
    cr.execute("UPDATE w3b SET pwd=? WHERE site=?", (new_password, name))
    db.commit()
    db.close()


if __name__ == "__main__":
    db = sql.connect("data.db")
    cr = db.cursor()
    cr.execute("CREATE TABLE w3b(site text, pwd txt);")
    cr.execute("INSERT INTO w3b VALUES('M4IN', 'NULL')")
    db.commit()
    db.close()
import sqlite3


class DBConnect:
    def __init__(self):
        self._db=sqlite3.connect("Reservation.db")
        self._db.row_factory=sqlite3.Row
        self._db.execute("create table if not exists Ticket(ID integer primary key autoincrement,Name text,Gender text,Comments text)")
        self._db.commit()

    def Add(self,Name,Gender,Comments):
        self._db.execute("insert into Ticket(Name,Gender,Comments) values(?,?,?)",(Name,Gender,Comments))
        self._db.commit()
        return "request is submitted"
    def ListRequest(self):
        cursor=self._db.execute("select * from Ticket")
        return cursor;
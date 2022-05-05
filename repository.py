import sqlite3

from daos import Hats, Suppliers, Orders


class Repository:

    def __init__(self, path):
        self._conn = sqlite3.connect(path)
        self.Hats = Hats(self._conn)
        self.Suppliers = Suppliers(self._conn)
        self.Orders = Orders(self._conn)

    def create(self):
        self._conn.cursor().execute("""
                CREATE TABLE hats ( 
                id integer primary key autoincrement, 
                topping text,
                supplier INTEGER REFERENCES Supplier(id),
                quantity INTEGER
                )
                """)

        self._conn.cursor().execute("""
                        CREATE TABLE suppliers (
                        id integer primary key autoincrement,
                        name text
                        )
                        """)

        self._conn.cursor().execute("""
                        CREATE TABLE orders (
                        id integer primary key autoincrement,
                        location text,
                        hat INTEGER REFERENCES hats(id)
                        )
                        """)

    def delete_all_entries(self):
        self._conn.cursor().execute("DELETE FROM suppliers")
        self._conn.cursor().execute("DELETE FROM orders")
        self._conn.cursor().execute("DELETE FROM hats")


    def close(self):
        self._conn.commit()
        self._conn.close()


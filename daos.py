from dtos import Hat, Order, Supplier


class Hats:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, data):
        self._conn.execute("""
                INSERT INTO hats (topping, supplier, quantity) VALUES (?,?,?)
                """, data)

    def gethat(self, hid):
        hat = self._conn.execute("""
               SELECT id, topping, supplier, quantity FROM hats WHERE id = ?
                """, [hid]).fetchone()
        return Hat(*hat)

    def order(self, topping):
        print(topping)
        #oid, quantity, supplier_id
        data = self._conn.cursor().execute(("SELECT oid, quantity, supplier FROM hats WHERE topping LIKE ?"),
                                                   (f'%{topping}%',)).fetchall()
        oid, quantity, supplier_id = data[0]
        for tempOid, tempQuantity, tempSupplier_id in data:
            if tempSupplier_id < supplier_id:
                oid = tempOid
                quantity = tempQuantity
                supplier_id = tempSupplier_id
        if quantity == 1:
            self._conn.cursor().execute(("DELETE FROM hats WHERE oid=?"), (oid,))
        else:
            self._conn.cursor().execute(("UPDATE hats SET quantity=? WHERE oid=?"), (quantity - 1, oid))

        return oid, supplier_id


class Suppliers:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, data):
        self._conn.execute("""
                        INSERT INTO suppliers (name) VALUES (?);
                        """, data)

    def get_supplier(self, id):
        self.c = self._conn.cursor()
        supplier = self.c.execute("""
              SELECT id, name FROM suppliers WHERE id = ?
          """, [id]).fetchone()

        return Supplier(*supplier)


class Orders:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, data):
        self._conn.execute("""
                INSERT INTO orders (location, hat) VALUES (?,?);
                """, data)

    def get_orders(self):
        self._conn.cursor().execute("""
                                SELECT oid, location, hat FROM orders
                                """)
        orders = self._conn.cursor().fetchall()
        arr = [Order(*row) for row in orders]
        return arr

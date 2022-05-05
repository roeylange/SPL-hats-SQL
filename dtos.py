class Hat:
    def __init__(self, hid, topping, supplier, quantity):
        self.hid = hid
        self.topping = topping
        self.supplier = supplier
        self.quantity = quantity


class Order:
    def __init__(self, oid, location, hat):
        self.oid = oid
        self.location = location
        self.hat = hat


class Supplier:
    def __init__(self, sid, name):
        self.sid = sid
        self.name = name

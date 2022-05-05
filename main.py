import sys

from daos import Hats, Suppliers, Orders
from dtos import Hat, Supplier, Order
from repository import Repository


def main(config_dirc, order_dirc, output_dirc, database_dirc):
    flag = False
    reposit = Repository(database_dirc)
    hats = Hats(reposit._conn)
    suppliers = Suppliers(reposit._conn)
    orders = Orders(reposit._conn)
    # reposit.delete_all_entries()
    reposit.create()
    with open(config_dirc, "r") as text:
        for l in text:
            curr =l.split(",")
            index = len(curr[len(curr) - 1])
            if '\n' in curr[len(curr) - 1]:
                curr[len(curr) - 1] = curr[len(curr) - 1][:index - 1]

            if len(curr) == 4:
                h = Hat(curr[0],curr[1],curr[2],curr[3])
                curr.pop(0)
                hats.insert(curr)

            else:
                if not flag:
                    flag = True
                else:
                    Supplier(curr[0],curr[1])
                    curr.pop(0)
                    suppliers.insert(curr)

    with open(order_dirc, "r") as text:
        output = open(output_dirc, "w")
        index = 1
        for line in text:
            curr =line.split(",")
            location = curr[0]
            topping = curr[1]
            if '\n' in topping:
                topping = topping[:len(topping) - 1]
            hid, sid = hats.order(topping)
            Order(index, location, hid)
            index = index + 1
            orders.insert((location,hid))
            output.write(f"{topping},{suppliers.get_supplier(sid).name},{location}")
            output.write("\n")
        output.close()
    reposit.close()

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])


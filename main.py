import sqlite3
import sys
from typing import TextIO

from order import order
from Repository import r
from hat import hat
from supplier import supplier

# python3 main . py c o n f i g . t x t o r d e r s . t x t output . t x t d a t a b a s e . db
#           0                   1                   2               3               4
if __name__ == '__main__':
    config_file_path = sys.argv[1]
    orders_file_path = sys.argv[2]
    output_file_path = sys.argv[3]
    DB_file_path = sys.argv[4]

    r.set_database_path(DB_file_path)
    r.create_tables()

    # config_text: TextIO = open(sys.argv[1], "r+")
    text1 = open(config_file_path, "r+").read()
    numHats = int(text1[0: text1.find(',')])
    i = 0
    for line in text1.split('\n'):
        content = line.split(',')
        if 1 <= i <= numHats:
            ansOfHats = hat(content[0], content[1], content[2], content[3])
            r.hats.insert(ansOfHats)
        elif i > numHats:
            ansOfSupplier = supplier(content[0], content[1])
            r.suppliers.insert(ansOfSupplier)
        i = i + 1

    # orders_text = open(sys.argv[2], "r+").read()
    text2 = open(orders_file_path, "r+").read()
    writenAnswer = ""
    idOfOrder = 1
    for line in text2.split('\n'):
        content = line.split(',')
        location = content[0]
        nameOfTopping = content[1]
        hat = r.hats.sorter(nameOfTopping)
        if hat is not None:
            # here we check if there are no more hats left in the database
            if hat.quantity == 1:
                # there are no more hats left, so we remove the line from the database
                r.hats.remove(hat.id)
            else:
                # there are still more hats to spare, so we just update the database
                r.hats.update(hat.id, hat.quantity - 1)
        else:
            # this means we tried to access a hat that does not exist in the database
            print("ERROR : cannot find this hat...")

        ansOfOrders = order(idOfOrder, hat.id, location)
        r.orders.insert(ansOfOrders)
        idOfOrder = idOfOrder + 1

        name = r.suppliers.getSupplier(hat.supplier).name
        writenAnswer = writenAnswer + nameOfTopping + ',' + name + ',' + location + '\n'

    writer = open(output_file_path, "w")
    writer.write(writenAnswer)
    writer.close()

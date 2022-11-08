import atexit
import order
import supplier
import sqlite3
import hat
from DAO import DAO


class Repository:

    def __init__(self):
        self._c = None
        self.hats = None
        self.orders = None
        self.suppliers = None

    def set_database_path(self, path):
        self._c = sqlite3.connect(path)
        self.hats = DAO(hat, self._c)
        self.orders = DAO(order, self._c)
        self.suppliers = DAO(supplier, self._c)

    def create_tables(self):
        self._c.execute("""CREATE TABLE hats (id INT PRIMARY KEY, topping TEXT NOT NULL, supplier INT REFERENCES suppliers(id), quantity INT NOT NULL)""")
        self._c.execute("""CREATE TABLE orders (id INT PRIMARY KEY, hat INT REFERENCES hats(id), location TEXT NOT NULL)""")
        self._c.execute(""" CREATE TABLE suppliers (id INT PRIMARY KEY,name TEXT NOT NULL) """)

    def close(self):
        if self._c is not None:
            self._c.commit()
            self._c.close()


r = Repository()
atexit.register(r.close)

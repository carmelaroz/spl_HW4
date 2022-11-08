from hat import hat
from supplier import supplier


class DAO:
    def __init__(self, t, c):
        self.name = t.__name__.lower() + 's'
        self._t = t
        self._c = c

    def insert(self, inst):
        ans = vars(inst)
        q = ','.join(['?'] * len(ans))
        self._c.execute('INSERT OR REPLACE INTO {} VALUES ({})'.format(self.name, q), list(ans.values()))

    def update(self, id, val):
        self._c.execute('UPDATE {} SET quantity={} WHERE (id = {})'.format(self.name, val, id))

    def find(self, **value):
        c = self._c.cursor()
        content = value.keys()
        c.execute('SELECT * FROM {} WHERE {}'.format(self.name, ' AND '.join([column + '=?' for column in content])), list(value.values()))

    def sorter(self, v):
        c = self._c.cursor()
        c.execute("""SELECT * FROM hats WHERE topping = ? ORDER BY supplier""", [v])
        return hat(*c.fetchone())

    def remove(self, id):
        self._c.execute('DELETE FROM {} WHERE (id={})'.format(self.name, id))

    def getSupplier(self, id):
        c = self._c.cursor()
        c.execute("""SELECT * FROM suppliers WHERE id = ?""", [id])
        return supplier(*c.fetchone())

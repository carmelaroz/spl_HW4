from DTO import DTO


class hat(DTO):

    def __init__(self, id, t, s, q):
        super().__init__(id)
        self.topping = t
        self.supplier = s
        self.quantity = q

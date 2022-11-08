from DTO import DTO


class supplier (DTO):

    def __init__(self, id, n):
        super().__init__(id)
        self.name = n
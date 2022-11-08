from DTO import DTO


class order(DTO):

    def __init__(self, id, hat, location):
        super().__init__(id)
        self.hat = hat
        self.location = location

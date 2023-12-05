class Vehicle:
    all = []

    def __init__(self, x, y, id):
        self.id = id
        self.x_pos = x
        self.y_pos = y
        self.x_ant = None
        self.y_ant = None
        Vehicle.all.append(self)

    def get_pos(self):
        return self.x_pos, self.y_pos

    def get_id(self):
        return self.id

    def update_pos(self, x, y):
        self.x_ant, self.y_ant = self.get_pos()
        self.x_pos = x
        self.y_pos = y

    @staticmethod
    def delete_vehicle(id):
        for i in range(len(Vehicle.all)):
            if Vehicle.all[i].get_id() == id:
                Vehicle.all.pop(i)

    @staticmethod
    def vehicle_count():
        return len(Vehicle.all)
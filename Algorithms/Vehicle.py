import math


class Vehicle:
    all = []

    def __init__(self, x, y, id_num):
        self.id = id_num
        self.x_pos = x
        self.y_pos = y
        self.x_ant = None
        self.y_ant = None
        Vehicle.all.append(self)
        self.found = 1

    def set_found(self, value):
        self.found = value

    def get_found(self):
        return self.found

    def get_pos(self):
        return self.x_pos, self.y_pos

    def get_id(self):
        return self.id

    def update_pos(self, x, y):
        self.x_ant, self.y_ant = self.get_pos()
        self.x_pos = x
        self.y_pos = y

    @staticmethod
    def reset_found():
        if Vehicle.vehicle_count() == 0:
            return
        for vehicle in Vehicle.all:
            vehicle.set_found(0)

    @staticmethod
    def delete_vehicle(id_num):
        count = 0
        if Vehicle.vehicle_count() == 0:
            return
        for vehicle in Vehicle.all:
            if vehicle.get_id() == id_num:
                Vehicle.all.pop(count)
            count += 1

    @staticmethod
    def delete_missing():
        if Vehicle.vehicle_count() == 0:
            return
        for vehicle in Vehicle.all:
            if vehicle.get_found() == 0:
                Vehicle.delete_vehicle(vehicle.get_id())

    @staticmethod
    def vehicle_count():
        return len(Vehicle.all)

    @staticmethod
    def clear_all():
        Vehicle.all.clear()

    @staticmethod
    def compare_vehicle_proximity(x, y, v1, v2):
        v1_x, v1_y = v1.get_pos()
        v2_x, v2_y = v2.get_pos()
        d1 = math.sqrt((x - v1_x)**2 + (y - v1_y)**2)
        d2 = math.sqrt((x - v2_x)**2 + (y - v2_y)**2)
        if d1 < d2:
            return v1
        else:
            return v2

    @staticmethod
    def search_vehicle_position(x, y):
        th = 10  # threshold of minimal distance
        best = None
        if Vehicle.vehicle_count() == 0:
            print("Error: There's no vehicle to search")
            return None
        for vehicle in Vehicle.all:
            v_x, v_y = vehicle.get_pos()
            if x < 640:  # Search on the left side of the frame
                if abs(v_x - x) <= th and th > v_y - y > 0:
                    if best is None:
                        best = vehicle
                    else:
                        best = Vehicle.compare_vehicle_proximity(x, y, vehicle, best)
            else:  # Search on the right side of the frame
                if abs(v_x - x) <= th and th > y - v_y > 0:
                    if best is None:
                        best = vehicle
                    else:
                        best = Vehicle.compare_vehicle_proximity(x, y, vehicle, best)
        return best

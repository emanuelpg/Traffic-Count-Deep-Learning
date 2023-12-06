import math
import Tracker


class Vehicle:
    all = []

    def __init__(self, box, id_num):
        self.id = id_num
        self.box_pos = box
        self.box_ant = None
        self.x_pos, self.y_pos = Tracker.Tracker.find_center(box.xyxy[0])
        self.x_ant = None
        self.y_ant = None
        self.found = 1
        Vehicle.all.append(self)

    def set_found(self, value):
        self.found = value

    def get_found(self):
        return self.found

    def get_pos(self):
        return self.x_pos, self.y_pos

    def get_box_pos(self):
        return self.box_pos

    def get_id(self):
        return self.id

    def update_box(self, new_box):
        x, y = Tracker.Tracker.find_center(new_box.xyxy[0])
        self.update_pos(x, y)
        self.box_ant = self.box_pos
        self.box_pos = new_box

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
        d1 = math.sqrt((x - v1_x) ** 2 + (y - v1_y) ** 2)
        d2 = math.sqrt((x - v2_x) ** 2 + (y - v2_y) ** 2)
        if d1 < d2:
            return v1
        else:
            return v2

    @staticmethod
    def box_area(box):
        box_xyxy = box.xyxy[0]
        area = (box_xyxy[2] - box_xyxy[0]) * (box_xyxy[3] - box_xyxy[1])
        return area

    @staticmethod
    def intersection_over_union(box1, box2):
        box1_xyxy = box1.xyxy[0]
        box2_xyxy = box2.xyxy[0]
        area1 = Vehicle.box_area(box1)
        area2 = Vehicle.box_area(box2)
        if box1_xyxy[0] > box2_xyxy[2] or box2_xyxy[0] > box1_xyxy[2]:
            return 0.
        if box1_xyxy[1] > box2_xyxy[3] or box2_xyxy[1] > box1_xyxy[3]:
            return 0.

        union = area1 + area2
        intersection = (min(box1_xyxy[2] - box2_xyxy[0],
                            box2_xyxy[2] - box1_xyxy[0]) *
                        min(box1_xyxy[3] - box2_xyxy[1],
                            box2_xyxy[3] - box1_xyxy[1]))
        iou = intersection / (union - intersection)
        return iou

    @staticmethod
    def compare_vehicles_iou(box, v1, v2):
        v1_box = v1.get_box_pos()
        v2_box = v2.get_box_pos()
        iou1 = Vehicle.intersection_over_union(box, v1_box)
        iou2 = Vehicle.intersection_over_union(box, v2_box)
        if iou1 > iou2:
            return v1
        else:
            return v2

    @staticmethod
    def search_vehicle_box(box):
        best = None
        if Vehicle.vehicle_count() == 0:
            print("Error: There's no vehicle to search")
            return best
        for vehicle in Vehicle.all:
            v_box = vehicle.get_box_pos()
            if Vehicle.intersection_over_union(box, v_box) > 0.2:
                if best is None:
                    best = vehicle
                else:
                    best = Vehicle.compare_vehicles_iou(box, vehicle, best)
        return best

    @staticmethod
    def search_vehicle_position(x, y):
        th = 50  # threshold of minimal distance
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

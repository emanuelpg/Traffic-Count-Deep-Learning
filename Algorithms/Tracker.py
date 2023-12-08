import Vehicle
import VideoProcessing
import cv2


class Tracker:
    vehicle_cats = ["car", "bus", "truck", "motorcycle"]

    def __init__(self, detection_model):
        self.model = detection_model
        self.model_names = self.model.names

    def video_det_viewer(self, video_path, video_name):
        video = cv2.VideoCapture(video_path)
        ret, frame = video.read()
        while ret:
            result = self.model(frame)[0]
            im_array = result.plot()
            cv2.imshow(video_name, im_array)
            cv2.waitKey(40)

            ret, frame = video.read()
        cv2.destroyAllWindows()

    def get_classes_names(self):
        return self.model_names

    def detect(self, frame):
        return self.model(frame, verbose=False)[0]

    def detection_boxes(self, frame):
        det = self.detect(frame)
        return det.boxes

    @staticmethod
    def find_center(boxe_xyxy):
        mid_x = int(boxe_xyxy[0] + (boxe_xyxy[2] - boxe_xyxy[0])/2)
        mid_y = int(boxe_xyxy[1] + (boxe_xyxy[3] - boxe_xyxy[1])/2)
        return mid_x, mid_y

    def track(self, video_path, iou_th=0.2):
        id_num = 0
        count = 0
        video = VideoProcessing.VideoProcessing(video_path)
        for frame in video.get_frames():
            Vehicle.Vehicle.reset_found()
            count += 1
            boxes = self.detection_boxes(frame)
            for box in boxes:
                x, y = Tracker.find_center(boxes.xyxy[0])
                if y > 450:
                    if count == 1 and self.get_classes_names()[int(box.cls)] in Tracker.vehicle_cats:
                        Vehicle.Vehicle(box, id_num)
                        id_num += 1
                    elif self.get_classes_names()[int(box.cls)] in Tracker.vehicle_cats:
                        vehicle_found = Vehicle.Vehicle.search_vehicle_box(box, iou_th)
                        if vehicle_found is None:
                            Vehicle.Vehicle(box, id_num)
                            id_num += 1
                        else:
                            vehicle_found.update_box(box)
                            vehicle_found.set_found(1)
            if count % (int(video.get_fps())*10) == 0:  # Delete vehicles that weren't found on the screen anymore
                Vehicle.Vehicle.delete_missing()
        return id_num+1

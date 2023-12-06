from ultralytics import YOLO
import os
import time
import Tracker


def solver(parent_dir):
    detection_model = YOLO('yolov8n.pt')
    tracker = Tracker.Tracker(detection_model)
    count = 1
    for video_name in os.listdir(parent_dir):

        print(f"Counting vehicles in video {count}, please wait...")
        video_path = parent_dir + video_name
        # tracker.video_det_viewer(video_path, video_name)  # Visualize detection video
        start = time.time()
        print(f"Number of Vehicles in video {count}: {tracker.track(video_path)} vehicles")
        end = time.time()
        time_diff = end - start
        print("Counting video %d took %.4f minutes" % (count, time_diff/60))
        count += 1

videos_dir = "D:/Traffic-Count-Deep-Learning/Dataset Atividade/"

solver(videos_dir)

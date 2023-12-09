from ultralytics import YOLO
import os
import time
import Tracker
import numpy as np
import matplotlib.pyplot as plt


# Solver: Count the number of vehicles on some given videos.
# Input: Directory path where all videos are present.
# Output: Vehicle count for each video inside the input directory.
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


# Function used to measure the effect of different thresholds for IoU measurement
def measuring_iou_th(video_path):
    detection_model = YOLO('yolov8n.pt')
    tracker = Tracker.Tracker(detection_model)
    ths = np.linspace(0, 1, num=11)
    counts = []
    for th in ths:
        print("Counting for iou_th =", th)
        value = tracker.track(video_path, iou_th=th)
        print("Vehicle count:", value)
        counts.append(value)

    # Plotting results
    plt.plot(ths, counts)
    plt.xlabel("iou threshold")
    plt.ylabel("Vehicle count")
    plt.title("Graphic of iou_threshold x vehicle count")
    plt.show()


videos_dir = "D:/Traffic-Count-Deep-Learning/Dataset Atividade/"
video1_path = videos_dir + os.listdir(videos_dir)[0]

# measuring_iou_th(video1_path)
solver(videos_dir)

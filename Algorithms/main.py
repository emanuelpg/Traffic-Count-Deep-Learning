from ultralytics import YOLO
import cv2
import numpy as np
import sys, os
import VideoProcessing
import SupplyFunctions
import Tracker


def solver(parent_dir):
    detection_model = YOLO('yolov8n.pt')
    tracker = Tracker.Tracker(detection_model)
    videos = []
    count = 1
    for video_name in os.listdir(parent_dir):
        print(f"Counting vehicles in video {count}...")
        video_path = parent_dir + video_name
        print(f"Number of Vehicles in video {count}: {tracker.track(video_path)} vehicles")
        count += 1


videos_dir = "D:/Traffic-Count-Deep-Learning/Dataset Atividade/"

solver(videos_dir)

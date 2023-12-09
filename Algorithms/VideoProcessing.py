import cv2
import numpy as np
import os, sys


class VideoProcessing:
    def __init__(self, video_path):
        try:
            self.video = cv2.VideoCapture(video_path)
            self.frames = self.frame_extraction()
            self.fps = self.video.get(cv2.CAP_PROP_FPS)
            self.frame_count = self.video.get(cv2.CAP_PROP_FRAME_COUNT)
            self.duration = self.frame_count / self.fps
        except:
            print("Error trying to open video, do something")

    def get_frames(self):
        return self.frames

    def get_fps(self):
        return self.fps

    def get_frame_count(self):
        return self.frame_count

    def get_duration(self):
        return self.duration

    # Visualize the video
    def video_viewer(self):
        frame_rate = self.get_fps()
        waiting_time = int(1/frame_rate * 1000)
        for frame in self.frames:
            cv2.imshow('frame', frame)
            cv2.waitKey(waiting_time)

        cv2.destroyAllWindows()

    # Extract the frames of the video
    def frame_extraction(self):
        frames = []
        self.video.set(cv2.CAP_PROP_POS_FRAMES, 0)
        ret, frame = self.video.read()
        while ret:
            frames.append(frame)
            ret, frame = self.video.read()

        return np.array(frames)

    # Saves the frames of the video in a given folder
    def frame_saving(self, folder_path):
        count = 0
        for frame in self.get_frames():
            cv2.imwrite(f"{folder_path}/frame_{count}.jpg", frame)
            count += 1


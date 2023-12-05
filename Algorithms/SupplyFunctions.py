import os, sys
import VideoProcessing


def create_directory(dir_name, parent_dir):
    dir_path = os.path.join(parent_dir, dir_name)
    try:
        os.mkdir(dir_path)
    except:
        print("ERROR: directory probably already exists, verify that")


def video_frames_saving(videos, videos_names, parent_dir):
    video_count = 0
    for video in videos:
        path = os.path.join(parent_dir, f"frames_{videos_names[video_count]}")
        create_directory(path)
        video_processor = VideoProcessing.VideoProcessing(video)
        video_processor.frame_saving(path)
        video_count += 1



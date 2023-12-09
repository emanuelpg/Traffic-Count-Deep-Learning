import os, sys
import VideoProcessing


# Create_directory: Creates a directory given its name and parent directory
# Input: Name of the new directory; Path to parent directory
def create_directory(dir_name, parent_dir):
    dir_path = os.path.join(parent_dir, dir_name)
    try:
        os.mkdir(dir_path)
    except:
        print("ERROR: directory probably already exists, verify that")


# video_frames_saving: Saves each frame of a video in a folder.
# Input: list of videos; name of each video; path to parent directory to save the frames folders
def video_frames_saving(videos, videos_names, parent_dir):
    video_count = 0
    for video in videos:
        path = os.path.join(parent_dir, f"frames_{videos_names[video_count]}")
        create_directory(path)
        video_processor = VideoProcessing.VideoProcessing(video)
        video_processor.frame_saving(path)
        video_count += 1



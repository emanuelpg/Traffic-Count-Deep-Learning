# Traffic-Count-Deep-Learning
Traffic counting algorithm using Deep Learning and Computer Vision techiniques.

This repository contains my solution (or trial) to the problem suggested in the Selective Process of Visio.AI Internship.
The idea is create a script that receives a video of a traffic road and returns the number of vehicles that crossed that road in the video.

## Development Report
### Abstract
Measuring traffic density conventionaly takes a huge effort of managing people and spending money to do that. Recent studies show that applying Deep Learning and Computer Vision techinques transforms the problem into a more affordable and pratical one ([1](https://ieeexplore.ieee.org/document/9768653), [2](https://ieeexplore.ieee.org/document/9941299), [3](https://ieeexplore.ieee.org/document/9912668)). Thus, my project aims to employ these techiniques by merging object detection and tracking to count the number of vehicles that crossed a road in a pre-recorded video. To do this, I applied the YOLOV8 algorithm to detect the objects in a frame, and a tracker (coded by me) based on IoU (Intersection of Unior) measurements to track and count the number of vehicles. Though the correct number of vehicle in the video is not exactly known, with a self-paced (totally not much of a scientific method) counting, it can be seen that the algorithm shows expected results.

### Methodology
#### Dataset
The dataset is available in the repository. It consists of 67 videos of the same road, each one with 30 seconds (25 fps). The camera and position is the same for all of the videos. Below, you can see an example of a frame taken from the first video.

![video frame example](https://github.com/emanuelpg/Traffic-Count-Deep-Learning/blob/main/frame_example.jpg)

#### Algorithm
You Only Look Once (YOLO) is a deep learning algorithm designed for real-time object detection in images and videos. Developed by Joseph Redmon and Santosh Divvala, YOLO revolutionized object detection by dividing the image into a grid and predicting bounding boxes and class probabilities for objects within each grid cell in a single pass. Unlike traditional methods that require multiple passes, YOLO's single-shot approach enables faster and more efficient real-time detection. YOLO balances speed and accuracy, making it widely used in applications like surveillance, autonomous vehicles, and robotics, where quick and precise object recognition is crucial. In this project, the pre-trained 8th version of the algorithm is used to detect the vehicles presents in the video. The bounding boxes returned by it are, then, processed by a tracker which compares with the already predicted vehicles to decide whether is a previous seen vehicle or not. The comparation is based considering a positive (> 0.0) value in the IoU measurement of both (previous predicted and new) bounding boxes. Furthermore, the tracker only considers vehicles that crossed a certain y hight value between 400 and 500 pixels.

#### Model validation and results
By now, the model wasn't rigourous validated, the expected results were based on limited manual count of vehicles in the videos, where it was around 70-90 vehicles. But the manual measure wasn't made for all of the videos (just the first ones). And the algorithm did obtained a result value between the expected for those.

#### Conclusions
With a pre well-defined detection model (YOLO) and a simple trakcer we can see the incredible potential of applying Deep Learning and Computer Vision techiniques on traffic counting (a great way of learning more about those techniques). But, this project still lacks some details that could improve its applicability. First, we need a more scientifc approach to better validate the model with well defined metrics and ground truth results. Secondly it is very import to compare it with other existing models (including some already well-known trackers). So, there's a lot of room to explore and more variables to test in this project. Besides that, I reinforce the educational intention of this project as a way of understand how to deal with a real-life problem as a Computer Vision and AI researcher.

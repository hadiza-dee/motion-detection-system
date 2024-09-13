# motion-detection-system
The real-time motion detection system is designed to identify motion in live video streams, such as from a webcam or video file, and capture the moment by saving screenshots. This is ideal for applications like security surveillance, home automation, or any system where tracking movement is necessary.

The detection works by analyzing differences between consecutive video frames, highlighting the regions where movement occurs. When motion is detected, the system captures the frame and saves it as an image file.

Features:

Real-Time Motion Detection: Detect motion in real-time using a live video stream from a webcam or other video sources.

Screenshot Capture: Automatically captures and saves screenshots of frames where motion is detected.

Video Processing with OpenCV: Uses OpenCV for image processing, motion detection, and screenshot functionality.

Customizable Sensitivity: Configure the sensitivity of motion detection to control how easily motion is triggered.

Lightweight and Efficient: Designed to run efficiently on most systems using Python and OpenCV.


Project Structure:

motion_detection_system.py: The main Python script that handles real-time motion detection and screenshot capturing.

screenshots/: This folder is created automatically when you run the python file. It is a directory where the motion detection system saves captured screenshots of detected motion.

README.md: This file, providing an overview and instructions for using the system.



Prerequisites: Ensure that Python 3.x and OpenCV are installed on your system.

import cv2
import os
from datetime import datetime

# Create a directory for screenshots if it doesn't exist
screenshot_dir = "screenshots"
if not os.path.exists(screenshot_dir):
    os.makedirs(screenshot_dir)

video = cv2.VideoCapture(0)

first_frame = None
motion_records = []  # List to store motion timestamps and corresponding screenshots

while True:
    check, frame = video.read()
    if not check:
        print("Failed to grab frame")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    
    if first_frame is None:
        first_frame = gray
        continue

    delta_frame = cv2.absdiff(first_frame, gray)
    threshold_frame = cv2.threshold(delta_frame, 50, 255, cv2.THRESH_BINARY)[1]
    threshold_frame = cv2.dilate(threshold_frame, None, iterations=2)
    (cntr, _) = cv2.findContours(threshold_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cntr:
        if cv2.contourArea(contour) < 1000:
            continue
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

        # Capture screenshot and save with timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_filename = os.path.join(screenshot_dir, f"screenshot_{timestamp}.jpg")
        cv2.imwrite(screenshot_filename, frame)
        motion_records.append((timestamp, screenshot_filename))

    cv2.imshow("Motion Detection", frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
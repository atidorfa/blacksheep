import os
import sys
import time

import cv2

import HandTrackingModule as htm
import web

camera_port = 0
cam_width, cam_height = 640, 480

capture = cv2.VideoCapture(camera_port, cv2.CAP_DSHOW)
capture.set(3, cam_width)
capture.set(4, cam_height)

folder_path = "img"
my_list = os.listdir(folder_path)
overlay_list = []

for image_path in my_list:
    image = cv2.imread(f"{folder_path}/{image_path}")
    overlay_list.append(image)


detector = htm.handDetector(detectionCon=1)
previous_time = 0
tip_id = [4, 8, 12, 16, 20]

while True:
    success, img = capture.read()
    img = detector.findHands(img)
    landmark_list = detector.findPosition(img, draw=False)

    # check mediapipe documentation

    if len(landmark_list) != 0:
        fingers = []

        # Thumb
        if landmark_list[tip_id[0]][1] > landmark_list[tip_id[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        # 4 Fingers
        for i in range(1, 5):
            if landmark_list[tip_id[i]][2] < landmark_list[tip_id[i] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        total_fingers = fingers.count(1)

        # Open Youtube program
        if total_fingers == 5:
            web.open_fitness()
            sys.exit()

        # image output
        offset = 8  # margin offset
        h, w, c = overlay_list[total_fingers - 1].shape
        img[
            offset : h + offset, (cam_width - w - offset) : cam_width - offset
        ] = overlay_list[total_fingers - 1]

        # number output
        # cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)
        # cv2.putText(img, str(total_fingers), (45, 375), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    current_time = time.time()
    fps = 1 / (current_time - previous_time)
    previous_time = current_time
    cv2.putText(
        img, f"fps: {int(fps)}", (20, 60), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2
    )

    cv2.imshow("Image", img)
    cv2.waitKey(1)  # 1ms delay so we can see our img


# cv2.destroyAllWindows()

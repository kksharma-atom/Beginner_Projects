import cv2, glob, os
import time
from datetime import datetime
from emailing import send_email
from threading import Thread

video = cv2.VideoCapture(0)
time.sleep(1)

status_list = []
first_frame = None
count = 1

def clean_folder():
    print("Clean folder function started")
    images = glob.glob("images/*.png")
    for image in images:
        os.remove(image)
    print("Clean folder function ended")

while True:
    status = 0
    check, frame = video.read()

    now = datetime.now()
    cv2.putText(frame, now.strftime("%A"), (30, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 4, cv2.LINE_AA)
    cv2.putText(frame, now.strftime("%H:%M:%S"), (30, 140), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 4, cv2.LINE_AA)

    grey_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    grey_frame_gav = cv2.GaussianBlur(grey_frame, (21, 21), 0)


    if first_frame is None:
        first_frame = grey_frame_gav
    
    delta_frame = cv2.absdiff(first_frame, grey_frame_gav)

    thresh_frame = cv2.threshold(delta_frame, 50, 255, cv2.THRESH_BINARY)[1]
    dil_frame = cv2.dilate(thresh_frame, None, iterations=2)
    cv2.imshow("My video", dil_frame)

    contours, check = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 5000:
            continue
        x, y, w, h = cv2.boundingRect(contour)
        rectangle = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
        if rectangle.any():
            status = 1
            cv2.imwrite(f"images/{count}.png", frame)
            count = count + 1
            all_images = glob.glob("images/*.png")
            index = int(len(all_images)/2)
            image_with_object = all_images[index]

    status_list.append(status)
    status_list = status_list[-2:]
    if status_list[0] == 1 and status_list[1] == 0:
        email_thread = Thread(target=send_email, args=(image_with_object,))
        email_thread.daemon = True

        clean_thread = Thread(target=clean_folder)
        clean_thread.daemon = True

        email_thread.start()

    print(status_list)

    cv2.imshow("Video", frame)

    key = cv2.waitKey(1)

    if key == ord("q"):
        break

video.release()

clean_thread.start()


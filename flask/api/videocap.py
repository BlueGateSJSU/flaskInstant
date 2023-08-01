import cv2
import recognize 
import os
from datetime import datetime

def videoCapture(name):
    #output에는 강아지 이름별로 카테고리 및 이름은 현재시간 기준
    video_path = f"{os.getcwd()}/data/video/temp.mp4"
    output_img = f"{os.getcwd()}/data//detect/{name}{datetime.now()}.jpg/"
    
    
    cap = cv2.VideoCapture(video_path)

    while True:
        # 프레임 읽기
        ret, frame = cap.read()
        if cap.get(1) % 10 == 0:
            if not ret:
                break
            frame = cv2.resize(frame,(640,640))
            
            if recognize.find_dog_face(frame):
                pass

            cv2.imwrite(output_img,frame)
        else:
            continue

    # 작업 완료 후, 캡처 해제
    cap.release()
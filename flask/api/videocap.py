import cv2
import recognize 
import os
from datetime import datetime

def videoCapture(known_face_encodings, known_face_names ,size=None):
    #output에는 강아지 이름별로 카테고리 및 이름은 현재시간 기준
    name = ''
    video_path = f"{os.getcwd()}/data/video/temp.mp4"
    output_img = f"{os.getcwd()}/data//detect/{name}{datetime.now()}.jpg/"
    
    
    cap = cv2.VideoCapture(video_path)
    
    #비디오 프레임률 추출
    frame_rate = cap.get(cv2.CAP_PROP_FPS)
    frame_interval = int(frame_rate * 10) #10초 간격으로 캡쳐
    
    frame_count = 0 

    while True:
        # 프레임 읽기
        ret, frame = cap.read()
    
        if not ret:
            break
        # frame = cv2.resize(frame,size)
        if frame_count % frame_interval == 0:
            if recognize.checking(frame,known_face_encodings,known_face_names):
                cv2.imwrite(output_img,frame)
            else:
                continue                
        else:
            continue

    # 작업 완료 후, 캡처 해제
    cap.release()
    
# def webcamCapture(known_face_encodings, known_face_names ,size=None):
#     name = ''
#     output_img = f"{os.getcwd()}/data//detect/{name}{datetime.now()}.jpg/"
    
    
#     cap = cv2.VideoCapture(0)
    
#     #비디오 프레임률 추출
#     frame_rate = cap.get(cv2.CAP_PROP_FPS)
#     frame_interval = int(frame_rate * 10) #10초 간격으로 캡쳐
    
#     frame_count = 0 

#     while True:
#         # 프레임 읽기
#         ret, frame = cap.read()
    
#         if not ret:
#             break
#         # frame = cv2.resize(frame,size)
#         if frame_count % frame_interval == 0:
#             if recognize.checking(frame,known_face_encodings,known_face_names):
#                 cv2.imwrite(output_img,frame)
#             else:
#                 continue                
#         else:
#             continue

#     # 작업 완료 후, 캡처 해제
#     cap.release()
    

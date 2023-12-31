import cv2
import recognize 
import os
from datetime import datetime

def videoCapture(name="아콩",known_face_encodings=None, known_face_names=None ,size=None):
    #output에는 강아지 이름별로 카테고리 및 이름은 현재시간 기준
    video_path = f"{os.getcwd()}/temp.mp4"
    
    dir = f"data/{datetime.today().strftime('%Y-%m-%d')}"
    try:
        if not os.path.exists(dir):
            os.mkdir(dir)
    except OSError:
        print('Error: Creating directory. ' +  dir, flush=True)
        
    output_img = f"{os.getcwd()}/{dir}/{name}{str(datetime.today()).replace(':','-')}"
    
    
    cap = cv2.VideoCapture(video_path)
    
    #비디오 프레임률 추출
    frame_rate = cap.get(cv2.CAP_PROP_FPS)
    frame_interval = int(frame_rate) #1초 간격으로 캡쳐
    
    frame_count = 0 

    while True:
        # 프레임 읽기
        ret, frame = cap.read()
        frame_count += 1
    
        if not ret:
            break
        # frame = cv2.resize(frame,size)
        if frame_count % frame_interval == 0:
            if recognize.checking(frame,known_face_encodings,known_face_names):
                cv2.imwrite(output_img+str(frame_count)+'.jpg',frame)
            print(frame_count)
                       

    # 작업 완료 후, 캡처 해제
    cap.release()
    
#test
videoCapture()


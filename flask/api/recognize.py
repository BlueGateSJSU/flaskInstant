import dlib
import face_recognition
import imutils
import numpy as np
import cv2
import os
import dlib, imutils, cv2, face_recognition
from imutils import face_utils

face_landmark_detector_path = 'lib/dogHeadDetector.dat'
face_landmark_predictor_path = 'lib/landmarkDetector.dat'

detector = dlib.cnn_face_detection_model_v1(face_landmark_detector_path)
predictor = dlib.shape_predictor(face_landmark_predictor_path)

def add_known_face(face_image_path, name):
    face_image = cv2.imread(face_image_path)
    dets_locations = face_locations(face_image, 1)
    face_encoding = face_recognition.face_encodings(face_image, dets_locations)[0]
    
    return face_encoding, name

def checking(input_image,known_face_encodings, known_face_names ,size=None): # 얼굴 체크
    
    dir = "./output"
    try:
        if not os.path.exists(dir):
            os.makedirs(dir)
    except OSError:
        print('Error: Creating directory. ' +  dir, flush=True)

    os.remove(dir+"/result.jpg")
    
    input_image = cv2.imread(input_image)
    image = input_image.copy()
    
    if size:
        image = imutils.resize(image, width=size)
        
    dets_locations = face_locations(image)
    face_encodings = face_recognition.face_encodings(image, dets_locations)
    
    face_names = []
    face_bools = []
    
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.4)
        name = "Unknown"
        flag = False

        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
 
        if matches[best_match_index]:
            name = known_face_names[best_match_index]
            flag = True
 
        face_names.append(name)
        face_bools.append(flag)

    for (top, right, bottom, left), name in zip(dets_locations, face_names):
        if name != "Unknown":
            color = (0, 255, 0)
        else:
            color = (0, 0, 255)
 
        cv2.rectangle(image, (left, top), (right, bottom), color, 1)
        cv2.rectangle(image, (left, bottom - 10), (right, bottom), color, cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(image, name, (left + 3, bottom - 3), font, 0.2, (0, 0, 0), 1)
    
    cv2.imwrite("./static/result.jpg", image)
    return any(face_bools)



def find_dog_face(input_image, size=None, debug=False):
    image = input_image.copy()
    
    if size:
        image = imutils.resize(image, width=size)
        
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    dets = detector(gray_image, 1)
    
    print('Found {} faces.'.format(len(dets)))
    
    for (i, det) in enumerate(dets):
        # 얼굴 영역의 얼굴 랜드마크를 결정한 다음 
        # 얼굴 랜드마크(x, y) 좌표를 NumPy Array로 변환합니다.
        shape = predictor(image, det.rect)
        shape = face_utils.shape_to_np(shape)
 
        # dlib의 사각형을 OpenCV bounding box로 변환(x, y, w, h)
        (x, y, w, h) = face_utils.rect_to_bb(det.rect)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(image, "Face #{}".format(i + 1), (x - 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
        if debug:
            # 얼굴 랜드마크에 포인트를 그립니다.
            for (i, (x, y)) in enumerate(shape):
                cv2.circle(image, (x, y), int(image.shape[1]/250), (0, 0, 255), -1)
                # cv2.putText(image, str(i + 1), (x - 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.2, (255, 255, 255), 1)
        
    return image


def _trim_css_to_bounds(css, image_shape):
    return max(css[0], 0), min(css[1], image_shape[1]), min(css[2], image_shape[0]), max(css[3], 0)
 
 
def _rect_to_css(rect):
    return rect.top(), rect.right(), rect.bottom(), rect.left()
 
 
def _raw_face_locations(img, number_of_times_to_upsample=1):
    return detector(img, number_of_times_to_upsample)
    
 
def face_locations(img, number_of_times_to_upsample=1):
    return [_trim_css_to_bounds(_rect_to_css(face.rect), img.shape) for face in _raw_face_locations(img, number_of_times_to_upsample)]
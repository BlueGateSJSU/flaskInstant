import dlib

face_landmark_detector_path = 'lib/dogHeadDetector.dat'
face_landmark_predictor_path = 'lib/landmarkDetector.dat'

detector = dlib.cnn_face_detection_model_v1(face_landmark_detector_path)
predictor = dlib.shape_predictor(face_landmark_predictor_path)

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
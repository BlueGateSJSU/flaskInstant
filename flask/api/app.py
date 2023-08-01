from flask import Flask, jsonify, redirect, render_template, Response, request, session, url_for
from datetime import timedelta
import dlib, imutils, cv2, face_recognition
from imutils import face_utils
import numpy as np
import matplotlib.pyplot as plt
from recognize import *
import os
import sys
sys.stdout.flush()



def create_app():
    app = Flask(__name__)
    app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=60)
    app.secret_key = "asdfk"
    
    @app.route('/regist', methods=['POST'])
    def upload_photo():
        dir = "./registedIMG"
        try:
            if not os.path.exists(dir):
                os.makedirs(dir)
        except OSError:
            print('Error: Creating directory. ' +  dir, flush=True)

        photos = request.files.getlist("files[]")
        names  = request.form.getlist("names[]")

        # 모델 불러오기

  
        # 사진 인코딩해서 세션에 저장
        for name, img in (zip(names, photos)):

            
            img.save(dir+"/"+name+".jpg")

            # #ecoding img
            # dog_face_img = cv2.imread(dir+"/"+name+".jpg")
            # dets_locations = face_locations(dog_face_img, 1)
            # face_encoding = face_recognition.face_encodings(dog_face_img, dets_locations)[0]

            #로컬에 기록
            # with open(dir+"/"+name+".txt", "w") as f:
            #     f.write()


            # #session
            # old_encodings = []
            # old_names = []
            # if 'known_face_encodings' in session and 'known_face_name' in session:
            #     print("load session")
            #     old_encodings = session['known_face_encodings']
            #     old_names = session['known_face_name']
            # else :  #로컬에 저장했다가 세션으로 불러옴 / 구현 x
            #     print("make session")
            #     session['known_face_encodings'] = []
            #     session['known_face_name'] = []
               
         
            
            # old_encodings.append(face_encoding)
            # old_names.append(name)

            # session['known_face_encodings'] = old_encodings
            # session['known_face_name'] = old_names
        

        return "good"
    
    @app.route('/check', methods=['POST'])
    def check_registed_dog():
        ans = "no"

        known_face_encodings = []
        known_face_names = []

        enc, name = add_known_face()
        known_face_encodings.append(enc)
        known_face_encodings.append(name)

        

        return ans

    return app


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
  
        # 사진 인코딩해서 세션에 저장
        for name, img in (zip(names, photos)):  
            img.save(dir+"/"+name+".jpg")

        return "good"
    
    @app.route('/check', methods=['POST'])
    def check_registed_dog():

        dir = "./target"
        try:
            if not os.path.exists(dir):
                os.makedirs(dir)
        except OSError:
            print('Error: Creating directory. ' +  dir, flush=True)

        reqIMG = request.files['target'] # 입력 이미지 저장
        reqIMG.save(dir+"/temp.jpg")

        known_face_encodings = [] # registed data 가져온다
        known_face_names = []     

        file_list = os.listdir("./registedIMG")

        for f in file_list:
            enc, name = add_known_face("./registedIMG/"+f, f.split('.')[0])
            known_face_encodings.append(enc)
            known_face_names.append(name)

        if checking(dir+"/temp.jpg", known_face_encodings, known_face_names):
            return "true"
        else:
            return "false"

    return app


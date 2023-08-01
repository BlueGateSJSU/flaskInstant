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

    @app.route('/hi', methods=['POST'])
    def hello():
        return jsonify({'reply' : "welcome"}), 200
    
    @app.route('/')
    def home():
        return render_template('main.html')
    
    @app.route('/regist', methods=['POST'])
    def upload_photo():
        dir = "./registedIMG"
        try:
            if not os.path.exists(dir):
                os.makedirs(dir)
        except OSError:
            print('Error: Creating directory. ' +  dir, flush=True)

        photos = request.files.getlist("files")
        names  = request.form.getlist("names")
        print("kkkkkk")
        for name, img in (zip(names, photos)):
            #img.save(dir+"/"+name+".jpg")

            #ecoding img
            dog_face_img = cv2.imread(img)
            dets_locations = face_locations(dog_face_img, 1)
            face_encoding = face_recognition.face_encodings(dog_face_img, dets_locations)[0]

            #로컬에 기록
            with open(dir+"/"+name+".txt", "w") as f:
                f.write(face_encoding)

            #session
            old_encodings = []
            old_names = []
            if not('known_face_encodings' in session & 'known_face_name' in session):
                session['known_face_encodings'] = []
                session['known_face_name'] = []
            else :  #로컬에 저장했다가 세션으로 불러옴
                old_encodings = session['known_face_encodings']
                old_names = session['known_face_name']
        
            
            old_encodings.append(face_encoding)
            old_names.append(name)

            session['known_face_encodings'] = old_encodings
            session['known_face_name'] = old_names
        return "good"
    
    @app.route('/check', methods=['POST'])
    def check_registed_dog():
        ans = "no"



        return ans

    return app


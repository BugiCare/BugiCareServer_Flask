from flask import Flask, jsonify, request

from PIL import Image
import json
from io import BytesIO
import base64
import cv2
import torch
import numpy as np
import requests, json

from gtts import gTTS
import speech_recognition as sr
import playsound

model = torch.hub.load('ultralytics/yolov5', 'custom', path='/home/ubuntu/BugiCareServer_Flask/last.pt', force_reload = True)

temp = base64.b64encode(cv2.imencode('.jpg', cv2.imread('test.jpg'))[1]).decode()

def speak(text):
    tts = gTTS(text=text, lang='ko')
    filename='ttsWAV.wav'
    tts.save(filename)  # 음성 파일 저장
    playsound.playsound(filename)   # 음성 파일 출력

app = Flask(__name__)

image = base64.b64encode(cv2.imencode('.jpg', cv2.imread('test.jpg'))[1]).decode()

@app.route("/sendImage", methods = ["POST"])
def receiveImage():
    # 이미지 데이터 받기
    img_encoded = np.fromstring(request.data, np.uint8)

    # 인코딩된 이미지 디코딩
    img = cv2.imdecode(img_encoded, cv2.IMREAD_UNCHANGED)

    result = model(img)
    print(result)

    return {'result', 'success'}

@app.route("/image", methods = ["POST"])
def image():
    file = request.files['file']
    img_str = file.read()
    img_data = base64.b64decode(img_str)
    img_np = np.frombuffer(img_data, np.uint8)
    global temp
    temp = base64.b64encode(cv2.imencode('.jpg', img_np)[1]).decode()
    img = cv2.imdecode(img_np, cv2.IMREAD_COLOR)

    cv2.imwrite('received.jpg', img)
    result = model(img)
    
    headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
    data = {'result', result}
    #response = requests.post('http://15.164.7.163:8080/result', data=data)

    return 'ok'

@app.route("/cctv", methods = ["GET"])
def cctv():
    print(type(temp))
	img_dict = {'img': temp}
	img_json = json.dumps(img_dict)
	headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
	
	return img_json

@app.route("/tts", methods = ["POST"])
def tts():
    a = request.form.get('name')
    print(a)	# Flask 서버로 잘 넘어왔는지 확인
    speak(a)	# tts 함수로 텍스트를 넘겨 스피커로 출력하게 함
    return f'{a}'  # 확인용 반환값. 입력한 값 그대로 반환

if __name__ == "__main__":
	app.debug = True
	app.run(host = "0.0.0.0", port = 5000)

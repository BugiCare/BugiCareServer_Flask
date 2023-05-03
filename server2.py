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
import matplotlib.pyplot as plt
from PIL import Image


model = torch.hub.load('ultralytics/yolov5', 'custom', path='/home/ubuntu/BugiCareServer_Flask/last.pt', force_reload = True)

def speak(text):
    tts = gTTS(text=text, lang='ko')
    filename='ttsWAV.wav'
    tts.save(filename)  # 음성 파일 저장
    playsound.playsound(filename)   # 음성 파일 출력

app = Flask(__name__)

@app.route("/image", methods = ["POST"])
def image():
    file = request.files['file']
    img_str = file.read()
    img_data = base64.b64decode(img_str)
    img_np = np.frombuffer(img_data, np.uint8)
    img = cv2.imdecode(img_np, cv2.IMREAD_COLOR)

    cv2.imwrite('received.jpg', img)
    result = model(img)
    print(result)

    if img is None:
        print('Image load failed')
        sys.exit()

   # cv2.imshow('YOLO', np.squeeze(result.render()))
    # 이미지 디스플레이
    #plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    #plt.show()
    # PIL 이미지 객체 생성
    pil_img = Image.fromarray(img)

    # 이미지 디스플레이
    pil_img.show()

    temp_dict = {'text': result}
    #temp_json = json.dumps(temp_dict)
    headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}

    return "zz"

@app.route("/image2", methods = ["GET"])
def image2():
	img = cv2.imread('test.jpg')
	img_str = base64.b64encode(cv2.imencode('.jpg', img)[1]).decode()
	img_dict = {'img': img_str}
	img_dict = json.dumps(img_dict)
	headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
	
	return img_dict

@app.route("/tts", methods = ["POST"])
def tts():
    a = request.form.get('name')
    print(a)	# Flask 서버로 잘 넘어왔는지 확인
    speak(a)	# tts 함수로 텍스트를 넘겨 스피커로 출력하게 함
    return f'{a}'  # 확인용 반환값. 입력한 값 그대로 반환

if __name__ == "__main__":
	app.debug = True
	app.run(host = "0.0.0.0", port = 5000)

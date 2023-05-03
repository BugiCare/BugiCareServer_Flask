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

def speak(text):
    tts = gTTS(text=text, lang='ko')
    filename='ttsWAV.wav'
    tts.save(filename)  # 음성 파일 저장
    playsound.playsound(filename)   # 음성 파일 출력

app = Flask(__name__)

@app.route("/image", methods = ["POST"])
def image():
    img_str = request.data
    img_bytes = img_str.decode()
    img_decoded = base64.b64decode(img_bytes)
    img_array = np.frombuffer(img_decoded, dtype=np.uint8)
    print(img_array)
    img = cv2.imdecode(img_array, cv2.IMREAD_UNCHANGED)
    result = model(img)
    print(result)

    #cv2.imwrite('received_image.jpg', img, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
    
    temp_dict = {'text': result}
    temp_json = json.dumps(temp_dict)
    headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}

    return temp_json

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

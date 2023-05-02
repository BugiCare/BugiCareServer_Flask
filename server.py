from flask import Flask, jsonify, request

from PIL import Image
import json
from io import BytesIO
import base64
import cv2

from gtts import gTTS
import speech_recognition as sr
import playsound

def speak(text):

    tts = gTTS(text=text, lang='ko')

    filename='ttsWAV.wav'

    tts.save(filename)  # 음성 파일 저장

    playsound.playsound(filename)   # 음성 파일 출력

app = Flask(__name__)

@app.route("/image", methods = ["POST"])
def image():
	json_data = request.json

	img = json_data['img'] # str
	img_bytes = img.encode('ascii')
	img_base64 = base64.b64encode(img_bytes)

	print(img_base64)
	print(type(img_base64))
	return img_base64

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
    
# tts API를 위해 host와 port 임시 변경. 나중에 AWS와 Flask 연결 유무에 따라 host 변경
# if __name__ == "__main__":
# 	app.debug = True
# 	app.run(host = "127.0.0.1", port = 5001)

if __name__ == "__main__":
	app.debug = True
	app.run(host = "0.0.0.0", port = 80)

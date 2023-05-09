from flask import Flask, jsonify, request

from io import BytesIO
import base64
import cv2
import torch
import numpy as np
import requests, json

# YOLO model
model = torch.hub.load('ultralytics/yolov5', 'custom', path='/home/ubuntu/BugiCareServer_Flask/last.pt', force_reload = True)
# 라즈베리파이에서 온 이미지를 저장하는 변수
temp = base64.b64encode(cv2.imencode('.jpg', cv2.imread('test.jpg'))[1]).decode()

app = Flask(__name__)

@app.route("/image", methods = ["POST"])
def image():
    # 전달된 이미지 decode
    file = request.files['file']
    img_str = file.read()
    img_data = base64.b64decode(img_str)
    img_np = np.frombuffer(img_data, np.uint8)
    img = cv2.imdecode(img_np, cv2.IMREAD_UNCHANGED)

    # 전달된 이미지 크기 줄이기
    img_resized = cv2.resize(img, (int(img.shape[1]*0.5), int(img.shape[0]*0.5)))

    # 이미지 temp 변수에 저장
    global temp
    temp = base64.b64encode(cv2.imencode('.jpg', img_resized)[1]).decode()

    # 이미지 저장 후, 모델을 통해 결과 받기
    cv2.imwrite('received.jpg', img)
    result = model(img)
    print(result)
    
    # 결과값 스프링부트로 전달
    data = {'result' : str(result)}
    requests.post('http://15.164.7.163:8080/result', json=data)

    return 'ok'

@app.route("/cctv", methods = ["GET"])
def cctv():
    global temp
    img_dict = {'img': temp}
    img_json = json.dumps(img_dict)
    headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
	
    return img_json

if __name__ == "__main__":
	app.debug = True
	app.run(host = "0.0.0.0", port = 5000)

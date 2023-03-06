from flask import Flask, jsonify, request

from PIL import Image
import json
from io import BytesIO
import base64
import cv2

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

if __name__ == "__main__":
	app.debug = True
	app.run(host = "127.0.0.1", port = 5001)

import requests
import json
import base64
import cv2
from PIL import Image
import io

image_name = 'test.jpg'
img = cv2.imread(image_name)
jpg_img = cv2.imencode('.jpg', img)
b64_string = base64.b64encode(jpg_img[1]).decode('utf-8')

files = {
	"img" : b64_string
}

r = requests.post("http://127.0.0.1:5001/image", json=files)
img_bytes_str = r.text
img_bytes = bytes(img_bytes_str, 'ascii')
print(img_bytes)
print(type(img_bytes))
decoded_img = base64.decodebytes(img_bytes)

img_stream = io.BytesIO(decoded_img)
img_file = Image.open(img_stream)

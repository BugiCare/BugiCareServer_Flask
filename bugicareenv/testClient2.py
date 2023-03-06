import cv2
import json
import requests
import base64
import numpy as np

r = requests.get('http://127.0.0.1:5001/image2')
print(type(r.json())) # dict
data = r.json()
data = base64.b64decode(data['img'])
jpg_arr = np.frombuffer(data, dtype=np.uint8)
img = cv2.imdecode(jpg_arr, cv2.IMREAD_COLOR)
print(img.shape)

import requests

files = open('iamge.png', 'rb')
upload = {'file': files}
res = requests.post('http://127.0.0.1:5000/image/', files = upload)

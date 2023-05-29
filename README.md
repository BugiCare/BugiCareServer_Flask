# 👵🏻 BugiCareServer_Flask 🤖

> 2023 HSU Capstone AI를 활용한 어르신 돌봄 시스템 - Bugicare의 Flask Server입니다.

</br>

## ✔️ GUIDES

AWS의 ubuntu 환경에서 실행하였습니다. server.py 실행 시 에러가 발생한다면 요구하는 라이브러리들을 sudo pip3 install "이름"을 통해 설치하면 됩니다.

```shell
$git clone https://github.com/BugiCare/BugiCareServer_Flask.git
$cd BugiCareServer_Flask
$sudo python3 server.py
```

</br>

## ✏️ API

##### http://3.36.218.186:5000/image

- 라즈베리파이에서 보낸 사진 수신
- 모델 입력 값에 사진을 넣어 얻은 결과를 스프링부트로 전송

##### http://3.36.218.186:5000/cctv

- 라즈베리파이로부터 온 사진 중 가장 최근 사진 반환

</br>

## 🕗 VERSION

- Python 3.10.6
- Flask 2.3.2
- Pillow 9.5.0

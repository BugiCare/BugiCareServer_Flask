# BugiCareServer_Flask

> 2023 HSU Capstone AI를 활용한 어르신 돌봄 시스템 Bugicare의 Flask Server입니다.

</br>

## ✔️ GUIDES

AWS의 ubuntu 환경에서 실행하였습니다.

```shell
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

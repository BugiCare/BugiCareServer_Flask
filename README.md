### 🍒 실행 방법

------

1. 가상환경 실행
   1. bugicareenv/bin으로 이동
   2. source activate -> 쉘 뜨는거 앞에 bugicareenv라고 뜨면서 가상환경 실행된 것을 볼 수 있다.
2. 서버 실행
   1. bugicareenv로 이동
   2. python server.py
3. testClient2 테스트
   1. 새로운 터미널 창에서 bugicareenv/testClient2를 실행

</br>

### 📍코드

------

- server.py
  - http://127.0.0.1:5001/image
    - 테스트 용이니 무시
  - http://127.0.0.1:5001/image2
    - get 요청이 들어오면 'test.jpg' response
    - 딕셔너리가 반환되는 듯..합니다?
- testClient.py
  - 테스트 용이니 무시
- testClinet2.py
  - http://127.0.0.1:5001/image2 로 get 요청
  - 제대로 받았는지 테스트하기 위해 shape 출력
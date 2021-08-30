# practice_fastapi
Fast API연습 레포

## requirments
pip install pororo, fastapi[all]


# 도커 컨테이너 애플리케이션 외부에 노출하기
따로 설정을 하지 않는다면 도커가 설치된 호스트에서만 컨테이너 내부의 애플리케이션에 접근할 수 있습니다. 
외부 접속을 가능하게 하려면 컨테이너의 IP와 포트를 호스트의 IP와 포트에 바인딩해주어야 합니다.

## 1. 컨테이너 띄우기
```shell
$ docker run -it --name (하고싶은 이름) -p (호스트의 포트):(컨테이너의 포트) (도커 이미지)  
```
예시)
```shell
$ docker run -it --name mycontainer -p 1234:2222 myimage
$ docker run -it --name mycontainer -p 192.168.0.1:1234:2222 myimage
```
-p 옵션을 여러번 사용하여 여러개의 포트를 개방할수도 있습니다. 또한 호스트의 특정 IP와 바인딩 할 수 있습니다.


## 2. 컨테이너에서 서버띄우기
1.에서 **바인딩한 컨테이너의 포트**에 서버를 띄워주어야 합니다. FastAPI로 만든 서버로 예시를 들면 다음과 같습니다.
```shell
$ uvicorn main:app --reload --port 2222 --host 0.0.0.0
```

이러한 설정이 완료되고 호스트의 포트를 외부 포트에 바인딩해주면 최종적으로 외부접속이 가능하게 됩니다.
호스트의 1234번 포트로 접속 → 1234번 포트는 컨테이너의 2222번 포트로 포워딩 → 서버 접근
![](/image/port_forwarding.png)



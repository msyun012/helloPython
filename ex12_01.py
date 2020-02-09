import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mysock.connect(('data.pr4e.org',80))

##  encode()  UTF-8 으로 encoding
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()

mysock.send(cmd)

while True:

    ##  (512)  전달받는 최대 글자 수 지정
    data = mysock.recv(512)

    # 문장 끝인지 확인, 아래 조건절이 없으면 무한루프를 돔
    if (len(data) < 1):
       break

    print(data.decode())

mysock.close()

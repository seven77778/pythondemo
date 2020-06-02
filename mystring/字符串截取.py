str = "request data: b'GET /?room=0102180&begin=1912381638&end=1912381638 HTTP/1.1\r\nHost: localhost:8000\r\nConnection: Keep-Alive\r\nUser-Agent: Apache-HttpClient/4.5.2 (Java/1.8.0_201)\r\nAccept-Encoding: gzip,deflate\r\n\r\n'";

print(str[27:34])
print(str[41:51])
print(str[56:66])
room = str[27:34]
begin = str[27:34]
end = str[56:66]
print(room)
if room.isdigit() & begin.isdigit() & end.isdigit():
    print(123)
else:
    print("ggg")

if ("room" in str) & ("begin" in str):
    print("sdss")
else:
    print("333")

if ("room" in str) & ("begin" in str) & ("end" in str):
        print("222")
        room = str[27:34]
        begin = str[27:34]
        end = str[56:66]
        print("room-" + str[27:34])
        print("begin-" + str[41:51])
        print("end-" + str[56:66])

        # 构造响应数据
        response_start_line = "HTTP/1.1 200 OK\r\n"
        response_headers = "Server: My server\r\n"
        # 调用dll
        print(room)
        if (room.isdigit() & begin.isdigit() & end.isdigit()):
            print(11111)

            if 1==1:
                print("hahaha")
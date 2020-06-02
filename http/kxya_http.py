#-.- coding:utf-8 -.-

from http.server import  HTTPServer
import ctypes
from ctypes import *
# HTTPRequestHandler class
import http.server
import socketserver
import logging
# pyinstaller -F
class testHTTPServer_RequestHandler(http.server.BaseHTTPRequestHandler):
    # GET
  def do_GET(self):
        logging.error('start make ')
        str2 =  str(self.path)
        print("revice： " + str2)
        if ("room" in str2) & ("begin" in str2) & ("end" in str2):
            print("get room")
            room = str2[7:14]
            begin = str2[21:31]
            end = str2[36:46]
            print("room-" + room)
            print("begin-" + begin)
            print("end-" + end)

            # 调用dll
            if (room.isdigit() & begin.isdigit() & end.isdigit()):
                print("makecard")
                logging.error('makecard')
                dll = ctypes.windll.LoadLibrary('C:\\xxx\\xxx.dll')
                print("dll version ： " + str(dll.GetVersion()))
                name = ctypes.c_char_p(b"gc")
                roomno = ctypes.c_char_p(bytes(room.encode("utf-8")))
                begintime = ctypes.c_char_p(bytes(begin.encode("utf-8")))
                endtime = ctypes.c_char_p(bytes(end.encode("utf-8")))
                cardno = ctypes.c_void_p(0)
                print("data open:" + str(dll.OpenDatabase("", "")))
                logging.error("database open:" + str(dll.OpenDatabase("", "")))
                response_body = dll.WriteGuestCard2(name,bytes(0),roomno,begintime,endtime,byref(cardno))
                print("invoke dll  " +  str(response_body))
                logging.error("invoke dll  " +  str(response_body))
                # response_body = "0"
                print("data close:" + str(dll.CloseDatabase()))
                self.send_response(200)

                # Send headers
                self.send_header('Content-type','text/html')
                self.end_headers()

                # Send message back to client
                message = "Hello world!"
                # Write content as utf-8 data
                self.wfile.write(bytes(str(response_body), "utf8"))


                return

def run():
  print('starting server...')
  logging.basicConfig(
      level=logging.INFO,
      format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
      filename="http_make_card.txt",
      filemode='a+'
  )
  # Server settings
  # Choose port 8080, for port 80, which is normally used for a http server, you need root access
  server_address = ('127.0.0.1', 8000)
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
  print('running server...')
  httpd.serve_forever()




run()

print("success")


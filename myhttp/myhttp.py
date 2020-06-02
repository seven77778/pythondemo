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
        if "xxx" in str2:
            # todo 你的具体业务操作
            print("in")
            room = str2[7:14]
            begin = str2[21:31]
            end = str2[36:46]
            print("room-" + room)
            print("begin-" + begin)
            print("end-" + end)
            if (room.isdigit() & begin.isdigit() & end.isdigit()):
                print("hahaha")
                logging.error('hahaha')
                # response_body = "0"
                self.send_response(200)
                # Send headers
                self.send_header('Content-type','text/html')
                self.end_headers()
                # Send message back to client
                message = "Hello world!"
                # Write content as utf-8 data
                self.wfile.write(bytes(message, "utf8"))
                return
        else:
            print("1else")
            self.send_response(200)
            # Send headers
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            # Send message back to client
            message = "Hello world222333!"
            # Write content as utf-8 data
            self.wfile.write(bytes(message, "utf8"))
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
  server_address = ('127.0.0.1', 8888)
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
  print('running server...')
  httpd.serve_forever()

run()


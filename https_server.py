import BaseHTTPServer
import SimpleHTTPServer
import ssl
import sys


if __name__ == "__main__":
  httpd = BaseHTTPServer.HTTPServer(
    ('127.0.0.1', int(sys.argv[1])),
    SimpleHTTPServer.SimpleHTTPRequestHandler)

  httpd.socket = ssl.wrap_socket(
    httpd.socket,
    certfile='server.pem',
    server_side=True)

  httpd.serve_forever()
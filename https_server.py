import socket
import ssl
import sys
import SimpleHTTPServer
from BaseHTTPServer import HTTPServer

class HTTPServerV6(HTTPServer):
  address_family = socket.AF_INET6

if __name__ == "__main__":
  httpd = HTTPServerV6(
    ('', int(sys.argv[1])),
    SimpleHTTPServer.SimpleHTTPRequestHandler)

  httpd.socket = ssl.wrap_socket(
    httpd.socket,
    certfile='server.pem',
    server_side=True)

  httpd.serve_forever()


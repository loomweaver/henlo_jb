#!/usr/bin/env python2

import socket
import SocketServer, SimpleHTTPServer

localIP = "192.168.0.123"
PORT = 8888

print "Starting server on " + localIP + ":" + str(PORT)

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
server = SocketServer.TCPServer(('', PORT), Handler)
server.serve_forever()

#!/usr/bin/env python3

import socket
import socketserver, http.server

localIP = "192.168.0.123"
PORT = 8888

print("Starting server on " + localIP + ":" + str(PORT))

Handler = http.server.SimpleHTTPRequestHandler
server = socketserver.TCPServer(('', PORT), Handler)
server.serve_forever()

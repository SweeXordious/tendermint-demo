#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import json

PORT_NUMBER = 8080

class JudgeHandler(BaseHTTPRequestHandler, object):
	def do_GET(self):
		if (self.path == "/status"):
			self.send_response(200)
			self.end_headers()
			self.wfile.write(json.dumps(status_map))
		else:
			self.send_response(400)
			self.end_headers()

	def do_POST(self):
		path_components = self.path.split("/")
		if len(path_components) >= 3 and path_components[1] == "submit":
			node = path_components[2]
			status_json = self.rfile.read(int(self.headers.getheader("Content-Length")))
			status_map[node] = json.loads(status_json)

			self.send_response(200)
			self.end_headers()
		else:
			self.send_response(400)
			self.end_headers()

	def log_message(self, format, *args):
		return

try:
	status_map = {}

	server = HTTPServer(("", PORT_NUMBER), JudgeHandler)
	print "the Judge server started on port", PORT_NUMBER
	
	server.serve_forever()
except KeyboardInterrupt:
	print "^C received, shutting down the Judge"
	server.socket.close()
	
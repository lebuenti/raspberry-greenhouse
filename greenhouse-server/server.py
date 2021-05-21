#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
from urllib.parse import urlparse
from fuzzyctrl import FuzzyCtrl

class Server(BaseHTTPRequestHandler):
    fuzzyctrl = FuzzyCtrl()

    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        query = urlparse(self.path).query
        query_components = dict(qc.split("=") for qc in query.split("&"))
        plant_name = query_components["plantName"]
        self.fuzzyctrl.something(plant_name)    
        self._set_response()
        self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=Server, port=8080):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    server = server_class(server_address, handler_class)
    logging.info('Starting server on localhost with port ' + str(port) + '\n')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    server.server_close()
    logging.info('Stopping server...\n')

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()

#!/usr/bin/env python
"""
Very simple HTTP server in python.
Usage::
    ./dummy-web-server.py [<port>]
Send a GET request::
    curl http://localhost
Send a HEAD request::
    curl -I http://localhost
Send a POST request::
    curl -d "foo=bar&bin=baz" http://localhost
"""
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from parser import Parser
import json


class S(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_POST(self):
        if self.path == '/wordcount':
            print("incoming http: ")
            try:
                content_length = int(self.headers['Content-length'])
                post_data = self.rfile.read(content_length)
                count = self.fetch_count(post_data)
                self.wfile.write(count)
                self._set_headers()
            except Exception as e:
                print("error occurred: " + str(e))
                self._set_headers()
                self.send_response(400)

    @staticmethod
    def fetch_count(data):
        params = {}
        print('incoming data', data)
        js = json.loads(data)
        for key in js:
            if key == "word" or key == "url":
                params[key] = js[key]
        p = Parser()
        count = p.parse(params['url'], params['word'])
        data = {"status": "ok", "count": count}
        return data


def run(server_class=HTTPServer, handler_class=S, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()

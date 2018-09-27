#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test application for labwork.
Environment variables:
LISTEN_PORT (default: 80)
"""
import re   # for using of regular expressions
import logging  # best-practices of python logging
from os import getenv   # method gets environment vars from system
from http.server import BaseHTTPRequestHandler, HTTPServer  # classes for creation of wev server

class Server(BaseHTTPRequestHandler):
    def do_POST(self):
        '''
        Automaticaly called in case of POST request.
        :return: 
        '''
        self.new_request()
        pass

    def do_GET(self):
        '''
        Automaticaly called in case of GET request.
        :return: 
        '''
        self.new_request()
        pass

    def new_request(self):
        try:
            # Send response status code
            self.send_response(200)
            # Send headers
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            # Create html code
            self.wfile.write(bytes(self.prepare_html(), "utf8"))
        except Exception as e:
            logging.error('cannot send answer: {0}', str(e))

    def prepare_html(self) -> str:
        '''
        Creates HTML code basing on base.html
        :return: html code
        '''
        html = ''
        # read html template
        with open('base.html', 'rt') as f:
            html = f.read()
        # replace substr '!!hostname!!' with value of environment variable
        html = re.sub('!!hostname!!', getenv('HOSTNAME', 'somewhere =\\'), html)
        return html


def main():
    '''
    Simply starts web server.
    :return:
    '''
    ip = '0.0.0.0' # listeninng all interfaces
    port = getenv('LISTEN_PORT', 80)    # getting var with port number to listen on, if did not set - use 80
    server_address = (ip, int(port))    # just creation of tuple
    # starting and serving forever
    httpd = HTTPServer(server_address, Server)  # starting server
    logging.info('Listenning requests on {0}:{1}'.format(ip, port)) # logging msg about successful start
    httpd.serve_forever()   # infinite loop with spawning of subthreads on each request
    pass


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO) # saying that all logging messages except DEBUG should be printed to stdout
    try:
        main()  # calling main entrypoint function
    except Exception as e:
        logging.error('all crashed: {0}', str(e))

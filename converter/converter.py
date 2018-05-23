from http import client, server
from lib.requests import api as requests
import socketserver
import os
import threading


class WebServerThread(threading.Thread):
    def __init__(self):
        super(WebServerThread, self).__init__()
        self.web_server = None

    @staticmethod
    def create_socketserver():
        return socketserver.TCPServer(('', 8000),
                                      server.SimpleHTTPRequestHandler)

    def run(self):
        script_dir = os.path.dirname((os.path.realpath(__file__)))
        os.chdir(os.path.join(script_dir, '..', 'tool'))
        self.web_server = self.create_socketserver()
        self.web_server.serve_forever()


web_server_thread = WebServerThread()
web_server_thread.start()

request = requests.get('http://localhost:8000')

pass

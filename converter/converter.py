from http import server
import socketserver
import os

PORT = 8000

webserver = socketserver.TCPServer(('', 8000),
                                   server.SimpleHTTPRequestHandler)
script_dir = os.path.dirname((os.path.realpath(__file__)))
os.chdir(os.path.join(script_dir, '..', 'tool'))
print(os.getcwd())

webserver.serve_forever()

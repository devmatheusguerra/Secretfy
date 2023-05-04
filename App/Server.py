from flask import Flask
from flask import render_template, request
import platform
from time import sleep as wait
from os import system
import os
from json import dumps, loads
from src.Cript import Cript
from src.Database import Database
import _thread
class Server:
    def __init__(self):
        app = Flask(__name__)
        @app.route("/")
        def main():
            return render_template('index.html')
        
        @app.route("/files", methods=['get'])
        def index():
            return dumps(Database('info.db').get_all())
        
        @app.route("/files", methods=['post'])
        def store():
            try:
                file = request.files['file']
                print(file.filename)
                file.save('./resources/' + file.filename)
                Cript.encrypt('./resources/' + file.filename)
                # Remove the original file
                os.remove('./resources/' + file.filename)
                # Status 201: Created
                return '', 201
            except Exception as e:
                return dumps({
                    'error': str(e)
                }), 400
                        
        @app.route("/files/<id>/download", methods=['get'])
        def download(id):
            data = Database('info.db').get(id)
            if data == None:
                return dumps({
                    'error': 'File not found'
                }), 404
            file = Cript.decrypt('./resources/' + data['hashable_file'])
            header = {
                'Content-Type': 'application/octet-stream',
                'Content-Disposition': 'attachment; filename=' + data['original_file']
            }

            response = app.response_class(
                response=file,
                status=200,
                mimetype='application/octet-stream',
                headers=header
            )
            return response

        @app.route("/files/<id>/delete", methods=['delete'])
        def delete(id):
            data = Database('info.db').get(id)
            if data == None:
                return dumps({
                    'error': 'File not found'
                }), 404
            
            Database('info.db').delete(id)
            return '', 200
        
        print('Server is starting...')

        _thread.start_new_thread(self.open, ())


        app.run(host='127.0.0.1', port=8082)

    def open(self):
        wait(1)
        if platform.system() == 'Windows':
            system('start http://127.0.0.1:8082/')
        elif platform.system() == 'Linux':
            system('xdg-open http://127.0.0.1:8082/')
        elif platform.system() == 'Darwin':
            system('open http://127.0.0.1:8082/')

    
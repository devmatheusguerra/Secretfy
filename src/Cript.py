from cryptography.fernet import Fernet
import os
import json
from base64 import b64encode, b64decode
import random
from time import time
from src.Database import Database

class Cript:
    @staticmethod
    def randomName():
        name = ''
        for i in range(10):
            name += chr(random.randint(97, 122))
        name += '__' + str(int(time()))
        return name
    
    @staticmethod
    def encrypt(path):
        with open(path, 'rb') as file:
            data = file.read()
            filename, fileextension = os.path.splitext(path)
            filesize = os.path.getsize(path)
            with open('./.key', 'rb') as key:
                metadata = json.dumps({
                    'name': filename,
                    'size': filesize,
                    'type': fileextension,
                    'data': b64encode(data).decode('utf-8')
                }).encode('utf-8')

                f = Fernet(key.read())
                data = f.encrypt(metadata)
                randomName = Cript.randomName()
                with open('./resources/' + randomName, 'wb') as file:
                    file.write(data)
                    Database('./info.db').insert(path.split('/')[-1], randomName)


    @staticmethod
    def decrypt(path):
        with open(path, 'rb') as file:
            with open('./.key', 'rb') as key:
                f = Fernet(key.read())
                data = f.decrypt(file.read())
                data = json.loads(data.decode('utf-8'))
                return b64decode(data['data'].encode('utf-8'))
    


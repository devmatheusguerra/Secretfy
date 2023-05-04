import os.path
from getpass import getpass
from json import dumps, loads
from base64 import b64encode, b64decode
import cryptography
from cryptography.fernet import Fernet
import hashlib
import random

from src.Files import Files

if os.path.isfile('./.data'):
    file = Files('.data')
    data = loads(b64decode(file.read().decode('utf-8')).decode('utf-8'))
    first_pass = data['p1']
    second_pass = data['p2']
    third_pass = data['p3']
    t1 = getpass('')
    t2 = getpass('')
    t3 = getpass('')

    if t1 == first_pass and t2 == second_pass and t3 == third_pass:
        from App.Server import Server
        Server()

else:
    first_pass = str(int(input('Type the first password: ')))
    second_pass = str(int(input('Type the second password: ')))
    third_pass = str(int(input('Type the last password: ')))
    data = {
        "p1":first_pass,
        "p2":second_pass,
        "p3":third_pass
    }
    data = b64encode(dumps(data).encode('utf-8'))    
    F1 = Files('.data')
    F1.write(data)

        


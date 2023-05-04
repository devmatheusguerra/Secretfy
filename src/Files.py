from cryptography.fernet import Fernet
import os.path
class Files:
    def __init__(self, path):
        self.path = path
        if os.path.isfile('.key'):
            with open('.key', 'rb') as file:
                self.key = file.read()
            self.f = Fernet(self.key)
        else:
            key = Fernet.generate_key()
            with open('.key', 'wb') as file:
                file.write(key)
            self.f = Fernet(key)

    def read(self):
        with open(self.path, 'rb') as file:
            data = file.read()
        return self.f.decrypt(data)
    
    def write(self, data):
        data = self.f.encrypt(data)
        with open(self.path, 'wb') as file:
            file.write(data)

    def exists(self):
        return os.path.isfile(self.path)
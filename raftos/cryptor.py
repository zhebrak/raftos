import base64

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

from .conf import config


class Cryptor:
    def __init__(self):
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=config.salt,
            iterations=100000,
            backend=default_backend()
        )
        self.f = Fernet(base64.urlsafe_b64encode(kdf.derive(config.secret_key)))

    def encrypt(self, data):
        return self.f.encrypt(data)

    def decrypt(self, data):
        return self.f.decrypt(data)


cryptor = Cryptor()

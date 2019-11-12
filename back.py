from hashlib import sha3_512, md5
from Crypto.Cipher import AES, _mode_cbc
from dbm import open
from pickle import loads, dumps


class crypto:
    def sencrypt(self, dat):
        return sha3_512(dat).hexdigest()
    def encrypt(self, dat, key, iv):
        keyd = md5(key).hexdigest()
        iv = list(iv)
        if len(iv) != 16:
            ilen = len(iv) - 16
            if ilen < 0:
                iv = iv + "0"*ilen
            else:
                del iv[ilen:]
        iv = "".join(iv)
        enc = AES.new(keyd, _mode_cbc, iv)
        return {"enc":enc, "key":keyd, "iv":iv}
    def decrypt(self, dat, key, iv):
        keyd = md5(key).hexdigest()
        dec = AES.new(keyd, _mode_cbc, iv)
        decd = dec.decrypt(dat)
        return decd

class data:
    def add(self, dat1, dat2):
        with open('dat.db', 'c') as db:
            db[dat1] = dumps(dat2)
    def remove(self, dat):
        with open('dat.db', 'c') as db:
            del db[dat]
    def update(self, dat1, dat2):
        try:
            with open('dat.db', 'w') as db:
                db[dat1] = dat2
        except FileNotFoundError:
            print("DATABAsE NOT FOUND!!!")
    def view(self,dat):
        try:
            with open('dat.db', 'r') as db:
                return loads(db[dat])
        except FileNotFoundError:
            print("DATABAsE NOT FOUND!!!")
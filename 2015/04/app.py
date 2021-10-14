import hashlib

class Md5Miner:
    def __init__(self, secret_key):
        self.secret_key = secret_key
        self.answer = 0

    def mine(self):
        while True:
            current_key = self.secret_key + str(self.answer)
            md5 = hashlib.md5(current_key.encode())
            md5_hash = md5.hexdigest()
            if md5_hash[0:5] == '00000':
                return self.answer
            self.answer += 1

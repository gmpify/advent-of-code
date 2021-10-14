import hashlib
import re

class Md5Miner:
    def __init__(self, secret_key):
        self.secret_key = secret_key

    def mine(self, zeros = 5):
        answer = 0
        while True:
            current_key = self.secret_key + str(answer)
            md5 = hashlib.md5(current_key.encode())
            md5_hash = md5.hexdigest()
            if re.match(rf"0{{{zeros}}}", md5_hash):
                return answer
            answer += 1

if __name__ == '__main__':
    miner = Md5Miner('ckczppom')
    print('The answer is: ', miner.mine())

    print('The second part answer is: ', miner.mine(6))

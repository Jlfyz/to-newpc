import datetime
import hashlib
import json


class Block:
    nonce = 0

    def __init__(self, index, data, privious_hash=''):
        self.data = data
        self.index = index
        self.timestamp = datetime.datetime.now()
        self.privious_hash = privious_hash
        self.hash = self.give_block_hash()
        self.nonce = 0

    def give_block_hash(self):
        h = hashlib.sha256()
        h.update(
            str(self.index).encode('utf-8')+
            str(self.privious_hash).encode('utf-8')+
            str(self.timestamp).encode('utf-8')+
            str(json.dumps(self.data)).encode('utf-8')+
            str(self.nonce).encode('utf-8')
        )
        return h.hexdigest()

    def log_block(self):
        print('Block number = '+str(self.index))
        print('Block hash = '+str(self.hash))
        print('Block privious hash = '+str(self.privious_hash))
        print('Block\'s timestamp = '+str(self.timestamp))
        print('------------------')

    def mine_block(self, difficulty):
        string = '0'*difficulty
        while self.hash[:difficulty] != string:
            self.nonce += 1
            self.hash = self.give_block_hash()


def main():
    genesis_block = Block(1, '', '0000')
    genesis_block.log_block()


if __name__ == '__main__':
    main()

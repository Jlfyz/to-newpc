import block


class Blockchain:

    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.counter = 0
        self.difficulty = 5

    def create_genesis_block(self):
        return block.Block(0, 'Genesis block', '0')

    def get_the_latest_block(self):
        return self.chain[self.counter]

    def add_new_block(self, new_block):
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)
        self.counter += 1


def main():
    blockchain = Blockchain()
    for i in range(10):
        z = block.Block(i+1, '{ ammount: 4 }', blockchain.get_the_latest_block().hash)
        blockchain.add_new_block(new_block=z)
        z.log_block()


if __name__ == '__main__':
    main()


class Configs():
    def __init__(self):
        self.BOARD_COLS = 10
        self.BOARD_ROWS = 10
        self.POLICIES_DIR = './policies'
        self.lr = 0.2
        self.decay_gamma = 0.9 #how rapidly the values change
        self.exp_rate = 0.9 #how much randomness
#below seems like a good value to never lose.
        self.training_epoch = 15000 # the amount of rounds
#        self.training_epoch = 10000
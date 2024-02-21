import random

import numpy as np

from configs import Configs


class State():
    def __init__(self, p1):
        self.configs = Configs()
        self.BOARD_COLS = self.configs.BOARD_COLS
        self.BOARD_ROWS = self.configs.BOARD_ROWS
        self.POLICIES_DIR = self.configs.POLICIES_DIR
        #        self.POLICIES_DIR = self.configs.POLICIES_DIR

        self.p1 = p1
        #self.score = 0
        self.board = np.zeros((self.BOARD_ROWS, self.BOARD_COLS))
        self.mines = [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0],#0
                      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],#1
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#2
                      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],#3
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#4
                      [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],#5
                      [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],#6
                      [0, 0, 0, 0, 1, 0, 0, 1, 1, 0],#7
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#8
                      [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]]#9
                      #0 #1 #2 #3 #4 #5 #6 #7 #8 #9
        self.nums = [[2,-1, 1, 0, 0, 0, 0, 0, 0, 0], #0
                     [-1, 2, 1, 0, 0, 0, 0, 0, 0, 0], #1
                     [ 2, 2, 0, 0, 0, 0, 0, 0, 0, 0], #2
                     [-1, 1, 0, 0, 0, 0, 0, 0, 0, 0], #3
                     [ 1, 1, 0, 0, 1, 2, 2, 1, 0, 0], #4
                     [ 0, 0, 0, 0, 1,-1,-1, 2, 1, 0], #5
                     [ 0, 0, 0, 1, 2, 3, 4,-1, 3, 1], #6
                     [ 0, 0, 0, 1,-1, 1, 2,-1,-1, 1], #7
                     [ 1, 1, 1, 1, 1, 1, 1, 2, 2, 1], #8
                     [ 1,-1, 1, 0, 0, 0, 0, 0, 0, 0]] #9
        self.numFlags = 10
        self.zeroArray = []
#        print(self.board)
#        print(self.board.ndim)
        self.boardHash = None
        self.isEnd = False
        self.playerSymbol = 1

    #    def getHash(self):
    #        self.boardHash = str(self.board.reshape(self.BOARD_ROWS * self.BOARD_COLS))
    #        return self.boardHash


    """def placeMines(self):
        numMines = (self.BOARD_ROWS * self.BOARD_COLS) * 0.1;
        while numMines > 0:
            arr = np.random.randint(self.BOARD_COLS, size=3)
            print(arr)
            if(arr[0] >= (self.BOARD_COLS / 2) and self.mines[arr[1],arr[2]] != 1):
                self.mines[arr[1],arr[2]] = 1
                numMines -= 1

        for i in range(self.BOARD_ROWS):
            for j in range(self.BOARD_COLS):
                num = 0
                for u in range(-1,1):
                    for o in range(-1, 1):
                        if(self.mines[(i+u),(j+o)] == 1):
                            num += 1
                self.nums[i,j] = num
        print(self.mines)
        print(self.nums)"""

    def getHash(self):
        self.boardHash = str(self.board.reshape(self.BOARD_ROWS * self.BOARD_COLS))
        return self.boardHash

    def getAvailablePositions(self):
        positions = []
        for i in range(self.BOARD_ROWS):
            for j in range(self.BOARD_COLS):
                if self.board[i][j] == 0:
                    positions.append((i, j))
        #        print(positions)
        return positions
    def getAvailablePositionsForWin(self):
        positions1 = []
        for i in range(self.BOARD_ROWS):
            for j in range(self.BOARD_COLS):
                if self.board[i][j] == 0 or self.board[i][j] == 1:
                    positions1.append((i, j))
        #        print(positions)
        return positions1

    def winner(self):
        # draw
        """if len(self.getAvailablePositions()) == 10:
            self.isEnd = True
            self.reset()
            print('game over')
            return True"""

        squares = []
        for i in range(self.BOARD_ROWS):
            for j in range(self.BOARD_COLS):
                if ((self.board[i][j] == 1 and self.mines[i][j] == 1) or (self.board[i][j] == 0 and self.mines[i][j] == 1)) and (len(self.getAvailablePositionsForWin()) <= 10):
                    squares.append((i, j))

        if len(squares) == 10:
            print(len(squares))
            self.isEnd = True
            print('You won')
            return 1
        if len(self.getAvailablePositions()) == 0:
            self.isEnd = True
            #print('you lostasas')
            return -1

        # game continues
        self.isEnd = False
        return None

    def updateStates(self, action):
        if self.board[action[0]][action[1]] == 1:
            print('a')
            return False
        elif self.mines[action[0]][action[1]] == 1:
            self.isEnd = True
            print('Game Over')
            return True
        else:
            if self.nums[action[0]][action[1]] != 0:
                self.board[action[0]][action[1]] = -1
                #print('1')
                return False
            else:
                self.clearZeroes([action[0],action[1]])
                #print('2')
                return False

    """        if (action[0] == 1):
    if (self.board[action[1]][action[2]] == 1):
        self.board[action[1]][action[2]] = 0
        self.numFlags += 1
        return False
    else:
        if self.numFlags>0:
            print(self.numFlags)
            self.board[action[1]][action[2]] = 1
            self.numFlags -= 1
            return False
        else:
            print('u ran out of flags')"""

    def clearZeroes(self, action):
        self.board[action[0]][action[1]] = -1
        self.zeroArray.append([action[0],action[1]])
        for i in range(-1,2):
            for j in range(-1,2):
                if(0 <= (action[0]+i) and (action[0]+i) < len(self.board) and 0 <= (action[1]+j) and (action[1]+j) < len(self.board)):
                    if(self.nums[action[0]+i][action[1]+j] == 0 and not([action[0]+i,action[1]+j] in self.zeroArray)):
                        self.clearZeroes([action[0]+i,action[1]+j])
                    else:
                        self.board[action[0]+i][action[1]+j] = -1


    def reset(self):
        self.board = np.zeros((self.BOARD_ROWS, self.BOARD_COLS))
        self.mines = [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # 0
                      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 1
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 2
                      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 3
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 4
                      [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],  # 5
                      [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],  # 6
                      [0, 0, 0, 0, 1, 0, 0, 1, 1, 0],  # 7
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 8
                      [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]]  # 9
        # 0 #1 #2 #3 #4 #5 #6 #7 #8 #9
        self.nums = [[2, -1, 1, 0, 0, 0, 0, 0, 0, 0],  # 0
                     [-1, 2, 1, 0, 0, 0, 0, 0, 0, 0],  # 1
                     [2, 2, 0, 0, 0, 0, 0, 0, 0, 0],  # 2
                     [-1, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # 3
                     [1, 1, 0, 0, 1, 2, 2, 1, 0, 0],  # 4
                     [0, 0, 0, 0, 1, -1, -1, 2, 1, 0],  # 5
                     [0, 0, 0, 1, 2, 3, 4, -1, 3, 1],  # 6
                     [0, 0, 0, 1, -1, 1, 2, -1, -1, 1],  # 7
                     [1, 1, 1, 1, 1, 1, 1, 2, 2, 1],  # 8
                     [1, -1, 1, 0, 0, 0, 0, 0, 0, 0]]  # 9
        self.boardHash = None
        self.isEnd = False
        self.playerSymbol = 1
        #self.score = 0

    def giveReward(self):
        """
        At game end only
        """
        result = self.winner()

        if result == 1:
            self.p1.feedReward(1)

        elif result == -1:
            print('t')
            self.p1.feedReward(0)
            #self.p1.feedReward(self.score/-10000)
            #self.score=0

    # play 2 humans
    def playGame(self, rounds=100):
        print("Initialize training for {} epochs".format(rounds))
        for i in range(rounds):
            if i % 1000 == 0:
                print('Rounds {}'.format(i))

            while not self.isEnd:
                # player 1
                positions = self.getAvailablePositions()
                p1_action = self.p1.chooseAction(positions, self.board, self.playerSymbol)
                print(p1_action)
                if (self.updateStates(p1_action)):
                    #self.p1.feedReward(self.score/-10000)
                    self.p1.feedReward(0)
                    print('u lostsds')
                    self.p1.reset()
                    self.reset()
                    break
                #self.score+=1
                #print(self.score)
                board_hash = self.getHash()
                self.p1.addStates(board_hash)

                # check if win
                winner = self.winner()
                #print('hi')
                if winner is not None:
                    print('wte')
                    self.giveReward()
                    self.p1.reset()
                    self.reset()
                    break


        print("Done training... Saving 1 policies to {}".format(self.POLICIES_DIR))
        self.p1.savePolicy(self.POLICIES_DIR)






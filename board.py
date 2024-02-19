import numpy as np

class Board(object):

    def __init__(self):
        self.pieces = np.zeros((2,6), dtype=np.uint64)

    # white = 0
    # black = 1
        
    # pawn = 1
    # knight = 2
    # bishop = 3
    # rook = 4
    # queen = 5
    # king = 6

    def get_bitboards(self):
        self.pieces[0][1] = np.uint64(0x000000000000FF00)
        self.pieces[0][2] = np.uint64(0x0000000000000042)
        self.pieces[0][3] = np.uint64(0x0000000000000024)
        self.pieces[0][4] = np.uint64(0x0000000000000081)
        self.pieces[0][5] = np.uint64(0x0000000000000008)
        self.pieces[0][6] = np.uint64(0x0000000000000010)

        self.pieces[1][1] = np.uint64(0x00FF000000000000)
        self.pieces[1][2] = np.uint64(0x4200000000000000)
        self.pieces[1][3] = np.uint64(0x2400000000000000)
        self.pieces[1][4] = np.uint64(0x8100000000000000)
        self.pieces[1][5] = np.uint64(0x0800000000000000)
        self.pieces[1][6] = np.uint64(0x1000000000000000)
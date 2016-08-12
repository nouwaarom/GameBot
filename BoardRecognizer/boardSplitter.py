class BoardSplitter:
    def __init__(self, board_size):
        self.board_size = board_size

    def get_tiles(self, board):
        tiles = [[0 for _ in range(self.board_size)] for _ in range(self.board_size)]

        for i in range(self.board_size):
            row = board[(i*50):((i+1)*50)]
            for j in range(self.board_size):
                tiles[i][j] = row[0:50, (j*50):((j+1)*50)]
        return tiles

drawing = []

with open("drawing.txt") as f:
    for e in f.readline().split(","):
        drawing.append(e)

print(drawing)


class BingoBoard:
    def __init__(self, board):
        self.board = board

    def check_Number(self, drawn_number):
        for line in self.board:
            for num in line:
                if num == drawn_number:
                    return

    def isComplete():
        return

    def sumBoard():
        return
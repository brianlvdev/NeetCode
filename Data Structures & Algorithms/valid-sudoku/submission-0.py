class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = collections.defaultdict(set)
        lin = collections.defaultdict(set)
        qua = collections.defaultdict(set)

        for l in range(9):
            for c in range(9):
                if board[l][c] == ".":
                    continue
                if (board[l][c] in lin[l] or
                    board[l][c] in col[c] or
                    board[l][c] in qua[l // 3, c // 3]):
                    return False
                col[c].add(board[l][c])
                lin[l].add(board[l][c])
                qua[(l // 3, c // 3)].add(board[l][c])
        return True
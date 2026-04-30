class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for i in range(9):
            for j in range(9):
                val = board[i][j]

                if val == '.':
                    continue

                row = ("row", val, i)
                col = ("col", val, j)
                box = ("box", val, i // 3, j // 3)

                if row in seen or col in seen or box in seen:
                    return False

                seen.add(row)
                seen.add(col)
                seen.add(box)

        return True
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_maps = [set() for _ in range(9)]
        col_maps = [set() for _ in range(9)]
        box_maps = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                num = board[row][col]
                
                if num == ".":
                    continue

                if num in row_maps[row]:
                    return False
                if num in col_maps[col]:
                    return False
                if num in box_maps[row//3 * 3 + col//3]:
                    return False

                row_maps[row].add(num)
                col_maps[col].add(num)
                box_maps[row//3 * 3 + col//3].add(num)
        
        return True
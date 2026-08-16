class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set) # row_index: row_elements
        cols = defaultdict(set) # col_index: col_elements
        boxes = defaultdict(set) #
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                num = board[i][j]

                if (num == "."):
                    continue
                
                if ((num in rows[i]) or (num in cols[j])):
                    return False
                rows[i].add(num)
                cols[j].add(num)

                if (num in boxes[(i//3, j//3)]):
                    return False
                boxes[(i//3, j//3)].add(num)
        
        return True
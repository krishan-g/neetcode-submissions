from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        
        def bfs(r, c):
            area = 1

            grid[r][c] = 0
            q = deque([(r, c)])

            directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            while q:
                x, y = q.popleft()
                for dx, dy in directions:
                    if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]):
                        if grid[x + dx][y + dy] == 1:
                            area += 1
                            q.append((x + dx, y + dy))
                            grid[x + dx][y + dy] = 0
            
            return area


        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    max_area = max(max_area, bfs(r, c))
        
        return max_area
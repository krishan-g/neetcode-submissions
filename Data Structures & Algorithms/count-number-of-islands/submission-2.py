class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "0":
                    continue

                grid[r][c] = "0"
                nodes = [(r, c)]
                while nodes:
                    x, y = nodes.pop()

                    neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
                    for neighbor in neighbors:
                        in_bounds = ((0 <= neighbor[0] < len(grid)) and
                                    (0 <= neighbor[1] < len(grid[0])))
                        if in_bounds:
                            if grid[neighbor[0]][neighbor[1]] == "1":
                                nodes.append(neighbor)
                                grid[neighbor[0]][neighbor[1]] = "0"
                
                islands += 1
        
        return islands
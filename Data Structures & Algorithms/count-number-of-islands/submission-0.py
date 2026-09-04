class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set() # tracks lands visited
        islands = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "0":
                    continue
                if (r, c) in visited:
                    continue

                nodes = [(r, c)]
                while nodes:
                    x, y = nodes.pop()
                    visited.add((x, y))

                    neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
                    for neighbor in neighbors:
                        in_bounds = ((0 <= neighbor[0] < len(grid)) and
                                    (0 <= neighbor[1] < len(grid[0])))
                        if in_bounds and neighbor not in visited:
                            if grid[neighbor[0]][neighbor[1]] == "1":
                                nodes.append(neighbor)
                
                islands += 1
        
        return islands
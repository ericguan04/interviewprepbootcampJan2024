from ast import List
import collections

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #we need to use graph algorithm breadth first search

        #return 0 for empty grid
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        #bfs is an iterative algorithm (use queues)
        def bfs(r,c):
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))

            while q:
                row, col = q.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r) in range(rows) and (c) in range(cols) and grid[r][c] == "1" and (r, c) not in visit:
                        q.append((r, c))
                        visit.add((r, c))

        #graph traversal
        for r in range(rows):
            for c in range(cols):
                #if it is a piece of land and not already visited, run bfs
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    islands += 1
        return islands
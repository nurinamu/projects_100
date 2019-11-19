from typing import List

class Solution:
    x = 0
    y = 0
    count = 0
    obstacles = 0

    def init(self) :
        self.x = 0
        self.y = 0
        self.count = 0
        self.obstacles = 0

    def findStart(self, grid: List[List[int]]) :
        for posY in range(0, len(grid)) :
            for posX in range(0, len(grid[posY])) :
                if grid[posY][posX] == 1 :
                    self.x = posX
                    self.y = posY
                elif grid[posY][posX] == -1 :
                    self.obstacles += 1

    def searchEnd(self, grid: List[List[int]], orgX:int, orgY:int, path:int) :
        if orgX < 0 or orgY < 0 or orgY >= len(grid) or orgX >= len(grid[0])  :
            return
        tmp = grid[orgY][orgX]
        if tmp == 2 :
            print("goal! {}".format(path))
            if len(grid) * len(grid[0]) - 1 - self.obstacles == path :
                self.count += 1
        elif tmp == 1 or tmp == 0 :
            grid[orgY][orgX] = 9
            #top
            self.searchEnd(grid, orgX, orgY - 1, path + 1)
            #bottom
            self.searchEnd(grid, orgX, orgY + 1, path + 1)
            #left
            self.searchEnd(grid, orgX - 1, orgY, path + 1)
            #right
            self.searchEnd(grid, orgX + 1, orgY, path + 1)
            grid[orgY][orgX] = tmp

    def uniquePathsIII(self, grid: List[List[int]]) -> int:

        self.init()
        self.findStart(grid)
        print("x:{}, y:{}".format(self.x, self.y))

        self.searchEnd(grid, self.x, self.y, 0)

        return self.count

if __name__ == "__main__":
    sol = Solution()
    print(sol.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]]))
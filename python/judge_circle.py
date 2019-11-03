class Solution:
    def judgeCircle(self, moves: str) -> bool:
        if len(moves) % 2 == 1 :
            return False
        dic = {
            "U" : 0,
            "D" : 0, 
            "L" : 0,
            "R" :0
        }
        for move in moves :
            dic[move] += 1
        return dic["U"] == dic["D"] and dic["L"] == dic["R"]

if __name__ == "__main__":
    solution = Solution()
    print(solution.judgeCircle("ULDR"))
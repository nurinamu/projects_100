from typing import List

class Solution:
    morseList = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        dic = {}
        for idx in range(0, len(words)) :
            morse = ''
            for wIdx in range(0, len(words[idx])) :
                morse += self.morseList[ord(words[idx][wIdx]) - 97]
            dic[morse] = words[idx]

        return len(dic)

if __name__ == "__main__":
    solution = Solution()
    print("result : {}".format(solution.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"])))
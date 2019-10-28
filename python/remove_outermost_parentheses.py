class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        depth = 0
        result = ''
        for idx in range(0, len(S)) :
            if S[idx] == '(' :
                if depth != 0 :
                    result += S[idx]
                depth += 1
            elif S[idx] == ')' :
                depth -= 1
                if depth != 0 :
                    result += S[idx]

        return result

if __name__ == "__main__":
    solution = Solution()
    print(solution.removeOuterParentheses("(())()()(((())))"))
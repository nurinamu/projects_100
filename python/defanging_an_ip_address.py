class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")
    
if __name__ == "__main__":
    solution = Solution()
    print("result : {}".format(solution.defangIPaddr("192.168.0.1")))
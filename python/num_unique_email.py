from typing import List

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        dic = {}
        for email in emails :
            atIdx = email.index("@")
            lc = email[:atIdx]
            try:
                plusIdx = lc.index("+")
                if plusIdx >= 0 :
                    lc = lc[:plusIdx]
            except ValueError:
                pass
            lc = lc.replace(".","")
            dic[lc + email[atIdx:]] = 1

        return len(dic)

if __name__ == "__main__":
    sol = Solution()
    print(sol.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))
    print(sol.numUniqueEmails(["testemail@leetcode.com","testemail1@leetcode.com","testemail+david@lee.tcode.com"]))
class Solution:
    def checkString(self, s: str) -> bool:
        for i in range(len(s) - 1):
            if s[i] > s[i + 1]:   # 'b' followed by 'a'
                return False
        return True               # only after checking every pair
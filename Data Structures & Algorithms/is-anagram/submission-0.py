class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s2 = "".join(sorted(s))
        t2 = "".join(sorted(t))
        if s2 ==t2:
            return True
        return False

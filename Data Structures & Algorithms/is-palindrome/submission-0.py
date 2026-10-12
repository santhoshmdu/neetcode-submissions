class Solution:
    def isPalindrome(self, s: str) -> bool:
        letter = "".join(char.lower() for char in s if char.isalnum())
        if letter == letter[::-1]:
            return True
        else:
            return False
            
        
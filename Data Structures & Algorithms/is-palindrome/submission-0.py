class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c.lower() for c in s if c.isalnum())
        ivrt = s[::-1]
        if s != ivrt:
            return False
        if s == ivrt:
            return True

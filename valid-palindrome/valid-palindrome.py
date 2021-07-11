class Solution:
    def isPalindrome(self, s: str) -> bool:
        array = []
        for word in s:
            if word.isalnum():
                array.append(word.lower())
        
        while len(array) > 1:
            if array.pop(0) != array.pop():
                return False
        
        return True
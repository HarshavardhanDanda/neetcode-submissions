class Solution:
    def isAlphaNumeric(self, s):
        return True if ord(s) in range(65, 91) or ord(s) in range(97,123) or ord(s) in range(48, 58) else False
    def isPalindrome(self, s: str) -> bool:
        i,j=0,len(s)-1
        while(i<j):
            if(not self.isAlphaNumeric(s[i])):
                i+=1
                continue
            if(not self.isAlphaNumeric(s[j])):
                j-=1
                continue
            if(s[i].lower() == s[j].lower()):
                i+=1
                j-=1
                continue
            else:
                return False
        return True
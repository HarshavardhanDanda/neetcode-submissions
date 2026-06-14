class Solution:
    def isValid(self, s: str) -> bool:
        br={"}": "{", "]": "[", ")": "("}
        li=[]
        for i in s:
            if(len(li)>0 and li[-1] == br.get(i)):
                li.pop()
            else:
                li.append(i)
        if(len(li)==0):
            return True
        else:
            return False
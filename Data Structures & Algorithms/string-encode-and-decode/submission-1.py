class Solution:

    def encode(self, strs: List[str]) -> str:
        output=''
        for i in strs:
            output+=str(len(i))+'|'+i
        return output

    def decode(self, s: str) -> List[str]:
        j=0
        i=0
        output=[]
        while(i<len(s)):
            while(s[j] != '|'):
                j+=1
            count=int(s[i:j])
            # print(output)
            output.append(s[j+1:j+1+count])
            i=j+1+count
            j=j+1+count
        return (output)











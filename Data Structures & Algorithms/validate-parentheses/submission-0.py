class Solution:
    def isValid(self, s: str) -> bool:
        arr = ['0']*len(s)
        i=-1
        for c in s:
            if c==')':
                if i>=0 and arr[i]=="(":
                    arr[i]='0'
                    i-=1
                else:
                    i+=1
                    arr[i]=c
            elif c=='}':
                if i>=0 and arr[i]=="{":
                    arr[i]='0'
                    i-=1
                else:
                    i+=1
                    arr[i]=c
            elif c==']':
                if i>=0 and arr[i]=="[" :
                    arr[i]='0'
                    i-=1
                else:
                    i+=1
                    arr[i]=c
            else:
                i+=1
                arr[i]=c
        if i>=0:
            return False
        return True
            
                

        
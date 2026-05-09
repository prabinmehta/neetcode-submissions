class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss= ''.join(c for c in s if c.isalnum())
        # print(ss)
        i = 0
        j = len(ss)-1
        while i<j:
            a = ss[i].lower()
            b = ss[j].lower()
            # print(a,b)
            if a==b:
                i+=1
                j-=1
            else:
                return False
        return True

        
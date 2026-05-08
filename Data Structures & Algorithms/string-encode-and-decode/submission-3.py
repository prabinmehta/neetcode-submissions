class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs)<1:
            return ""
        k = 15
        result=""
        for s in strs:
            r = len(s)
            rep = []
            for i in s:
                c = ord(i)+k
                rep.append(str(c))
            rep = "#".join(rep)
            res = str(r)+"#"+rep+"#"
            result+=res
        return result

    def decode(self, s: str) -> List[str]:
        if s=="":
            return []
        k =15
        slist = s.split("#")
        i=0
        result=[]
        while i<len(slist)-1:
            print(i)
            l = int(slist[i])
            if l==0:
                result.append("")
                i=i+2
            else:
                res = ""
                for j in range(i+1,i+l+1):
                    print(slist[j])
                    c = chr(int(slist[j])-k)
                    res+=c
                result.append(res)
                i=i+l+1
        return result

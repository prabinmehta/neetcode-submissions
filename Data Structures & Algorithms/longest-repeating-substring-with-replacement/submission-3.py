from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # d = defaultdict(int)
        # l=0 
        # maxi =0
        # result = 0
        # for r in range(len(s)):
        #     d[s[r]]+=1
        #     maxi = max(maxi,d[s[r]])
        #     while (r-l+1)-maxi>k:
        #         d[s[r]]-=1
        #         l+=1
        #     result = max(result,r-l+1)
        # return result

        count = defaultdict(int)
        l = 0
        maxFreq = 0
        result = 0

        for r in range(len(s)):
            count[s[r]] += 1
            maxFreq = max(maxFreq, count[s[r]])

            # shrink window if invalid
            while (r - l + 1) - maxFreq > k:
                count[s[l]] -= 1
                l += 1

            result = max(result, r - l + 1)

        return result
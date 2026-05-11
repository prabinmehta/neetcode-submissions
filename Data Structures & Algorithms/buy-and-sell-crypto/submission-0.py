class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_suffix = [0]*len(prices)
        maxi =prices[-1]
        for i in range(len(prices)-1,-1,-1):
            if prices[i]>maxi:
                maxi=prices[i]
            max_suffix[i]=maxi
        print(max_suffix)
        maxi=0
        for i,j in enumerate(prices):
            sub = max_suffix[i]-j
            maxi = max(maxi,sub)
        return maxi

        
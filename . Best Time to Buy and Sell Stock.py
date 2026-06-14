class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = prices[0]
        r = 0
        for p in prices:
            l = min(p,l)
            r = max(r,p-l)
        return r

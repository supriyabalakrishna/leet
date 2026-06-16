class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        ma = mi = 1
        for n in nums:
            temp = ma*n
            ma = max(temp,mi*n,n)
            mi = min(temp,mi*n,n)
            res = max(res,ma)
        return res

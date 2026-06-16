class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = nums[0]
        ans = nums[0]
        for n in nums[1:]:
            curr = max(n,curr+n)
            ans = max(ans,curr)
        return ans

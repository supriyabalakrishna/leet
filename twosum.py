class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i , n in enumerate(nums):
            x = target - n
            if x in d:
                return [d[x],i]
            d[n] = i
        return False

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        for i in range(2 * len(nums)):
            if i >= len(nums):
                res.append(nums[i-n])
            else:
                res.append(nums[i])
        return res

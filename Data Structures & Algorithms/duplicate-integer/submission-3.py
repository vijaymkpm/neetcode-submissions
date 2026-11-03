class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        keys = set()
        for i in range(len(nums)):
            if nums[i] in keys:
                return True
            else:
                keys.add(nums[i])
        
        return False
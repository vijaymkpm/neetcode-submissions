class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        hashset = set(nums)
        # if len(hashset) <= 1:
        #     return len(hashset)

        max_length = 0
        for num in hashset:
            if (num-1) not in hashset:
                current_length = 1
            
                while (num + current_length) in hashset:
                    current_length +=1
                max_length = max(max_length, current_length)
        
        return max_length
        
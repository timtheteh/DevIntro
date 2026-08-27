class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        # num: idx -> tracks what num has been seen so far
        seen = {}

        for idx, num in enumerate(nums):
            if (target-num) not in seen:
                seen[num] = idx
            else:
                return [idx, seen[target-num]]
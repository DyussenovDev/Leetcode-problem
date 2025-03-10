# Runtime: 1 ms 

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in ans:
                return [i, ans[complement]]
            ans[nums[i]] = i
        return []
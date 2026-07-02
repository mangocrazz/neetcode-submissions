class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            target_search = target - nums[i]
            for j in range(i+1,len(nums)):
                if nums[j] == target_search:
                    return [i,j]
    
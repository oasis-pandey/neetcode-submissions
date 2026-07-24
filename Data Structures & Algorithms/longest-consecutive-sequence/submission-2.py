class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 1
        sorted_nums = sorted(nums)
        for i in range(len(sorted_nums)-1):
            if (sorted_nums[i+1]- sorted_nums[i] == 1):
                count += 1
        return count
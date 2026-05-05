from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        write = 1

        for read in range(1, len(nums)):
            if nums[read] != nums[read - 1]:
                nums[write] = nums[read]
                write += 1

        return write

sol = Solution()

nums = [0,0,1,1,1,2,3,3,3,4,4,5,5,]

print(sol.removeDuplicates(nums=nums))
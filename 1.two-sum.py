#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for i in nums:
            temp = nums[:nums.index(i):] + nums[nums.index(i)+1::]
            for j in temp:
                if i + j == target:
                    result_1 = nums.index(i)
                    nums.remove(i)
                    result_2 = nums.index(j) + 1
                    return list((result_1, result_2))

# @lc code=end

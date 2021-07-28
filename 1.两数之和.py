#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
#时间复杂度：O(N)，其中 N 是数组中的元素数量。对于每一个元素 x，我们可以 O(1) 地寻找 target - x。
#空间复杂度：O(N)，其中 N 是数组中的元素数量。主要为哈希表的开销。
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i, num in enumerate(nums):
            if target - num in h.keys():
                return [h[target - num], i]
            #键-值反向用来初始化哈希表，用值来判断更方便
            h[nums[i]] = i
        return []
# @lc code=end


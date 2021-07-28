#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start

#方法1，横向比较，从第一个字符串开始轮流比较每个字符串
#时间复杂度：O(mn)，其中 m 是字符串数组中的字符串的平均长度，n 是字符串的数量。最坏情况下，字符串数组中的每个字符串的每个字符都会被比较一次。
#空间复杂度：O(1)。使用的额外空间复杂度为常数。
'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        prefix, count = strs[0], len(strs)
        for i in range(1, count):
            #从第一个字符串轮流开始比较
            prefix = self.lcp(prefix, strs[i])
            if not prefix:
                break
        
        return prefix
    #找出两个字符串的公共前缀
    def lcp(self, str1, str2):
        length, index = min(len(str1), len(str2)), 0
        while index < length and str1[index] == str2[index]:
            index += 1
        return str1[:index]
'''
#方法2，纵向比较，i循环单个字符串内部，j循环字符串个数
#时间复杂度：O(mn)，其中 m 是字符串数组中的字符串的平均长度，n 是字符串的数量。最坏情况下，字符串数组中的每个字符串的每个字符都会被比较一次。
#空间复杂度：O(1)。使用的额外空间复杂度为常数。
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        length, count = len(strs[0]), len(strs)
        for i in range(length):
            c = strs[0][i]
            #i等于某个字符串的长度或者某个元素和首个字符串的某个元素不相等则退出循环
            if any(i == len(strs[j]) or strs[j][i] != c for j in range(1, count)):
                return strs[0][:i]
        
        return strs[0]

# @lc code=end


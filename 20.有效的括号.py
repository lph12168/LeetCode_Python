#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
#时间复杂度：O(n)，其中 nnn 是字符串 sss 的长度。
#空间复杂度：O(n+∣Σ∣)，其中 Σ 表示字符集，本题中字符串只包含 6 种括号，∣Σ∣ = 6。栈中的字符数量为 O(n)，而哈希表使用的空间为 O(∣Σ∣)，相加即可得到总空间复杂度。
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        #反向定义可以减少入栈次数
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = list()
        for ch in s:
            #此处遍历的是key，没有遍历value
            if ch in pairs:
                #出现右半符号则比较，相等就弹出
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                #出现左半符号都入栈
                stack.append(ch)
        
        return not stack

# @lc code=end


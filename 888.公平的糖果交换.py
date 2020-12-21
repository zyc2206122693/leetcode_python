#
# @lc app=leetcode.cn id=888 lang=python3
#
# [888] 公平的糖果交换
#

# @lc code=start
class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        differ = sum(A) - sum(B)
        for a in A:
            b = a - differ // 2
            if b in B:
                return [a,b]
# @lc code=end


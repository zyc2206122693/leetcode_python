#
# @lc app=leetcode.cn id=653 lang=python3
#
# [653] 两数之和 IV - 输入 BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        #可以考虑队列
        res = []
        queue = [root]
        while queue:
            nxt = []
            for q in queue:
                res.append(q.val)
                if q.left:
                    nxt.append(q.left)
                if q.right:
                    nxt.append(q.right)
            queue = nxt
        
        for i in range(len(res)-1):
            for j in range(i+1,len(res)):
                if res[i]+res[j] == k:
                    return True
        return False
# @lc code=end


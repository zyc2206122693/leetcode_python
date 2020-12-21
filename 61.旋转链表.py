#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        fast,slow = head,head
        #找到fast的起始节点
        def findStart(fast,k):
            len = 0
            while k > 0:
                k -= 1
                len += 1
                fast = fast.next
                if not fast:
                    fast = head
                    k = k % len
                    return findStart(fast,k)
            return fast
        
        fast = findStart(fast,k)
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        
        fast.next = head
        head = slow.next
        slow.next = None
        return head
# @lc code=end


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head):
        
        flag = 0
        prev = None
        val = 0
        
        ans = node = head
        
        while node:
            if flag == 0:
                prev = node
                flag = 1
                node = node.next
                continue
                
            if flag == 1:
                val = node.val
                node.val = prev.val
                prev.val = val
                node = node.next
                flag = 0
                continue
        
        return ans
        
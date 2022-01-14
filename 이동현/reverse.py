# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def recur(self, li, cnt, right):
        
        if cnt == right:
            if li is None:
                return li, li, None
            return li, li, li.next
        
        if li != None:
            first, recent, end = self.recur(li.next, cnt+1, right)
        
            recent.next = li
        
            return first, li, end
        else:
            return li, li, li
    
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        cnt = 1
        first = head
        
        if head is None:
            return head

        while cnt == left:
            head = head.next
            cnt += 1
            
        
        if head is None:
            return first
        
        st, recent, end = self.recur(head.next, left, right)

        if end != None:
            
            recent.next = end
        
        head.next = st
        
        return first
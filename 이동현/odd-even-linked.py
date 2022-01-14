# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        odd = head
        
        if head is None:
            return head
        if head.next is None:
            return head
        
        even = head.next
        
        
        temp_odd = odd
        temp_even = even
        
        while temp_even.next and temp_even.next.next:
            
            temp_odd.next  = temp_odd.next.next
            temp_even.next = temp_even.next.next
            temp_odd = temp_odd.next
            temp_even = temp_even.next
            
            # print(odd)
            # print(even)
            # print("odd_temp", temp_odd)
            # print("even_tmep", temp_even)
        
        if temp_even.next is not None:
            temp_odd.next = temp_odd.next.next
            temp_odd = temp_odd.next
            temp_even.next = None
            
        temp_odd.next = even
        
        return odd
        
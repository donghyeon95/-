# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        start = res = ListNode(None)
        heap = []
        
        for idx in range(len(lists)):
            if lists[idx]:
                heapq.heappush(heap, (lists[idx].val, idx, lists[idx]))
        
        while heap:
            node = heapq.heappop(heap) 
            idx = node[1]
            res.next = node[2]
            
            res = res.next
            if res.next:
                heapq.heappush(heap, (res.next.val, idx ,res.next))
        return start.next
            

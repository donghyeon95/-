class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    
    def get_num(self, li) ->  int:
        number = 0
        dec = 1
        nextNode = li
        
        while nextNode:
            number += nextNode.val * dec
            dec *= 10
            nextNode = nextNode.next
        
        return number
    
    
    def get_list(self, num: int):
        
        num_list = str(num)
        ans = ListNode()
        temp = ans
        
        for index in range(len(num_list)-1, -1, -1):
            node = ListNode(num_list[index])
            temp.next = node
            temp = node
        
        return ans.next
        
    
    def addTwoNumbers(self, l1, l2):
        
        num1 = self.get_num(l1)
        num2 = self.get_num(l2)
        
        print(num1, num2)
        return self.get_list(num1+num2)
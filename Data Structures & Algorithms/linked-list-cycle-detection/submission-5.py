# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        step=0
        d={}
        curr=head
        while(curr):
            if(id(curr) in d):
                return True
            step+=1
            d[id(curr)]=step
            curr=curr.next
        return False

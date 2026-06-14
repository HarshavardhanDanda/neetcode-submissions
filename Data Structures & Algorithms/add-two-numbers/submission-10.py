# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# keep the loop until u reach both ends, so use or condition
# calculate sum and carry for each pair, carry the 1 to next pair
# edge case, if both linked lists contain one number 9 and 9, we get
# 18, so 8 1 if we reverse, so dont forget to add the carry 1 after u
# reach the end 
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result=ListNode()
        head=result
        carry=0
        while(l1 or l2):
            a=l1.val if l1 else 0
            b=l2.val if l2 else 0
            sum=a+b+carry
            carry = 1 if a+b+carry > 9 else 0
            head.next=ListNode(sum%10)
            head=head.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        if(carry==1):
            head.next=ListNode(1)
        return result.next

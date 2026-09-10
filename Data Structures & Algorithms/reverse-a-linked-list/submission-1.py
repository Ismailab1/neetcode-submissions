# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize pointers for the reversal process.
        # `prev` will eventually be the new head.
        prev = None
        curr = head

        # Iterate through the list, reversing each node's pointer.
        while curr:
            # 1. Store the next node before we change anything.
            temp = curr.next
            
            # 2. Reverse the current node's pointer to point to the previous node.
            curr.next = prev
            
            # 3. Move both pointers one step forward for the next iteration.
            prev = curr
            curr = temp

        # When the loop ends, `prev` is the new head of the reversed list.
        return prev
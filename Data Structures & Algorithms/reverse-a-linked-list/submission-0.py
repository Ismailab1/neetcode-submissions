# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Sets up curr and head as two pointers to traverse the list with
        curr = head
        prev = None

        # While curr does not point to "None", we set up a temporary node to point to
        # the next node for curr, then we have the pointer to curr point to prev, which
        # reverses the direction of the current node to the oppisite direction.
        # Then we set the prev pointer to the current node and move the curr pointer to
        # the next node
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # Returns the reversed linked list
        return prev
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Checks if the list exists and has more than one element
        if not head or not head.next:
            return

        # Initiates slow anf fast pointers
        slow, fast = head, head.next

        # Looks for the middle of the list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverses the starting point of second half of the list
        second = slow.next
        prev = None
        # Breaks the link between the two lists
        slow.next = None

        # Reverses the second half of the list
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # Sets the pointers at the beginning of both linked lists
        first, second = head, prev
        
        # Merges both lists
        while second:
            temp1, temp2 = first.next, second.next

            first.next = second
            second.next = temp1

            first, second = temp1, temp2
        
        return
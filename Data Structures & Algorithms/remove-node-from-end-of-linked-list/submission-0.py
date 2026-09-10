# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Establishes the curr pointer and the index counter
        curr = head
        indexes = 0

        # Counts how many nodes there are
        while curr:
            indexes += 1
            curr = curr.next
        
        # Finds the index of the node we need to remove
        index_to_remove = indexes - n

        # If the index is at the beginning of the list, then we
        # Return the node after the beginning of the list
        if index_to_remove == 0:
            return head.next
        
        # We reset the curr pointer back to the beginning of the list to find
        # the index where we need to remove a node
        curr = head
        
        # We iterate through the list to find the deletion_index and
        # set the pointer to the node after the marked node to delete
        # the node
        for i in range(indexes - 1):
            if (i + 1) == index_to_remove:
                curr.next = curr.next.next
            curr = curr.next
        
        # We return the beginning of the list after the deleted node
        return head

        
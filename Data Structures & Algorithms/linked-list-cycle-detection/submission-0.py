# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Create a set to track the nodes we have seen
        seen = set()

        # Create a pointer to traverse through the linked list
        pointer = head

        # While the pointer does not point to "None", we
        # check if the current node at the pointer has been seen in the
        # set. If it has, we return True immediately because that 
        # means a cycle has been found. If not, it adds that not to the set
        # to track that it has become seen and move the pointer to the net node
        while pointer:
            if pointer in seen:
                return True
            seen.add(pointer)
            pointer = pointer.next

        # Returns False due to not finding a cycle within the list
        return False
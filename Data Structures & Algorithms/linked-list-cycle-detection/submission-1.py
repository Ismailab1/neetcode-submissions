# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Use a set to store nodes that have already been visited.
        seen = set()
        pointer = head

        # Traverse the list. If we encounter a node already in our set,
        # we have found a cycle.
        while pointer:
            if pointer in seen:
                return True
            
            # If the node is new, add it to the set and move to the next one.
            seen.add(pointer)
            pointer = pointer.next

        # If the loop finishes, the pointer reached the end (None), so no cycle exists.
        return False
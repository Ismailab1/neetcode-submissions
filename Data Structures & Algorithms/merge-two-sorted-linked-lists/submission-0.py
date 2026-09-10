# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Creates a new LinkedList for us to use
        dummy = ListNode()
        l3 = dummy

        # While both linked list exists, we point the l3 pointer to the
        # lesser value between list1 and list2. Then we move the pointer at
        # list1 or list2, then finally at list 3 once the current node has been updated
        while list1 and list2:
            if list1.val < list2.val:
                l3.next = list1
                list1 = list1.next
            else:
                l3.next = list2
                list2 = list2.next
            l3 = l3.next
        
        # Adds the rest of the nodes left over from the while loop
        # to ensure we account for all nodes
        l3.next = list1 or list2

        # Returns the newly merged list
        return dummy.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to act as the starting point of the new list.
        dummy = ListNode()
        # l3 will be the "tail" pointer, tracking the last node in the merged list.
        l3 = dummy

        # Loop as long as both lists have nodes.
        while list1 and list2:
            # Compare nodes and append the smaller one to the tail.
            if list1.val < list2.val:
                l3.next = list1
                list1 = list1.next
            else:
                l3.next = list2
                list2 = list2.next
            
            # Advance the tail pointer to the newly added node.
            l3 = l3.next
        
        # Once a list is empty, append the remaining nodes from the other list.
        l3.next = list1 or list2

        # The merged list starts after the dummy node.
        return dummy.next
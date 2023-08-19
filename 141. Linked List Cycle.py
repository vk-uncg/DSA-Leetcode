# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        marker1 = head
        marker2 = head

        while(marker2 is not None and marker2.next is not None):
            marker1 = marker1.next
            marker2 = marker2.next.next

            if(marker1 == marker2):
                return True

        return False
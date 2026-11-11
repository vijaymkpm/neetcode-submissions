# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1, head)

        current = dummy.next
        

        while current and current.next is not None:
            if current.val != current.next.val:
                current = current.next
            else:
                prev = current
                while current and current.val == prev.val:
                    current = current.next
                prev.next = current
        return dummy.next
                
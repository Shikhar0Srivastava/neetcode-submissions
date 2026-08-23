# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        mover = head
        while mover:
            mover = mover.next
            length += 1
        remove_index = length - n
        
        prev = None
        first = head
        while remove_index > 0:
            prev = first
            first = first.next
            remove_index -= 1
        
        if prev:
            if first:
                prev.next = first.next
        else:
            return head.next

        return head

        
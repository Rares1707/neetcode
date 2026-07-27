# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle of the list
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half
        current = slow.next
        slow.next = None
        prev = None
        while current:
            next, current.next = current.next, prev
            prev, current = current, next

        # insert second half into first half
        first_head = head
        second_head = prev
        while second_head:
            next = first_head.next
            first_head.next = second_head
            second_head.next, second_head = next, second_head.next
            first_head = next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        result = ListNode()

        current = result
        add_later = 0
        while l1 and l2:
            total = l1.val + l2.val + add_later

            current.next = ListNode()
            current = current.next
            current.val = total % 10
            add_later = total // 10

            l1 = l1.next
            l2 = l2.next

        remaining_list = l1 if l1 else l2  # it's fine if both are None
        while remaining_list:
            total = remaining_list.val + add_later

            current.next = ListNode()
            current = current.next
            current.val = total % 10
            add_later = total // 10

            remaining_list = remaining_list.next

        if add_later:
            current.next = ListNode()
            current = current.next
            current.val = 1

        return result.next

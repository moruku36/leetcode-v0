class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        while current.next and current.next.next:
            first_node = current.next
            second_node = current.next.next
            first_node.next = second_node.next
            current.next = second_node
            current.next.next = first_node
            current = current.next.next
        return dummy.next
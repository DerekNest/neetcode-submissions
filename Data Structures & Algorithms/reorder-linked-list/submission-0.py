class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        curr = slow.next
        slow.next = None
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        head2 = prev  

        
        while head2:
            nxt1 = head.next
            nxt2 = head2.next
            head.next = head2
            head2.next = nxt1
            head = nxt1
            head2 = nxt2
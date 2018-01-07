# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummyHead = ListNode(0)
        p = l1
        q = l2
        carry = 0
        curr = dummyHead

        #while l1 or l2:
        while p or q:
            x = p.val if p else 0
            y = q.val if q else 0
            sum = x + y + carry
            carry = sum // 10

            curr.next = ListNode(sum % 10)
            curr = curr.next

            if p: p = p.next
            if q: q = q.next

        if carry:
            curr.next = ListNode(carry)
        return dummyHead.next

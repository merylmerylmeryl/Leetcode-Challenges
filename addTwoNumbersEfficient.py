# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype  : ListNode
        """

        carry = 0
        thisNode = l1
        otherNode = l2
        sumList = ListNode(0)
        sumList.val = 0
        sumListRoot = sumList
        
        while thisNode:
            
            if otherNode:
                sumList.val += thisNode.val + otherNode.val
                otherNode = otherNode.next
            else:
                sumList.val += thisNode.val
            if sumList.val >= 10:
                carry = 1
                sumList.val -= 10
                
            thisNode = thisNode.next

            if thisNode or otherNode:
                sumList.next = ListNode(0)
                sumList = sumList.next
                sumList.val = carry
                carry = 0

        if carry:
            sumList.next = ListNode(1)

        while otherNode:
            carry = 0
            sumList.val += otherNode.val
            if sumList.val >= 10:
                sumList.val -= 10
                carry = 1
            if otherNode.next:
                sumList.next = ListNode(0)
                sumList = sumList.next
                sumList.val = carry
            otherNode = otherNode.next
            if carry and not otherNode:
                sumList.next = ListNode(carry)

        return sumListRoot

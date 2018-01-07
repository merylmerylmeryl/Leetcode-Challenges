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
        string1 = self.linkedToIntString(l1)
        string2 = self.linkedToIntString(l2)
        strSum = str(int(string1) + int(string2))
        
        return self.stringToLinkedList(strSum)

    def linkedToIntString(self, linkList):
        if not linkList:
            return ''
        return  str(self.linkedToIntString(linkList.next)) + str(linkList.val)

    def stringToLinkedList(self, string):
        root = ListNode(int(string[-1]))
        string = string[:-1]

        node = root
        for c in reversed(string):
            node.next = ListNode(int(c))
            node = node.next
        
        return root

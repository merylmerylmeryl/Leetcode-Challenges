# iterate from the start to the middle
# iterate from the middle to the start at the same time

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        while x >= 1:
            x = x // 10

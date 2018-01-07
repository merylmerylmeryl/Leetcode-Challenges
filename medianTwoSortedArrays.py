class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        p = nums1
        q = nums2
        solList = []
        
        if not p and q:
            if p:
                return self.medianOf(p)
            elif q:
                return self.medianOf(q)
            else:
                return None

        while p or q:
            if p and q:
                if p[0] <= q[0]:
                    solList.append(p[0])
                    p = p[1:]
                else:
                    solList.append(q[0])
                    q = q[1:]
            elif p:
                solList.extend(p)
                return self.medianOf(solList)
            else:
                solList.extend(q)
                return self.medianOf(solList)

        return self.medianOf(solList)

    def medianOf(self, nums):
        # calculate the median index of nums array
        if not nums:
            return None
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return (nums[0] + nums[1]) / 2
        else:
            if len(nums) % 2 == 0:
                index = (len(nums) // 2) - 1
                return (nums[index] + nums[index+1]) / 2
            else:
                index = len(nums) // 2
                return nums[index]

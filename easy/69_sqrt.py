# O(log(x))      ---Binary Search---
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x
        left, right = 1, x // 2
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
        return right

# O(root(x))
class Solution1(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        i = 0
        while True:
            if i*i == x :
                return i
            if i*i > x :
                return i-1
            i +=1
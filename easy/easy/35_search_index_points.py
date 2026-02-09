'''
    Given a sorted array of distinct integers and a target value, 
    return the index if the target is found. 
    If not, return the index where it would be if it were inserted in order.
    You must write an algorithm with O(log n) runtime complexity.
'''
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target :
                return mid
            elif nums[mid] < target :
                left = mid + 1
            else :
                right = mid - 1
        return left

sol = Solution()

# Example 1
print(sol.searchInsert([1,2,4], 3))  # Output: 2

# Example 2
print(sol.searchInsert([1,3,5,6], 5))  # Output: 2

# Example 3
print(sol.searchInsert([1,3,5,6], 2))  # Output: 1

# Example 4
print(sol.searchInsert([1,3,5,6], 7))  # Output: 4

# Example 5
print(sol.searchInsert([1,3,5,6], 0))  # Output: 0

# Example 6 (Edge Case)
print(sol.searchInsert([], 1))  # Output: 0

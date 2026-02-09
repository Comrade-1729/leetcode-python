'''
    Given an integer array nums and an integer val, remove all occurrences of 
    val in nums in-place. The order of the elements may be changed. 
    Then return the number of elements in nums which are not equal to val.
'''
class Solution(object):
    ''' Main class '''
    def remove_element(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = 0
        for num in nums:
            if num != val:
                nums[n] = num
                n += 1
        return n

def main():
    ''' Main function to demonstrate the remove_element method '''
    solution = Solution()

    # Example 1
    nums1 = [3, 2, 2, 3]
    val1 = 3
    result_length1 = solution.remove_element(nums1, val1)
    print("Modified length:", result_length1)
    print("Modified array:", nums1[:result_length1])  # Show only the modified portion of the array

    # Example 2
    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    val2 = 2
    result_length2 = solution.remove_element(nums2, val2)
    print("Modified length:", result_length2)
    print("Modified array:", nums2[:result_length2])  # Show only the modified portion of the array

if __name__ == "__main__":
    main()

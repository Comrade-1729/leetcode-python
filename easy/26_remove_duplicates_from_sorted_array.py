''' Given an integer array nums sorted in non-decreasing order, 
    remove the duplicates in-place such that each unique element appears only once. 
    The relative order of the elements should be kept the same. 
    Then return the number of unique elements in nums. 
'''
class Solution(object):
    ''' main class '''
    def __init__(self):
        pass
    def remove_duplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        # Pointer for the unique element position
        n = 0
        
        for i in range(1, len(nums)):
            if nums[i] != nums[n]:
                n += 1
                nums[n] = nums[i]
        # The length of the array without duplicates
        return n + 1
def main() :
    ''' main function '''
    a=Solution()
    nums1 = [1,1,2]
    nums2 = [0,0,1,1,1,2,2,3,3,4]
    print(a.remove_duplicates(nums1))
    print(a.remove_duplicates(nums2))
if __name__ == '__main__' :
    main()

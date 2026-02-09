'''
    You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
    and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
    Merge nums1 and nums2 into a single array sorted in non-decreasing order.
    The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
    To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that
    should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
'''
class Solution(object):
    ''' Main Class '''
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1, nums2 : List[int]
        :type m, n : int
        :rtype : list (nums1)
        """
        # Start from the end of nums1
        i, j = m - 1, n - 1
        # Pointer for the last position in nums1
        k = m + n - 1

        # Merge in reverse order
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # If there are elements left in nums2, put them in nums1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

        return nums1

def main() :
    ''' Main Function '''
    solution = Solution()
    lst1, lst2 = [1,2,3,0,0,0], [2,5,6]
    m1, n1 = 3, 3
    lst3, lst4 = [1], []
    m2, n2 = 1, 0
    lst5, lst6 = [2,3,0,0], [1,2]
    m3, n3 = 2, 2
    print(solution.merge(lst1,m1,lst2,n1))
    print(solution.merge(lst3,m2,lst4,n2))
    print(solution.merge(lst5,m3,lst6,n3))

if __name__ == '__main__' :
    main()    

'''
    You are given a large integer represented as an integer array digits, 
    where each digits[i] is the ith digit of the integer. 
    The digits are ordered from most significant to least significant in left-to-right order. 
    The large integer does not contain any leading 0's.
    Increment the large integer by one and return the resulting array of digits.
'''
class Solution(object):
    ''' Main Class '''
    def plus_one(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        # If we exit the loop, it means all digits were 9
        return [1] + digits
def main() :
    ''' Main Function '''
    digits1 = [1,2,3]
    digits2 = [4,3,2,1]
    solution = Solution()
    print(solution.plus_one(digits1))
    print(solution.plus_one(digits2))
if __name__ == '__main__' :
    main()

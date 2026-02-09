'''
    Given two binary strings a and b, 
    Return their sum as a binary string.
'''
class Solution(object):
    ''' Main Class '''
    def add_binary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # Convert binary strings to integers, add them, and convert back to binary
        sum_value = int(a, 2) + int(b, 2)
        # Convert the sum back to binary string and remove the '0b' prefix
        return bin(sum_value)[2:]
def main() :
    ''' Main Function '''
    solution = Solution()
    a1 = "11"
    b1 = "1"
    a2 = "1010"
    b2 = "1011"
    a3 = "1111"
    b3 = "1111"
    print(solution.add_binary(a1,b1))
    print(solution.add_binary(a2,b2))
    print(solution.add_binary(a3,b3))
if __name__ == '__main__' :
    main()

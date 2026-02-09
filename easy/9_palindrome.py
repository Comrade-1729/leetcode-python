'''
    A number is a palindrome if it remains the same when its digits are reversed.
'''
class Solution(object):
    ''' Main Class '''
    def ispalindrome(self, x):
        """
        type x: int
        rtype: bool
        """
        if x < 0 :
            return False
        copy = x
        a = 0
        while x!=0 :
            a = (a*10) + (x%10)
            # x = x / 10     #Floating point Division since python3
            x = x // 10      #Use this for Integer Division
        return True if a == copy else False
obj1 = Solution()
while True :
    num = int(input("Enter a Number to check : "))
    print(obj1.ispalindrome(num))

'''
    You are climbing a staircase. It takes n steps to reach the top.
    Each time you can either climb 1 or 2 steps. 
    In how many distinct ways can you climb to the top?
'''
class Solution(object):
    ''' Main class '''
    def climb_stairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2
        # Initialize base values
        a, b = 1, 2
        # Compute the number of ways for each integer up to n
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b
def main() :
    ''' Main Function '''
    solution = Solution()
    for i in range(1,5):
        print(solution.climb_stairs(i))

if __name__ == '__main__' :
    main()

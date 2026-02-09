'''
    Given an array of integers nums and an integer target
    Return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution,
    And you may not use the same element twice.
'''
class Solution(object):
    ''' Main Class '''
    def sum(self, nums, target) :
        ''' Sum Function '''
        seen = {}
        for i,num in enumerate(nums) :
            compliment = target - num
            if compliment in seen :
                return [seen[compliment],i]
            seen[num] = i
obj = Solution()
# Get input and convert it into a list of integers
n = list(map(int, input("Enter a list/array of Numbers (space-separated): ").split()))
t = int(input("Enter a 'Target' integer : "))
indices = obj.sum(n,t)
print(f"The Indices of values that sum up to Target are : {indices}")

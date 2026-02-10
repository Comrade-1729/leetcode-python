'''
    Given two strings needle and haystack, 
    return the index of the first occurrence of needle in haystack, 
    or -1 if needle is not part of haystack.
'''
class Solution(object):
    ''' Main class '''
    def str_str(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)

def main() :
    ''' Main function
      '''
    solution = Solution()
    haystack1 = "sadbutsad"
    needle1 = "sad"
    haystack2 = "leetcode"
    needle2 = "leeto"
    print(solution.str_str(haystack1,needle1))
    print(solution.str_str(haystack2,needle2))

if __name__ == '__main__' :
    main()

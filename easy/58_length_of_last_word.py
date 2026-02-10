'''
    Given a string s consisting of words and spaces, 
    Return the length of the last word in the string.
    A word is a maximal substring consisting of 
    non-space characters only.
'''
class Solution(object):
    ''' Main class '''
    def length_of_last_word(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if not s:
            return 0
        l = len(s)
        for i in range(l - 1, -1, -1):
            if s[i] == " ":
                return l - i - 1
        return l
def main() :
    ''' Main Function '''
    solution = Solution()
    s1 = "Hello World"
    s2 = "   fly me   to   the moon  "
    s3 = "luffy is still joyboy"
    print(solution.length_of_last_word(s1))
    print(solution.length_of_last_word(s2))
    print(solution.length_of_last_word(s3))

if __name__ == '__main__' :
    main()

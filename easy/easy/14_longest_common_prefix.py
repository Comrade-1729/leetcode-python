'''
    Write a function to find the longest common prefix string amongst an array of strings. 
'''
class Solution(object):
    ''' Main class '''
    def longest_common_prefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        s = ""
        for char in strs[0]:
            s += char
            for word in strs[1:]:
                if not word.startswith(s):
                    return s[:-1]
        return s

def main():
    ''' Main Function '''
    strs1 = ["flower","flow","flight"]
    strs2 = ["dog","racecar","car"]
    a=Solution()
    print(a.longest_common_prefix(strs1))
    print(a.longest_common_prefix(strs2))

if __name__ =='__main__':
    main()

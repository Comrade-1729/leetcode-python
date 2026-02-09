'''
    Given an integer numRows, return the first numRows of Pascal's triangle.
    In Pascal's triangle, each number is the sum of the two numbers directly above
'''
class Solution(object):
    ''' Main Class '''
    def generate(self, num_rows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        nums = []
        for _ in range(num_rows):
            # Start each row with [1]
            row = [1]
            # Add elements from the previous row
            if nums:
                last_row = nums[-1]
                for j in range(1, len(last_row)):
                    row.append(last_row[j - 1] + last_row[j])
                row.append(1)
            nums.append(row)
        return nums
def main() :
    ''' Main Function '''
    while True :
        n = int(input("Enter number of rows of the Pascal Triangle : "))
        solution = Solution()
        print(solution.generate(n))
if __name__ == '__main__' :
    main()

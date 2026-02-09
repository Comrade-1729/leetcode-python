'''
    Given a roman numeral, convert it to an integer.
'''
class Solution(object):
    ''' Main Class '''
    def roman_to_int(self, s):
        ''' Input type String 's', and returns an Integer type 'total' '''
        roman_values = { "I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000 }
        total = 0

        # Loop through each character and its index using enumerate
        for i, char in enumerate(s):
            # Check if the current numeral is less than the next numeral
            if i + 1 < len(s) and roman_values[char] < roman_values[s[i + 1]]:
                # Subtract current numeral value
                total -= roman_values[char]
            else:
                # Add current numeral value
                total += roman_values[char]

        return total

# Define the main function outside of the class
def main():
    ''' Main Function '''
    num = input("Enter the Roman Numeral to be converted to Integer: ")
    solution = Solution()  # Create an instance of Solution
    print(solution.roman_to_int(num))  # Call roman_to_int through the instance

# Run main if this script is executed directly
if __name__ == "__main__":
    main()

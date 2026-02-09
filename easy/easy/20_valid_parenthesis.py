'''
    Valid Parenthesis 
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
Determine if the input string is valid.

An input string is valid if:
1) Open brackets must be closed by the same type of brackets.
2) Open brackets must be closed in the correct order.
3) Every close bracket has a corresponding open bracket of the same type.
'''
def is_valid(s):
    """
    :type s: str
    :rtype: bool
    """
    # Stack to keep track of opening brackets
    stack = []

    # Dictionary to map closing brackets to opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}     # key : value

    # Iterate over each character in the input string
    for char in s:
        if char in bracket_map.values():  # Opening brackets (value)
            stack.append(char)
        elif char in bracket_map:  # Closing brackets (key)
            # Check for matching opening bracket at top of stack
            if stack and stack[-1] == bracket_map[char]:   # Also checking if stack is not empty
                stack.pop()  # Remove matched opening bracket
            else:
                return False  # Mismatch found
        else:
            return False  # Invalid character in input

    # Check if stack is empty, indicating all brackets matched
    return len(stack) == 0

def main():
    """Main Function"""
    # Test cases
    test_cases = ["()", "()[]{}", "(]", "([])"]
    for s in test_cases:
        print(f"{s}: {is_valid(s)}")

if __name__ == '__main__':
    main()

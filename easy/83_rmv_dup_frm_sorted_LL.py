'''
    Given the head of a sorted linked list, 
    delete all duplicates such that each element appears only once. 
    Return the linked list sorted as well.
'''
class ListNode(object):
    ''' Definition for singly-linked list. '''
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node
class Solution(object):
    ''' Solution class '''
    def delete_duplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current = head
        while current and current.next :
            if current.val == current.next.val :
                current.next = current.next.next
            else :
                current = current.next
        return head

def list_to_linkedlist(elements):
    ''' Helper function to convert list to linked list '''
    dummy = ListNode()
    current = dummy
    for el in elements:
        current.next = ListNode(el)
        current = current.next
    return dummy.next

def linkedlist_to_list(node):
    ''' Helper function to convert linked list to list '''
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Example Usage
sol = Solution()
l1 = [1,1,2]
l2 = [1,1,2,3,3]
l3 = []
l4 = [1]
# Test Case 1
lst1 = list_to_linkedlist([1])
new = sol.delete_duplicates(lst1)
print(linkedlist_to_list(new))

# Test Case 2
lst1 = list_to_linkedlist([1,1,2])
new = sol.delete_duplicates(lst1)
print(linkedlist_to_list(new)) 

# Test Case 3
lst1 = list_to_linkedlist([1,1,2,3,3])
new = sol.delete_duplicates(lst1)
print(linkedlist_to_list(new))

# Test Case 4
lst1 = list_to_linkedlist([])
new = sol.delete_duplicates(lst1)
print(linkedlist_to_list(new))

# Test Case 5
lst1 = list_to_linkedlist([1,2,3])
new = sol.delete_duplicates(lst1)
print(linkedlist_to_list(new))
# Example 1
# Input: head = [1,1,2]
# Output: [1,2]

# Example 2
# Input: head = [1,1,2,3,3]
# Output: [1,2,3]

# Edge Case: Empty List
# Input: head = []
# Output: []

# Edge Case: Single Element
# Input: head = [1]
# Output: [1]

# Edge Case: No Duplicates
# Input: head = [1,2,3]
# Output: [1,2,3]

'''
    You are given the heads of two sorted linked lists list1 and list2.
    Merge the two lists into one sorted list. 
    The list should be made by splicing together the nodes of the first two lists.
    Return the head of the merged linked list.
'''
class ListNode :
    ''' Node Class '''
    def __init__(self,val=0, next_node=None) :
        self.val = val
        self.next = next_node
class Solution(object) :
    ''' Merging class '''
    def merge_two_lists(self,list1,list2) :
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Initialize a dummy node to build the merged list
        dummy = ListNode()
        current = dummy # pointer of dummy LL
        # Traverse both lists and merge them in sorted order
        while list1 and list2 :
            if list1.val <= list2.val :
                current.next = list1
                list1 = list1.next
            else :
                current.next = list2
                list2 = list2.next
            current = current.next
        # Attach the remaining nodes (if any)
        current.next = list1 if list1 else list2
        # The merged list is next of dummy node
        return dummy.next

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

# Test Case 1
lst1 = list_to_linkedlist([1, 2, 4])
lst2 = list_to_linkedlist([1, 3, 4])
merged = sol.merge_two_lists(lst1, lst2)
print(linkedlist_to_list(merged))  # Output: [1, 1, 2, 3, 4, 4]

# Test Case 2
lst1 = list_to_linkedlist([])
lst2 = list_to_linkedlist([])
merged = sol.merge_two_lists(lst1, lst2)
print(linkedlist_to_list(merged))  # Output: []

# Test Case 3
lst1 = list_to_linkedlist([])
lst2 = list_to_linkedlist([0])
merged = sol.merge_two_lists(lst1, lst2)
print(linkedlist_to_list(merged))  # Output: [0]

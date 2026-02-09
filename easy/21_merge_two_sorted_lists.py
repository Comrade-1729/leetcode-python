# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    ''' main class '''
    def merge_two_lists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        i1, i2 = 0
        list=[]
        if not list1 and list2:
            return list[]
        if not list1 or list2 :
            return list1 if not list2 else list2
        l = len(list1)+len(list2)
        for i in range(l) :
            if list1[i1] < list2[i2] :
                list[i] = list1[i1]
                i1 += 1
            elif list1[i1] > list[i2] :
                list[i] = list2[i2]
                i2 += 1
            else :
                list[i] = list1[i1]
                list[i+1] = list2[i2]
                i += 1
                i1 += 1
                i2 += 1
        return list

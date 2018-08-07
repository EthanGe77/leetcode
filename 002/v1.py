# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    carry = 0

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        result = ListNode(0)
        pointer = result
        carry = 0
        while l1 or l2 or carry:
        	sum_ = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
        	carry = sum_ // 10
        	pointer.next = ListNode(sum_ % 10)
        	pointer = pointer.next

        	l1 = l1.next if l1 else None
        	l2 = l2.next if l2 else None

        return result



# a = Solution()
# print(a.addTwoNumbers([9,2,3],[1,2,3]))
# # print(Solution.carry)


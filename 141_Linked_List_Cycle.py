# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None: return False
        node1 = head
        node2 = head.next
        while node2 != None and node2.next != None:
            if node1 == node2:
                return True
            node1 = node1.next
            node2 = node2.next.next
        return False
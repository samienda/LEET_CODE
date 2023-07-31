# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def traverse(first, second):
            if not first:
                return second

            if not second:
                return first

            if first.val <= second.val:
                last = ListNode(first.val)
                last.next = traverse(first.next, second)
            else:
                last = ListNode(second.val)
                last.next = traverse(first, second.next)


            return last


        return traverse(list1, list2)     


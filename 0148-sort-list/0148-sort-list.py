# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # BUBBLE SORT

        def bubble(head):
            record = None
            second = ListNode()
            second.next = head
            mainone = head

            while mainone:
                curr = head
                while curr.next != record:
                    if curr.val > curr.next.val:
                        temp = curr.val
                        curr.val = curr.next.val
                        curr.next.val = temp

                    curr = curr.next
                
                record = curr

                mainone = mainone.next

            return second.next

        # return bubble(head)

        # built in sort

        def builtIn(head):
            curr = head
            lis = []
            while curr:
                lis.append(curr.val)
                curr = curr.next

            lis.sort()

            curr = ListNode()
            temp = curr
            for i in range(len(lis)):
                curr.next = ListNode(lis[i])
                curr = curr.next

            return temp.next

        return builtIn(head)



        # MERGE SORT



            




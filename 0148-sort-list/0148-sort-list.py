# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        lst = []
        node=head
        while node:
            lst.append(node.val)
            node=node.next

        def quickSort(lst):
            if len(lst) <= 1:
                return lst
            left, equal, right = [], [], []
            pivot = lst[len(lst)//2]
            for l in lst:
                if l < pivot:
                    left.append(l)
                elif l > pivot:
                    right.append(l)
                else:
                    equal.append(l)
            
            return quickSort(left) + equal + quickSort(right)

        sortedLst = quickSort(lst)

        answer = ListNode(sortedLst[0])
        curr = answer
        for l in sortedLst[1:]:
            curr.next = ListNode(l)
            curr = curr.next

        return answer
    
    
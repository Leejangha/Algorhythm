# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = [head.val]
        head = head.next

        while head:
            lst.append(head.val)
            head = head.next
        
        for i in range(1, len(lst)):
            key = lst[i]
            j = i -1
            while j >= 0 and lst[j] >= key:
                lst[j+1] = lst[j]
                j -= 1
            lst[j+1] = key
        
        answer = ListNode(lst[0])
        curr = answer

        for i in range(1, len(lst)):
            curr.next = ListNode(lst[i])
            curr = curr.next

        return answer
        
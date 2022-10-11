# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self, l1, l2):
        self.l1 = l1
        self.l2 = l2

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = temp = ListNode(None)
        adv = 0
        while l1 or l2 or adv:
            if l1 and not l2:
                smt = adv + l1.val
            elif l2 and not l1:
                smt = adv + l2.val
            elif l1 and l2:
                smt = adv + l1.val + l2.val
            else:
                smt = adv
            temp.next = ListNode(smt % 10)
            adv = smt // 10
            temp = temp.next
            if l1:
                l1 = l1.next
            else:
                l1 = None
            if l2:
                l2 = l2.next
            else:
                l2 = None
        return l3.next

        def PrintList(self):
            p = ListNode(self)
            while p.next:
                print(p.val, '->', end=' ')
                p = p.next
            print(p.val)


list1 = ListNode(None)
list1.next = ListNode(2)
list1.next.next = ListNode(4)
list1.next.next.next = ListNode(3)
list2 = ListNode(None)
list2.next = ListNode(5)
list2.next.next = ListNode(6)
list2.next.next.next = ListNode(4)
Solution(list1, list2)
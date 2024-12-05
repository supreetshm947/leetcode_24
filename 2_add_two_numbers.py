class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers( l1, l2):
    """
    :type l1: Optional[ListNode]
    :type l2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    dummy = ListNode()
    res = dummy
    carry = 0

    while l1 or l2:
        total = 0
        total += carry
        if l1:
            total += l1.val
            l1 = l1.next
        if l2:
            total += l2.val
            l2 = l2.next
        val = total % 10
        carry = total // 10
        dummy.next = ListNode(val)
        dummy = dummy.next

    return res.next

l1 = [2,4,3]
l2 = [5,6,4]
#ListNode{val: 2, next: ListNode{val: 4, next: ListNode{val: 3, next: None}}}
node1 = ListNode()
n = node1
for i in range(len(l1)):
    n.val = l1[i]
    if i<len(l1)-1:
        n.next = ListNode()
        n=n.next

node2 = ListNode()
n = node2
for i in range(len(l2)):
    n.val = l2[i]
    if i<len(l2)-1:
        n.next = ListNode()
        n=n.next


print(addTwoNumbers(node1, node2))

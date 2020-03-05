# 61

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def rotateRight(head, k):
    if not head:
        return None
    if not head.next:
        return head
    # 将链表连成环
    tail = head
    n = 1
    while tail.next:
        tail = tail.next
        n += 1
    tail.next = head

    # 找到新的表头表尾并断开链表
    new_tail = head
    for _ in range(n - k % n - 1):
        new_tail = new_tail.next
    new_head = new_tail.next
    new_tail.next = None
    return new_head 


head = ListNode(1)
head.next = h2 =  ListNode(2)
h2.next = h3 = ListNode(3)
h3.next = h4 = ListNode(4)
h4.next = h5 = ListNode(5)


temp = rotateRight(head, 7)
for i in range(5):
    print(temp.val)
    temp = temp.next


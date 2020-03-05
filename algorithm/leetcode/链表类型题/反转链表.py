# 206

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 迭代 O(n) O(1)
def ReverseList(head):
    if not head or not head.next:
        return head
    prev = None
    curr = head
    while curr:
        # temp存储curr的下一个节点信息
        temp = curr.next
        # 反转方向
        curr.next = prev
        # 将prev, curr 向后移位
        prev = curr
        curr = temp
    return prev


# 递归
# 时间复杂度：O(n)，假设 n 是列表的长度，那么时间复杂度为 O(n)。
# 空间复杂度：O(n)，由于使用递归，将会使用隐式栈空间。递归深度可能会达到 n 层。


def ReverseList1(head):
    if not head or not head.next:
        return head
    # 递归到最后一个节点
    new_head = ReverseList(head.next)
    # 调转方向
    head.next.next = head
    head.next = None
    return new_head

    

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
head.next.next.next.next.next.next = ListNode(7)
head.next.next.next.next.next.next.next = ListNode(8)


new = ReverseList(head)
cur = head
pre = None
temp = cur.next
cur.next = pre
pre = cur
cur = temp
a = b = 1
print(id(a), id(b))
a = 2
print(id(a), id(b))
print(b)


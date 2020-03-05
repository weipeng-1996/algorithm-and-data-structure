# 148

# 递归归并排序 时间O(nlogn)   空间O(logn)

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def sortList(head):
    if not head or not head.next:
        return head
    fast, slow = head.next, head
    # 找到链表中点
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    # 切割
    mid, slow.next = slow.next, None

    # 递归切割
    left, right = sortList(head), sortList(mid)

    # 合并
    h = res = ListNode(0) # 辅助表头
    while left and right:
        if left.val < right.val:
            h.next, left = left, left.next
        else:
            h.next, right = right, right.next
        h = h.next
    h.next = left or right
    return res.next

    


head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(4)
head.next.next.next = ListNode(6)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(1)
head.next.next.next.next.next.next = ListNode(7)
head.next.next.next.next.next.next.next = ListNode(8)

print(sortList(head))

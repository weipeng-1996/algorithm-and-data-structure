# 141 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 哈希表 时间O(n) 空间O(n)


def hasCycle(head):
    record = {}
    while head:
        try:
            record.pop(head)
            return True
        except:
            record[head] = 1
            head = head.next
    return False


# 快慢双指针 时间O(n) 空间O(1)

def hasCycle1(head):
    if not head or not head.next:
        return False
    fast = head.next
    slow = head
    while slow != fast:
        if fast == None or fast.next == None:
            return False
        slow = slow.next
        fast = fast.next.next
    return True
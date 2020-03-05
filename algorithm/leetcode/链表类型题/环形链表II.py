# 142

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 哈希表


def detectCycle(head):
    record = {}
    while head:
        if not record.get(head):
            record[head] = 1
            head = head.next
        else:
            return head
    return None


# 快慢双指针

def detectCycle1(head):
    if not head or not head.next:
        return None
    fast = head
    slow = head
    while  fast  and  fast.next :
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break 
    if fast == None or fast.next == None:
        return None
    else:
        while fast != head:
            fast = fast.next
            head = head.next
    return head


head = t = ListNode(3)
ce = t.next = ListNode(2)
t.next.next = ListNode(0)
t.next.next.next = ListNode(-1)
t.next.next.next.next = ce

# for i in range(8):
#     print(head.val)
#     head = head.next
print(detectCycle1(head).val)

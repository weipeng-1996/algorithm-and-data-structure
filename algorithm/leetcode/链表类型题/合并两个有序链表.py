class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 利用数组
def mergeTwoLists(l1, l2):
    if not l1 and not l2:
        return None
    t_l1 = l1
    t_l2 = l2
    new_l = ListNode(0)
    arr = []
    while(t_l1):
        arr.append(t_l1.val)
        t_l1 = t_l1.next
    while(t_l2):
        arr.append(t_l2.val)
        t_l2 = t_l2.next
    arr.sort()
    new_l.val = arr[0]
    temp2 = new_l
    for i in range(1,len(arr)):
        temp1 = ListNode(arr[i])
        temp2.next = temp1
        temp2 = temp1
    return new_l

# 将一条链表插入到另一条链表

def charu(l1, l2):
    cur_l = 1
    cur_l2 = 1
    new_l = 1
    if not l1 or not l2:
        if not l1:
            return l2
        else:
            return l1
    # 找到开头小的链表
    if l1.val < l2.val:
        cur_l = l1
        cur_l2 = l2
        new_l = cur_l
    else:
        cur_l = l2
        cur_l2 = l1
        new_l = cur_l
    while 1:
        if cur_l2.val >= cur_l.val and (not cur_l.next or cur_l2.val <= cur_l.next.val):
            temp = cur_l2.next
            cur_l2.next = cur_l.next
            cur_l.next = cur_l2
            cur_l = cur_l.next
            if not temp:
                break
            else:
                cur_l2 = temp
        else:
            cur_l = cur_l.next
    return new_l

# 迭代两链表每次将小的值插入新链表

def diedai(l1, l2):
    new_l = ListNode(None)
    cur_new_l = new_l
    while 1:
        if not l1 or not l2:
            break
        if l1.val < l2.val:
            cur_new_l.next = ListNode(l1.val)
            l1 = l1.next
            cur_new_l = cur_new_l.next
        else:
            cur_new_l.next = ListNode(l2.val)
            l2 = l2.next
            cur_new_l = cur_new_l.next
    if not l1:
        cur_new_l.next = l2
    else:
        cur_new_l.next = l1
    return new_l



if __name__ == '__main__':
    l1 = ListNode(-2)
    l2 = ListNode(-8)
    #l1.next = ListNode(5)
    l2.next = ListNode(-6)
    l2.next.next = ListNode(1)
    l2.next.next.next = ListNode(2)
    l2.next.next.next.next = ListNode(3)
    l2.next.next.next.next.next = ListNode(7)
    l2.next.next.next.next.next.next = ListNode(8)
    nn = charu(l1, l2)
    print(nn)

        



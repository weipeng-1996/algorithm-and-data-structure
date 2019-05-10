class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 130/131 最后一个测试用例超时
def mergeKLists(lists):
    new_list = ListNode(None)
    new_list_cur = new_list
    while lists:
        temp = 99999
        i = 0
        while i < len(lists):
            if lists[i]:
                if lists[i].val < temp:
                    temp = lists[i].val
                    index = i
            else:
                lists.pop(i)
                continue
            i += 1
        if not lists:
            break
        lists[index] = lists[index].next
        new_list_cur.next = ListNode(temp)
        new_list_cur = new_list_cur.next
    return new_list.next

# 利用list
def use_list(lists):
    node = lists[0]
    arr = []
    while lists or node:
        if node:
            arr.append(node)
            node = node.next
        else:
            lists.pop(0)
            if lists:
                node = lists[0]
            else:
                break
    if not arr:
            return
    arr.sort(key = lambda n:n.val)
    for i in range(len(arr)):
        if i == len(arr) - 1:
            arr[i].next = None
            break
        arr[i].next = arr[i+1]
    return arr[0]
        


if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(4)
    l1.next.next = ListNode(5)
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    l3 = ListNode(2)
    l3.next = ListNode(6)
    lists = [l1, l2, l3]
    a = use_list(lists)
    print(use_list(lists))

# 160

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 哈希表 时间O(m+n)   空间O(m)/O(n)
def getIntersectionNode(headA, headB):
    re = {}
    while headA:
        re[headA] = 1
        headA = headA.next
    while headB:
        try:
            re.pop(headB)
            return headB
        except:
            headB = headB.next
    return None


# 双指针 路径长度a + Intersection + b = b + Intersection + a

def getIntersectionNode1(headA, headB):
    if not headA or not headB:
        return None
    h1, h2 = headA, headB
    while h1 != h2:
        h1, h2 = h1.next, h2.next
        if h1 == None and h2 == None:
            return None
        if h1 == None:
            h1 = headB
        if h2 == None:
            h2 = headA
    return h1



tt = ListNode(5)
re = {}
re[tt] = 1
print(re.popitem(tt))
print(re)

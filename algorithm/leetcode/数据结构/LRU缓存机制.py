# 146 
from collections import OrderedDict
class LRUCache1(OrderedDict):

    def __init__(self, capacity):
        self.capacity = capacity

    def get(self, key):
        if key in self:
            self.move_to_end(key)
            return self[key]
        return -1

    def put(self, key, value):
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(False)


# 双向链表 + 哈希实现
class LinkNode:
    def __init__(self):
        self.val = 0
        self.key = 0
        self.next = None
        self.pre = None


class LRUCache:

    def add_node(self, node):
        temp = self.head.next
        self.head.next = node
        node.next = temp
        node.pre = self.head
        temp.pre = node

    def remove_node(self, node):
        pre_node = node.pre
        pre_node.next = node.next
        node.next.pre = pre_node

    def move_to_head(self, node):
        self.remove_node(node)
        self.add_node(node)
    
    def pop_tail(self):
        pre_node = self.tail.pre
        self.remove_node(pre_node)
        return pre_node

    def __init__(self, capacity):
        self.capacity = capacity
        self.catch = {}
        self.size = 0
        self.head, self.tail = LinkNode(), LinkNode()
        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self, key):
        node = self.catch.get(key)
        if not node:
            return -1
        else:
            self.move_to_head(node)
            return node.val
    
    def put(self, key, value):
        node = self.catch.get(key)
        if not node:
            new_node = LinkNode()
            new_node.key = key
            new_node.val = value
            self.add_node(new_node)
            self.catch[key] = new_node
            self.size += 1
            if self.size > self.capacity:
                tail = self.pop_tail()
                del self.catch[tail.key]
                self.size -= 1
        else:
            node.val = value
            self.move_to_head(node)
        




cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
cache.put(3, 3)
print(cache.get(1))
print(cache.get(2))
print(cache.catch)


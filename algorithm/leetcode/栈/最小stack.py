# 155


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.catch = []

    def push(self, x):
        self.catch.append(x)


    def pop(self):
        self.catch.pop()

    def top(self):
        return self.catch[-1]

    def getMin(self):
        min = 9999999999
        for i in self.catch:
            if i < min:
                min = i
        return min

        # Your MinStack object will be instantiated and called as such:
        # obj = MinStack()
        # obj.push(x)
        # obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.getMin()

obj = MinStack()
obj.push(5)
obj.push(1)
obj.push(0)
obj.pop()
param_3 = obj.top()
print(param_3)
param_4 = obj.getMin()
print(param_4)

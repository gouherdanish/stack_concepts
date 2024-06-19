class MyStack:
    def __init__(self) -> None:
        self._arr = []

    def __len__(self):
        return len(self._arr)
    
    def __str__(self) -> str:
        return f'MyStack({self._arr})'
    
    def __repr__(self) -> str:
        return str(self)
    
    def push(self,item):
        self._arr.append(item)

    def pop(self):
        return self._arr.pop()
    
    def isEmpty(self):
        return len(self._arr) == 0
    
    def peek(self):
        return self._arr[-1]
    
if __name__=='__main__':
    stack = MyStack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(stack)
    print(stack.pop())
    print(stack)
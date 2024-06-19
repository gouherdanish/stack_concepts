class MyStack:
    def __init__(self) -> None:
        self._arr = []

    def push(self,item):
        self._arr.append(item)

    def pop(self):
        return self._arr.pop()
    
    def isEmpty(self):
        return len(self._arr) == 0
    
    def peek(self):
        return self._arr[-1]
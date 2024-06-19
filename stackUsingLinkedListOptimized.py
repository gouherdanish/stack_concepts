class ListNode:
    def __init__(self, val=None, next=None) -> None:
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f'Node({self.val})'
    
    def __repr__(self) -> str:
        return str(self)

class SLL:
    def __init__(self) -> None:
        self._head = None
        self._length = 0
    
    def __str__(self) -> str:
        return ','.join([str(node.val) for node in self])
    
    def __iter__(self):
        curr = self._head
        while curr:
            yield curr
            curr = curr.next

    def __len__(self):
        return self._length

    def isEmpty(self):
        """
        O(1)
        """
        return self._head is None
    
    def insert(self,new_val):
        """
        Inserting at the head of the linked list

        O(1)
        """
        new_node = ListNode(new_val)
        if self.isEmpty():
            self._head = new_node
        else:
            new_node.next = self._head
            self._head = new_node
        self._length += 1

    def delete(self):
        """
        Deleting top element from the head of the linked list

        O(1)
        """
        if self._length == 0:
            raise ValueError("Popping from an empty stack")
        elif self._length == 1:
            temp = self._head
            self._head = None
            self._length -= 1
            return temp.val
        else:
            temp = self._head
            self._head = self._head.next
            self._length -= 1
            return temp.val
        
    def peek(self):
        """
        Showing the last element

        O(n) - Since we need to iterate to the end of Linked List
        """
        return self._head.val
        
class MyStack:
    """
    Note - This will be in reverse order of insertion
    i.e. from latest to Old
    """
    def __init__(self) -> None:
        self._sll = SLL()
    
    def __str__(self) -> str:
        return f'MyStack({self._sll})'
    
    def __repr__(self) -> str:
        return str(self)
    
    def __len__(self):
        return len(self._sll)
    
    def push(self,new_val):
        self._sll.insert(new_val)

    def pop(self):
        return self._sll.delete()
    
    def isEmpty(self):
        return self._sll.isEmpty()
    
    def peek(self):
        return self._sll.peek()
        
if __name__=='__main__':
    stack = MyStack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(stack)
    print(stack.pop())
    print(stack)



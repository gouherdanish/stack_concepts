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
        Inserting at the end of the linked list

        O(n) - Since we need to iterate to the end of Linked List
        """
        new_node = ListNode(new_val)
        if self.isEmpty():
            self._head = new_node
        else:
            curr = self._head
            while curr.next:
                curr = curr.next
            curr.next = new_node
        self._length += 1

    def delete(self):
        """
        Deleting last element from the linked list

        O(n) - Since we need to iterate to the end of Linked List
        """
        if self._length == 0:
            raise ValueError("Popping from an empty stack")
        elif self._length == 1:
            temp = self._head
            self._head = None
            self._length -= 1
            return temp.val
        else:
            curr = self._head
            while curr.next.next:
                curr = curr.next
            temp = curr.next
            curr.next = None
            self._length -= 1
            return temp.val
        
    def peek(self):
        """
        Showing the last element

        O(n) - Since we need to iterate to the end of Linked List
        """
        curr = self._head
        while curr.next:
            curr = curr.next
        return curr.val
        
class MyStack:
    """
    Note - This will be in insertion order
    i.e. from old to latest
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



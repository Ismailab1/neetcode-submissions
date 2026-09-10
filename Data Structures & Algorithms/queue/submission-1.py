# Node class to represent each element in the deque
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        # Initialize the deque with dummy head and tail nodes
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    # Check if the deque is empty
    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    # Append a value to the end of the deque
    def append(self, value: int) -> None:
        new_node = Node(value)
        last_node = self.tail.prev

        last_node.next = new_node
        new_node.prev = last_node
        new_node.next = self.tail
        self.tail.prev = new_node

    # Append a value to the beginning of the deque
    def appendleft(self, value: int) -> None:
        new_node = Node(value)
        first_node = self.head.next

        self.head.next = new_node
        new_node.prev = self.head
        new_node.next = first_node
        first_node.prev = new_node

    # Remove and return the value at the end of the deque
    def pop(self) -> int:
        if self.isEmpty():
            return -1  # Return -1 if the deque is empty
        last_node = self.tail.prev
        value = last_node.value
        prev_node = last_node.prev

        prev_node.next = self.tail
        self.tail.prev = prev_node

        return value

    # Remove and return the value at the beginning of the deque
    def popleft(self) -> int:
        if self.isEmpty():
            return -1  # Return -1 if the deque is empty
        first_node = self.head.next
        value = first_node.value
        next_node = first_node.next

        self.head.next = next_node
        next_node.prev = self.head

        return value

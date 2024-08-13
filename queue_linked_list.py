"""
Operations of an Queue
1. Enqueue
2. Dequeue
3. Peek
"""


# linked list
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


# queue
class Queue:
    def __init__(self, max_size=None) -> None:
        self.peek = self.rear = None
        self._size = 0
        self.max_size = max_size

    def is_empty(self):
        return self.peek is None

    def Enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.peek = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def Dequeue(self):
        if self.is_empty():
            raise ValueError("Queue is empty!")
        else:
            item = self.peek.data
            self.peek = self.peek.next
            # Queue 剛好只有一個 element
            if self.peek is None:
                self.rear = None
            self._size -= 1
            return item

    def Peek(self):
        if self.is_empty():
            raise ValueError("Queue is empty!")
        else:
            return self.peek.data


# test
queue = Queue(5)
queue.Enqueue("item1")
# print item1
print(queue.Peek())

queue.Enqueue("item2")
queue.Enqueue("item3")

queue.Dequeue()
# print item2
print(queue.Peek())
queue.Dequeue()
# print item3
print(queue.Peek())

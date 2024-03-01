class Node:
    def_int_(self,data):
        self.data = data
        self.next = None
class QueueLinkList:
    def_int_(self):
        self.front = self.rear = None
    def is_empty(self):
      return self.front is None
    def enqueue(self,item):
       new_node = Node(item)
      if self.is_empty():
       self.front = self.rear = new_node
       else:
       self.rear.next = new_node
       self.rear = new_node
    def dequeue(self):
      if not self.is_empty():
       dequeue = self.front.data
        self.front = self.front.next
      if self.front is None:
         self.rear = None
          return dequeue
       else:
         raise IndexError("Dequeue from an empty queue")
    def front(self):
      if not self.is_empty():
         return self.front.data
       else:
         raise IndexError("Front from an empty queue")
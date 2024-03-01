class QueueArray:
    def_int_(self):
        self.items = []
        def is_empty(self):
        return len(self.item) == 0
        def enqueue(self,item):
            self.items.append(item)
            def dequeue(self):
                if not self.is_empty():
                    return self.items.pop(0)
                    else:
                        raise IndexError("Dequeue from an empty queue")
                        def front(self):
                            if not self.is_empty():
                                return self.item[0]
                                else:
                                    raise IndexError("Front from an empty queue")
                                    def size(self):
                                        return len(self.items)

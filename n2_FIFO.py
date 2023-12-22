class FIFO1:
    def __init__(self, size=5):
        self.max_size = size
        self.queue = []

    def append(self, item):
        self.queue.append(item)

    def get(self):
        return self.queue.pop(0)

    def cycle(self, item):
        pop_item = self.get()
        self.append(item)
        return pop_item


class FIFO2:
    def __init__(self, size=5):
        self.max_size = size
        self.queue = [None] * self.max_size
        self.head = 0
        self.tail = 0

    def append(self, item):
        self.queue[self.head] = item
        self.head = (self.head + 1) % self.max_size

    def get(self):
        item = self.queue[self.tail]
        self.queue[self.tail] = None
        self.tail = (self.tail + 1) % self.max_size
        return item

    def cycle(self, item):
        pop_item = self.get()
        self.append(item)
        return pop_item

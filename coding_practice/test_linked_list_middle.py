class Element:
    def __init__(self, value):
        self.value = value
        self.next = None

    def link_to(self, next_node):
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.current = None

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            current_value = self.current.value
            self.current = self.current.next
            return current_value

    def listify(self):
        self.current = self.head
        while self.current is not None:
            yield self.current.value
            self.current = self.current.next


x = LinkedList()
a = Element("a")
b = Element("b")
c = Element("c")

x.head = a
a.link_to(b)
b.link_to(c)

print([el for el in x])
print([el for el in x.listify()])

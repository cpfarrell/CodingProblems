class node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

class linked_list:
    def __init__(self):
        self.head = None

    def add(self, value):
        if not self.head:
            self.head = node(value, None)
        else:
            self.head = node(value, self.head)

    def delete(self, value):
        self.head = self.find_not(value, self.head)
        cur = self.head
        while cur and cur.next:
            cur.next = self.find_not(value, cur.next)
            cur = cur.next

    def find_not(self, value, cur):
        while cur:
            if cur.value!=value:
                return cur
            cur = cur.next

        return cur

    def path(self):
        cur = self.head
        output = ""

        while cur:
            output += str(cur.value) + ", "
            cur = cur.next
        print output[:-2]


a = linked_list()
a.add(5)
a.add(1)
a.add(2)
a.add(3)
a.add(4)
a.add(5)
a.add(5)
a.add(8)
a.add(5)
a.path()
a.delete(5)
a.path()

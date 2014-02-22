class node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class linked_list:
    def __init__(self):
        self.head = None
        self.height = 0

    def add_node(self, value):
        if self.head:
            self.head =node(value, self.head)
        else:
            self.head =node(value)
            self.height += 1

    def kth_last(self, k):
        fast = self.head
        count = 0
        while count < k and fast:
            count += 1
            fast = fast.next
        assert count==k

        slow = self.head
        while fast:
            fast = fast.next
            slow = slow.next
        return slow.value

    def print_list(self):
        output = ""
        root = self.head
        while root:
            output += str(root.value) + ', '
            root = root.next
        print output[:-2]

a = linked_list()
a.add_node(5)
a.add_node(1)
a.add_node(7)
a.add_node(2)
a.add_node(8)
a.add_node(4)
a.print_list()
print a.kth_last(2)

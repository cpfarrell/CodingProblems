class heap:
    def __init__(self, values=None):
        if not values:
            values = []
        self.heapify(values)

    def heapify(self, values):
        self.array = values
        for i in range(len(values)):
            while self.tri_max(i)!=i:
                self.push_down(i)

    def children(self, i):
        return 2*i + 1, 2*i + 2
    
    def parent(self, i):
        return int((i-1)/2)

    def tri_max(self, i):
        left, right = self.children(i)
        max_child = self.max_arg(left, right)
        return self.max_arg(i, max_child)

    def max_arg(self, i, j):
        if i>=len(self.array):
            return j
        if j >= len(self.array):
            return i

        if self.array[i]>=self.array[j]:
            return i
        else:
            return j

    def swap(self, i, j):
        temp = self.array[i]
        self.array[i] = self.array[j]
        self.array[j] = temp

    def push_down(self, i):
        max = self.tri_max(i)
        if max!=i:
            self.swap(i, max)
            self.push_down(max)

    def push_up(self, i):
        parent = self.parent(i)
        if parent!=-1 and self.array[i]>self.array[parent]:
            self.swap(i, parent)
            self.push_up(parent)

    def peak(self):
        return self.array[0]

    def get_max(self):
        old_max = self.peak()
        bottom = len(self.array)-1
        self.array[0] = self.array[bottom]
        self.array.pop()
        if len(self.array)!=0:
            self.push_down(0)
        return old_max

    def insert(self, value):
        self.array.append(value)
        self.push_up(len(self.array)-1)
            
    def len(self):
        return len(self.array)

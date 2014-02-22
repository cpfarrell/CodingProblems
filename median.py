import my_heap

class median:
    def __init__(self):
        self.lower_half = my_heap.heap()
        self.upper_half = my_heap.heap()
        self.median = None

    def add_value(self, value):
        if self.lower_half.len()==self.upper_half.len():
            self.lower_half.insert(value)
            self.median = self.lower_half.peak()
        else:
            self.upper_half.insert(-1*value)
            lower = self.lower_half.get_max()
            upper = -1*self.upper_half.get_max()
            self.median = (lower+upper)/2.
            self.lower_half.insert(min(lower, upper))
            self.upper_half.insert(-1*max(lower, upper))

med = median()
med.add_value(1)
print med.median
med.add_value(4)
print med.median
med.add_value(6)
print med.median
med.add_value(2)
print med.median
med.add_value(8)
print med.median
med.add_value(10)
print med.median
med.add_value(-10)
print med.median
med.add_value(-4)
print med.median
med.add_value(0)
print med.median
med.add_value(2)
print med.median

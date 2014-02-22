class object:
    def __init__(self, weight, value, index):
        self.weight = weight
        self.value = value
        self.index = index

class object_list:
    def __init__(self, index=-1, previous=None):
        self.index=index
        self.previous = previous

class knapsack:
    def __init__(self, value=0, objects=None):
        self.value = value
        self.objects = objects
        
    #Get the list of items by following the linked list to the bottom
    def get_indices(self):
        objects = self.objects
        indices = ""
        while objects:
            indices = str(objects.index) + ', ' + indices
            objects=objects.previous
        return indices[:-2]

def build_knapsack(objs, max_w):
    knapsacks = [knapsack() for i in range(max_w+1)]
    for obj in objs:
        #Reversed so the object can only be included once for each weight. Without reverse would solve unbounded problem
        for i in reversed(range(obj.weight, len(knapsacks))):
            j = i - obj.weight
            if knapsacks[j].value + obj.value > knapsacks[i].value:
                knapsacks[i] = knapsack(knapsacks[j].value + obj.value, object_list(obj.index, knapsacks[j].objects))
    return knapsacks[max_w]

def max_knapsack(weights, values, max_w):
    objs = [object(w,p,i) for i, (w,p) in enumerate(zip(weights, values))]
    knapsack = build_knapsack(objs, max_w)
    return (knapsack.value, knapsack.get_indices())

import random
weights = [random.randint(1,100) for i in range(10000)]
values = [random.randint(1,100) for i in range(10000)]
print max_knapsack(weights, values, 10000)

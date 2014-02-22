import sys

import string
from collections import deque

#all_words = set(["bad", "bat", "bet", "get", "gel", "dog", "bets", "be", "pony"])
all_words = set([])

letters = string.lowercase

def read_file():
    f = open('scrabbleWords.txt', 'r')
    for line in f:
        all_words.add(line.strip())
read_file()

class node:
    def __init__(self, word, parent):
        self.word = word
        self.parent = parent

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
            self.head = node(value, self.head)
        else:
            self.head = node(value)
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
            

def assemble(end_node):
    path = []
    while end_node:
        path.append(end_node.word)
        end_node = end_node.parent

    print " ".join(path[::-1])

def height(end_node):
    height = 0
    while end_node:
        height += 1
        end_node = end_node.parent
    return height

def permutations(word):
    #Remove letterrs
    new_words = set(word[:position] + word[position+1:] for position in range(len(word)))
    
    #Replace letters
    new_words.update(word[:position] + char + word[position+1:] for char in letters for position in range(len(word)+1))

    #Add letters
    new_words.update(word[:position] + char + word[position:] for char in letters for position in range(len(word)))

    return list(new_words)

def word_path(start, end):
    if start not in all_words:
        print "Given word not in dictionary"
        return

    if end not in all_words:
        print "Termination word not in dictionary"
        return

    known_words = set([start])
    root = node(start, None)

    
    que = deque()

    while True:
        if root.word==end:
            assemble(root)
            return

        for word in permutations(root.word):
             if word in all_words and word not in known_words:
                 que.append(node(word, root))
                 known_words.add(word)

        if len(que)==0:
            break
        root = que.popleft()

    print root.word
    print "No path between the words exist, search height was " + str(height(root))

word_path(sys.argv[1], sys.argv[2])

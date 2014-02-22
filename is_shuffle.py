class node:
    def __init__(self, letter, prev, next):
        self.letter = letter
        self.prev = prev
        self.next = next

class linked_list():
    def __init__(self, head=None, cur=None):
        self.head = head
        self.cur = cur

    def add(self, letter):
        if not self.head:
            self.head=node(letter, None, None)
        else:
            old_head = self.head
            self.head = node(letter, None, old_head)
            old_head.prev = self.head

    def reset_cur(self):
        self.cur = self.head

    def remove(self, letter):
        while self.cur:
            #Found match, remove letter from list
            if self.cur.letter==letter:
                #Cur is not head or tail
                if self.cur.prev and self.cur.next:
                    self.cur.prev.next = self.cur.next
                    self.cur.next.prev = self.cur.prev
                #Cur is tail and not head
                elif self.cur.prev:
                    self.cur.prev.next = None
                #Cur is head and not tail
                elif self.cur.next:
                    self.cur.next.prev = None
                    self.head = self.cur.next
                #Cur is both head and tail
                else:
                    self.head = None

                self.cur = self.cur.next
                return True

            else:
                self.cur = self.cur.next

        return False

def shuffle_both(str1, str2, str3):
    return is_shuffle(str1, str2, str3) or is_shuffle(str2, str1, str3)


def is_shuffle(str1, str2, str3):
    #If lengths don't match can't be a shuffle
    if len(str3) != len(str1) + len(str2):
        return False

    str3_ll = linked_list()
    for char in reversed(str3):
        str3_ll.add(char)

    if not remove_string(str1, str3_ll):
        return False

    return remove_string(str2, str3_ll)

def remove_string(small, big):
    big.reset_cur()
    for let in small:
        if not big.remove(let):
            return False

    return True

print shuffle_both("abc", "def", "adbecf")
print shuffle_both("abc", "aef", "abecf")
print shuffle_both("abc", "aef", "aabecf")
print shuffle_both("abc", "def", "abdecfg")
print shuffle_both("abc", "def", "bdaecf")
print shuffle_both("abc", "def", "aedbcf")
print shuffle_both("aa", "aaf", "aafaa")
print shuffle_both("aaf", "aa", "aafaa")
print shuffle_both("aaf", "aaf", "faafaa")

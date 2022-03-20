class ItemExistsException(Exception):
    pass

class NotFoundException(Exception):
    pass

class Node:
    def __init__(self, key=None, data=None, next=None):
        self.key = key
        self.data = data
        self.next = next
        
    

class Bucket:
    def __init__(self):
        self.head = Node()
        self.size = 0

    def _find_key_recur(self, key, node):
        """Recursive fall sem athugar hvort að nóðann sé nú þegar til,
            ef nóðann er til þá skilar hann nóðunni."""
        if node == None:
            return
        elif node.key == key:
            return node
        else:
            return self._find_key_recur(key, node.next)

    def insert(self, key, data):
        no_key = self.contains(key)
        if no_key:
            if self.head.key == None:
                    self.head.key = key
                    self.head.data = data
                    self.size += 1
            else:
                new_node = Node(key, data, self.head)
                self.head = new_node
                self.size += 1
        else:
            raise ItemExistsException()

    def update(self, key, data):
        node = self._find_key_recur(key, self.head)
        if node != None:
            node.data = data
        else:
            raise NotFoundException()

    def find(self, key):
        node = self._find_key_recur(key, self.head)
        if node != None:
            return node.data
        raise NotFoundException()

    def contains(self, key):
        node = self._find_key_recur(key, self.head)
        if node != None:
            return True
        return False

    def _rem_helper(self, key, node):
        if node == None:
            return
        elif node.next.key == key:
            return node
        else:
            self._rem_helper(key, node.next)

    def remove(self, key):
        node = self._find_key_recur(key, self.head)
        if node != None:
            if node == self.head: #Ef hann er fremstur
                if node.next == None: #Ef það er engin önnur nóða
                    self.head = None
                else:
                    self.head = node.next
            elif node.next == None: #Ef hann er aftastur
                node = None
            else:
                node.next = node.next.next
            self.size -= 1
        else:
            raise NotFoundException()

    def __setitem__(self, key, data):
        node = self._find_key_recur(key, self.head)
        if node != None:
            node.data = data
        else:
            if self.head.key == None:
                self.head.key = key
                self.head.data = data
                self.size += 1
            else:
                new_node = Node(key, data, self.head)
                self.head = new_node
                self.size += 1

    def __getitem__(self, key):
        node = self._find_key_recur(key, self.head)
        if node != None:
            return node.data
        raise NotFoundException()

    def __len__(self):
        return self.size


bucket = Bucket()
print(dir(bucket))
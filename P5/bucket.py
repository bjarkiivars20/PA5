class ItemExistsException(Exception):
    pass

class NotFoundException(Exception):
    pass

class Node:
    def __init__(self, key=None, data=None, next=None):
        self.key = key
        self.data = data
        
    

class Bucket:
    def __init__(self, next=None):
        self.next = next

    def insert(key, data):
        new = Node(key,data)
        

    def update(key, data):
        pass

    def find(key):
        pass

    def contains(key):
        pass

    def remove(key):
        pass

    def __setitem__(self, key, data):
        pass

    def __getitem__(self, key):
        pass

    def __len__(self):
        pass
from array import array
from bucket import Bucket, NotFoundException, ItemExistsException

"""
When the number of items in the HashMap has reached 120% of the number of buckets (length of array or list) 
it must rebuild(), doubling the number of buckets. 
"""

class HashMap:
    def __init__(self):
        self.capacity = 8
        self.size = 0
        self.array = [Bucket() for _ in range(self.capacity)]

    def _find_index(self, key):
        """Hjálparfall sem skilar indexnum á því hvar við ætlum að endurraða fötunum"""
        if type(key) == int:
            array_index = key % self.capacity
        elif type(key) == str:
            first_char = key[0].lower()
            int_value = ord(first_char) - ord('a') #Berum saman muninn á fyrsta stafnum í lyklinum og 'a', fáum út heiltölu gildi og notum modulus við það
            array_index = int_value % self.capacity
        return array_index

    def _reorder_bucket_nodes_recur(self, node):
        """Hjálparfall sem endurraðar nóðunnum í nýja fylkið"""
        if node == None:
            return
        else:
            self.array.insert(node.key, node.data)
            self._reorder_bucket_nodes_recur(node.next)

    def rebuild(self):
        """"""
        self.capacity *= 2
        temp_array = self.array #Ætti að geyma gömlu útgáfunna af self.array
        self.array = [Bucket() for _ in range(self.capacity)]
        for bucket in temp_array:
            self._reorder_bucket_nodes_recur(bucket.head)
                
    def _find_bucket(self, key):
        """Hjálparfall sem skilar bucket tilvikinu sem lykillinn á að vera í"""
        if type(key) == int:
            array_index = key % self.capacity
        elif type(key) == str:
            first_char = key[0].lower()
            int_value = ord(first_char) - ord('a') #Berum saman muninn á fyrsta stafnum í lyklinum og 'a', fáum út heiltölu gildi og notum modulus við það
            array_index = int_value % self.capacity
        else:
            raise AttributeError()
        bucket = self.array[array_index]
        return bucket        

    def insert(self, key, data):
        """Adds this value pair to the collection 
            ○ If equal key is already in the collection, raise ItemExistsException() """
        over_sized = round(self.capacity * 1.2)
        total_amount = self._return_total_length()
        if over_sized <= total_amount:
            self.rebuild()
        bucket = self._find_bucket(key)
        bucket.insert(key, data)
        if bucket.head.key == None:
            self.size += 1
    def update(self, key, data):
        """○ Sets the data value of the value pair with equal key to data 
            ○ If equal key is not in the collection, raise NotFoundException()"""
        bucket = self._find_bucket(key)
        bucket.update(key, data)           
    
    def find(self, key):
        """○ Returns the data value of the value pair with equal key 
            ○ If equal key is not in the collection, raise NotFoundException()"""
        bucket = self._find_bucket(key)
        data = bucket.find(key)
        return data

    def contains(self, key):
        """Returns True if equal key is found in the collection, otherwise False """
        bucket = self._find_bucket(key)
        key_exists = bucket.contains(key)
        if key_exists:
            return True
        return False

    def remove(self, key):
        """Removes the value pair with equal key from the collection 
            ○ If equal key is not in the collection, raise NotFoundException()"""
        bucket = self._find_bucket(key)
        bucket.remove(key)
        if bucket.head == None:
            self.size -= 1

    def __setitem__(self, key, data):
        """○ Override to allow this syntax: 
                ■ some_hash_map[key] = data 
            ○ If equal key is already in the collection, update its data value 
                ■ Otherwise add the value pair to the collection"""
        bucket = self._find_bucket(key)
        bucket[key] = data

    def __getitem__(self, key):
        """○ Override to allow this syntax: 
                ■ my_data = some_hash_map[key] 
            ○ Returns the data value of the value pair with equal key 
            ○ If equal key is not in the collection, raise NotFoundException() """
        bucket = self._find_bucket(key)
        data = bucket[key]
        return data

    def __len__(self):
        """○ Override to allow this syntax: 
                ■ length_of_structure = len(some_hash_map) 
            ○ Returns the number of items in the entire data structure """
        total_amount = self._return_total_length()
        return total_amount
    
    def _return_total_length(self):
        total_amount = 0
        amount_in_buckets = 0
        for bucket in self.array:
            amount_in_buckets += bucket.size 
        total_amount = self.size + amount_in_buckets
        return total_amount


import random
import sys
import string

class MyHashableKey:
    def __init__(self, int_value, string_value):
        """A constructor that takes an integer value and a string value"""
        self.int_value = int_value
        self.string_value = string_value
    
    def __eq__(self, other):
        """Compares two instances of MyHashableKey and returns True if their values are 
            equal, otherwise False. """
        return self.int_value == other.int_value and self.string_value == other.string_value
        

    def __hash__(self):
        """Returns a positive integer The integer value must be the same for instances that are equal 
            Otherwise can be any integer"""
        hash_value = 1
        increment = self.int_value
        for char in self.string_value:
            hash_value *= (ord(char) + increment)
            increment += self.int_value
        return hash_value

if __name__ == '__main__':
    """TESTING"""
    # m = MyHashableKey(1, "Strengur")
    # print(hash(m))
    # m2 = MyHashableKey(2, "Skoli")
    # print(hash(m2))
    # m3 = MyHashableKey(3, "Pirrandi")
    # print(hash(m3))
    # m4 = MyHashableKey(4, "Verkefni")
    # print(hash(m4))
    # m5 = MyHashableKey(5, "Eyjafjallajökull")
    # print(hash(m5))
    # m6 = MyHashableKey(6, "maszproblem")
    # print(hash(m6))
    # print(m2 == m3)

    # """Profa dreyfingu á hashinu:"""
    # lis_size = 1000
    # lis = [0] * lis_size
    # for _ in range(1000000):
    #     S = random.randint(1,40)
    #     ran = ''.join(random.choices(string.ascii_letters + string.digits, k = S))
    #     mhk = MyHashableKey(random.randint(1, 10000), ran)
    #     index = hash(mhk) % lis_size
    #     lis[index] += 1

    # print(lis)
    



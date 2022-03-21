class Node:
    def __init__(self, key = None, data = None):
        self.key = key
        self.data = data

print(hash("p"))

str1 = "p"
str2 = "p"

print(hash(str1), hash(str2))
print(hash(str1) == hash(str2))

#range(-999.., +999..)
#
#-999..
#0
#+999..
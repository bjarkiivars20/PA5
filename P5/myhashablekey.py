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
        
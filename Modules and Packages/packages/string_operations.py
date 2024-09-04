class StringOperations:
    def __init__(self, s):
        self.s = s

    def to_uppercase(self):
        return self.s.upper()

    def to_lowercase(self):
        return self.s.lower()

    def reverse_string(self):
        return self.s[::-1]

    def count_vowels(self):
        vowels = 'aeiouAEIOU'
        return sum(1 for char in self.s if char in vowels)

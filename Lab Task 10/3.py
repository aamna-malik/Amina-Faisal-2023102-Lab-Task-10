class ReverseIterator:
    def __init__(self, sequence):
        self.sequence = sequence
        self.index = len(sequence)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > 0:
            self.index -= 1
            return self.sequence[self.index]
        raise StopIteration

# Test the iterator with a list of strings
string_list = ["apple", "banana", "cherry", "date", "fig"]

reverse_iterator = ReverseIterator(string_list)

print("Original List:", string_list)
print("Reverse Order:", list(reverse_iterator))

class UniqueIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.seen = set()
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.iterable):
            current_element = self.iterable[self.index]
            self.index += 1
            if current_element not in self.seen:
                self.seen.add(current_element)
                return current_element
        raise StopIteration

# Test the iterator with a list containing duplicates
my_list = [1, 2, 3, 2, 4, 5, 3, 6, 7, 6, 8, 9]

unique_iterator = UniqueIterator(my_list)

print("Original List:", my_list)
print("Unique Elements:", list(unique_iterator))

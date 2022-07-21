class Reverse:

    def __init__(self, initial_list):
        self.initial_list = initial_list
        self.index = len(initial_list)

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.initial_list[self.index]


ls = [10, 20, 30]
for it in Reverse(ls):
    print(it)
print(ls)
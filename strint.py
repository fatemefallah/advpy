import re

class Strint(int):
    
    def __lt__(self, other):
        return str(self)[-1] < str(other)[-1]

    def __gt__(self, other):
        return str(self)[-1] > str(other)[-1]

    def __le__(self, other):
        return str(self)[-1] <= str(other)[-1]

    def __ge__(self, other):
        return str(self)[-1] >= str(other)[-1]

    def __eq__(self, other):
        return str(self)[-1] == str(other)[-1]

    def __ne__(self, other):
        return str(self)[-1] != str(other)[-1]

    def __add__(self, other):
        return int(str(self) + str(other))

    def __sub__(self, other):
        sub_res = int(re.sub(str(other),"", str(self)))
        if sub_res < 0:
            raise 'The subtraction is not valid'
        else:
            return sub_res

    def __len__(self):
        return len(str(self))

    def __call__(self):
        pass


a = Strint(8439)
b = Strint(39)
d = b - a
print(d)
print(type(d))
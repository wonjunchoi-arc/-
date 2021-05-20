def add_function(first, second):
    return first + second
def sub_function(first, second):
    return first - second
def mul_function(first, second):
    return first * second
def div_function(first, second):
    return first / second



class Calculator:

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        return c.first + c.second
    def sub(self):
        return c.first - c.second
    def mul(self):
        return c.first * c.second
    def div(self):
        return c.first / c.second

if __name__ == '__main__':
    print(add_function(4, 7))
    print(sub_function(4, 7))
    print(mul_function(4, 7))
    print(div_function(4, 7))


    c = Calculator()
    ''''''
    c.setdata(1, 2)
    print(c.add())
    print(c.sub())
    print(c.mul())
    print(c.div())
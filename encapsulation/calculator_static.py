class Calculator_static(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        return self.first + self.second
    def sub(self):
        return self.first - self.second
    def mul(self):
        return self.first * self.second
    def div(self):
        return self.first / self.second

    @staticmethod #어노테이션
    def main():
        calc = Calculator_static(int(input('첫번째 수 입력')), int(input('두번째 수 입력')))
        print(f'{calc.first} + {calc.second} = {calc.add()}')
        print(f'{calc.first} - {calc.second} = {calc.sub()}')
        print(f'{calc.first} * {calc.second} = {calc.mul()}')
        print(f'{calc.first} / {calc.second} = {calc.div()}')

Calculator_static.main()



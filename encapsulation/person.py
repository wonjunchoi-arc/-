'''
이름, 출생년도, 주소를 입력받아서
회원가인한 사람의 이름, 나이(만), 주소를 출력하시오
'''

class Member:
    def __init__(self, first, second, third,):
        self.first = first
        self.second = second
        self.third = third

    def sub(self):
        return 2021 - self.second


    @staticmethod
    def main():
        m = Member(input('이름: '), int(input('출생년도: ')), (input('주소: ')))#숫자를 기계어로 입력해주기 위해서는 int 필수
        print(f'이름: {m.first}') #계산식이 아닌 단수 값을불러오기 때문에 뒤의 가로는 필요없는듯
        print(f'나이: {m.sub()}')
        print(f'주소: {m.third}')




Member.main()
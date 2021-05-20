class Stock(object):
    def __init__(self, name, number):
        self.name = name
        self.number =number

    def get_Stock(self):
        return f'종목명 {self.name}, 종목번호{self.number}'

    @staticmethod
    def main():
        ls = []
        while 1:
            menu = input('0 Exit 1.입력 2.출력 3.삭제')
            if menu == '0':
                break
            elif menu == '1':
                ls.append(Stock(input('종목명')), int(input('종목번호')))

            elif menu == '2':
                for i in ls:
                    print(f'출력결과: {i.get_Stock()}')

            elif menu == '3':
                del_Stock = input('삭제할 주식: ')

            else:
                print('잘못된 주문 입니다.')
                continue
Stock.main()









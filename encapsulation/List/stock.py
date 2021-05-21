class Stock(object):
    def __init__(self, name, number):
        self.name = name
        self.number =number

    def to_string(self):
        return f'종목명 {self.name}, 종목번호{self.number}'



    @staticmethod
    def del_element(ls, name):  # (ls, name)을 모두 주는 이유
        for i, j in enumerate(ls):
            if j.name == name:
                del ls[i]


    @staticmethod
    def main():
        ls = []
        while 1:
            menu = input('0 Exit 1.입력 2.출력 3.수정 4.삭제')
            if menu == '0':
                break
            elif menu == '1':
                ls.append(Stock(input('종목이름'), input('종목코드')))

            elif menu == '2':
                for i in ls:
                    print(f'출력결과값: {i.to_string()}')

            elif menu == '3':
                name = input("수정할 이름 :")
                stock = Stock(input("종목이름:"), input("종목번호 : "))   ##순서가 수정할 이름 삭제, 추가 아닌가?
                stock.del_element(ls, name)
                ls.append(stock)

            elif menu == '4':
                name = input('삭제할 주식:')
                stock.del_element(ls, input('종목코드'))  # 종목코드 넣는것 이해 안감

            else:
                print('잘못된 입력입니다.')
                continue




Stock.main()









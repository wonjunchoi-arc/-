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
            menu = input('0 Exit 1.입력 2.출력 3.수정 4.삭제')
            if menu == '0':
                break
            elif menu == '1':
                ls.append(Stock(input('종목명'), input('종목코드')))

            elif menu == '2':
                for i in ls:
                    print(f'출력결과값: {i.get_Stock()}')

            elif menu == '3':
                edit_name = input("수정할 이름 :")
                edit_info = Stock(input("종목이름:"), input("종목번호 : "))
                for i,j in enumerate(ls):
                    if j.name == edit_name:
                        del ls[i]
                        ls.append(edit_info)



            elif menu == '4':
                del_name = input('삭제할 주식:')
                for i, j in  enumerate(ls):
                    if j.name == del_name:
                        del ls[i]


Stock.main()









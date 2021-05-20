
'''
이름,전화번호,이메일,주소를 받아서 연락처 입력,출력,삭제하는 프로그램을 완성하시오.
'''

class Contacts(object):
    def __init__(self, name, ph, em, ad):
        self.name = name
        self.ph = ph
        self.em = em
        self.ad = ad

    def get_Contacts(self):
        return f'이름: {self.name}, 전화번호: {self.ph}, 이메일:{self.em} 주소: {self.ad}'

    @staticmethod
    def main():
        ls = []
        while 1:
            menu = input('0.그만 1.입력 2.출력 3.삭제')
            if menu == '0':
                break
            elif menu == '1':
                ls.append(Contacts(input('이름'), input('전화번호'), input('이메일'), input('주소:')))

            elif menu == '2':
                for i in ls:
                    print(f'출력결과 : {i.get_Contacts()}')


            elif menu == '3':
                del_name = input('삭제할 이름:')
                for i, j in enumerate(ls):
                    if j.name == del_name:
                        del ls[i]

            else:
                print('잘못된 주문입니다.')
                continue


Contacts.main()

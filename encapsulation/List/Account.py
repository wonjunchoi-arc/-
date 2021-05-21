import random

class Account(object):
    def __init__(self, account_number, name, money):
        self.BANK_NAME = 'SC 은행'
        self.account_number = account_number
        self.name = name
        self.money = money
    '''
    계좌번호는 3자리-2자리-6자리 형태로 랜덤하게 생성됩니다.
    '''
    @staticmethod
    def create_account_number():
        ls = [str(random.randint(0, 9)) for i in range(3)]  #이 항목을 왜 주신거지??
        ls.append('-')
        for i in range(2): #range 돈다는 뜻
            ls.append(str(random.randint(0, 9)))
        ls.append('-')
        for i in range(6):
            ls.append(str(random.randint(0, 9)))
        return ''.join(ls)


    def to_string(self):
        return f'Bank Name: {self.BANK_NAME} Name: {self.name}, account_number{self.account_number}, Money:{self.money}'


    @staticmethod
    def del_account(ls, account_number):
        for i, j in enumerate(ls):
            if j.account_number == account_number:
                del ls[i]

    @staticmethod
    def main():
        ls = []
        while 1:
            menu = input('0.종료 1.계좌개설 2.계좌목록 3.입금 4.출금 5. 계좌탈퇴')
            if menu == "0":
                break
            elif menu == "1":
                ls.append(Account(Account.create_account_number(),input('name'), input('money')))

            elif menu == "2":
                for i in ls:
                    print(i.to_string())

            elif menu =="3":
                account_number = input('입금할 계좌번호')
                money = input('입금액 입력바랍니다')
                for i, j in enumerate(ls):
                    if j.account_number == account_number:
                        replace = Account(j.account_number, j.name, int(j.money)+int(money)) #입금 +
                        Account.del_account(ls, account_number)
                        ls.append(replace)

            elif menu == "4":
                account_number = input('출금할 계좌번호')
                money = input('출금액 입력바랍니다.')
                for i, j in enumerate(ls):
                    if j.account_number == account_number:
                        replace =Account(j.account_number,j.name,int(j.money)-int(money))#출금
                        Account.del_account(ls, account_number)
                        ls.append((replace))

            elif menu == '5':
                Account.del_account((ls, input('삭제할 계좌번호')))
            else:
                print('Worng Number')
                continue

Account.main()















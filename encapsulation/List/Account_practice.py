import random
class Account(object):
    def __init__(self, name, money, account_number):
        self.BANK_NAME = 'SC은행'
        self.name = name
        self.money = money
        self.account_number = None


    @staticmethod
    def create_account_number():
        ls = [str(random.randint(0, 9)) for i in range(3)]
        ls.append('-')
        for i in range(2):
            ls.append(str(random.randint(0,9)))
            ls.append('-')
        for i in range(6):
            ls.append(str(random.randint(0,9)))
            ls.append('-')
        return ''.join(ls)


    def to_string(self):
        return f'은행명: {self.BANK_NAME}, 예금주: {self.name}, 잔액: {self.money}, 계좌번호: {self.account_number}'

    @staticmethod


    @staticmethod
    def main():
        ls = []
        while 1:
            menu = input('0.종료 1.계좌개설 2.계좌목록 3.입금 4.출금 5.계좌폐지')
            if menu == '0':
                break
            elif menu == '1':
                ls.append(Account(Account.create_account_number(), input('예금주:'), input('잔액:')))

            elif menu == '2':
                for i in ls:
                    print(i.to_string())

            elif menu == '3':
                account_numbers = input('입금할 계좌를 선택해 주세요')
                money = input('입금할 금액을 입력해 주세요')
                for i, j in enumerate(ls):
                    if j.account_number == account_numbers:
                        replace()
                        Account.del_account









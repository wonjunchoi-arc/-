
class Account(object):
    def __init__(self, name, mo):
        self.name = name
        self.mo = mo

    def get_Account(self):
        return f'은행이름: sc은행, 예금주: {self.name}, 계좌번호:  초기잔액: {self.mo}'


    @staticmethod
    def main():
        








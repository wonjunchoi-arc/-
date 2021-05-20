class Grade:
    def __init__(self, eng, math, korean):
        self.eng = eng
        self.math = math
        self.korean = korean

    def sum(self):
            return self.eng + self.math + self.korean

    def avg(self):
            return int(self.sum() / 3)

    def get_grade(self):
        score = int(self.avg())
        if score >= 90:
            grade = 'A학점'
        elif score >= 80:
            grade = 'B학점'
        elif score >= 70:
            grade = 'C학점'
        elif score >= 60:
            grade = 'D학점'
        elif score >= 50:
            grade = 'E학점'
        else:
            grade = 'F학점'


        return grade

    @staticmethod
    def main():
        g = Grade(int(input('영어점수: ')), int(input('수학점수: ')), int(input('국어점수: ')))
        print(f'총점: {g.sum()}') #여기서 f는 무엇을 의미하는거지???
        print(f'평균: {g.avg()}')
        print(f'학점: {g.get_grade()}')

Grade.main()




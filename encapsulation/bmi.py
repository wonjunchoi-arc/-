def bmi_function(height, weight):
    return weight / height **2 * 10000

class Bmi(object):#여기에 오브젝트를 넣는 이유는???
    def __init__(self, height, weight):
        self.weight = weight
        self.height = height

    def get_Bmi(self):
        bmi = ''
        index = self.weight / self.height ** 2 * 10000
        if index > 30:
            bmi = '초고도 비만'
        elif 25< index <= 30:
            bmi = '비만'
        elif 23 < index <= 25:
            bmi = '과체중'
        elif 18.5 < index <= 23:
            bmi = '정상'
        else:
            bmi = '저체중'

        return bmi

    def get_grade(self):
        score = int(self.get_Bmi())



    @staticmethod
    def main():
        b = Bmi(int(input('키 입력(cm)')), int(input('몸무게 입력(kg)')))
        print(b.get_Bmi())


Bmi.main()



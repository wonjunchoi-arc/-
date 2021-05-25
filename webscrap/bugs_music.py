from bs4 import BeautifulSoup
from urllib.request import urlopen

class BugsMmusic(object):

    url = ''

    def __str__(self):
        return self.url


#https://music.bugs.co.kr/chart/track/realtime/total?wl_ref=M_contents_03_01
    @staticmethod
    def main():
        bugs =BugsMmusic()
        while 1:
            menu = input('0.Exit 1.URL을 입력해 주세요 2.Get Rank URL 3. 4.')
            if menu == '0':
                break
            elif menu == '1':
                bugs.url = input('Input URL')
            elif menu == '2':
                print(f'Input URL is : {bugs}')
                soup = BeautifulSoup(urlopen(bugs.url), 'lxml')
                count = 0
                print('------------ARTIST RANKING-----------------')
                for i in soup.find_all(name='p', attrs=({"class": "artist"})):  # soup의 모두 찾음 중 (즉 가져온 HTML중) <p class="title" adult_yn="N"><p class="title" adult_yn="N"> </p> 즉 노래이름 부분
                                              # <p class="artist"> </p> 이 두부분을 리스트안에 넣기 시작하겠다는 거   #여기서의 name, attrs는 크롤링에서 지정된 함수인자이다.  즉 프레임워크


                    count += 1  # 랭크의 숫자를 만들어 내는 곳
                    print(f'{str(count)} RANKING')
                    print(f'ARTIST:{i.find("a").text}') #


                print('----------------------TITLE RANKING------------------')
                count = 0
                for i in soup.find_all(name='p', attrs=({"class":"title"})):
                    count += 1
                    print(f'{str(count)} RANKING')
                    print(f'TITLE:{i.find("a").text}')





            else:
                print('잘못된 입력입니다')
                continue
BugsMmusic.main()







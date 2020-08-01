import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

# db를 셋팅 -> html에서 가져온 정보를 db에 insert
client = MongoClient('localhost', 27017)
db = client.dbsparta

# 지니뮤직 사이트에서 html가져오기
# html을 못 끌어오면 header 정보 확인
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
response = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200713',headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# 가져온 html에서 select로 추출
musics = soup.select('table.list-wrap tbody tr.list')
# print(musics)

# 1~50위까지 순위, 제목, 가수 출력
# .number , .info a.title , .info a.artist
for music in musics:
    # print(music)
    music_rank = music.select_one('.number').contents[0].strip()
    music_title = music.select_one('.info a.title').contents[0].strip()
    music_artist = music.select_one('.info a.artist').text

    pretty = {
        'rank': music_rank,
        'title': music_title,
        'artist': music_artist
    }

    # db.genie_music.insert_one(pretty)








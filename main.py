from bs4 import BeautifulSoup
import requests


res = []
artist_name = "Olga Buzova"

song_name = "Not Enough Soulmates"

artist_name = artist_name.split(' ')

artist_name[0] = artist_name[0].capitalize()

artist = '-'.join(artist_name)

song_name = song_name.split(' ')

song_title = '-'.join(song_name)

link = f"https://genius.com/{artist}-{song_title}-lyrics"

result = str(requests.get(link).content.decode('utf-8')).replace('<br/>', '\n')

soup = BeautifulSoup(result, "html.parser")

parts = soup.find_all("div", {"class": "Lyrics__Container-sc-1ynbvzw-1"})

for part in parts:
    strings = part.text.split('\n')
    for string in strings:
        if string != "":
            res.append(string)

final_text = '\n'.join(res)

print(final_text)






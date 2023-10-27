from bs4 import BeautifulSoup
import requests
import ftfy


res = []
artist_name = "morgenshtern"

song_name = "leck"

artist_name = artist_name.split(' ')

artist_name[0] = artist_name[0].capitalize()

artist = '-'.join(artist_name)

song_name = song_name.split(' ')

song_title = '-'.join(song_name)

link = 'https://genius.com/#top-songs'

result = str(requests.get(link).content).replace('<br/>', '\n')


soup = BeautifulSoup(result, "html.parser")

parts = soup.find_all("div", {"class": "Lyrics__Container-sc-1ynbvzw-1"})

for part in soup:
    strings = part.text.split(' ')

    repaired = [ftfy.fix_text(elem) for elem in strings]
    res.append(repaired)

print(res)

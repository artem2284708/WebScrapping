from bs4 import BeautifulSoup
import requests
import argparse

parser = argparse.ArgumentParser(description="Parse and display the top N songs from Genius.com")
parser.add_argument("-n", "--top", type=int, help="Number of top songs to display")
args = parser.parse_args()

link = 'https://genius.com/#top-songs'
response = requests.get(link)
soup = BeautifulSoup(response.content.decode('utf-8'), "html.parser")

div_element = soup.find_all("div", {"class": "ChartSongdesktop__Title-sc-18658hh-3 fODYHn"})

k = 1
if args.top is not None:
    num_songs_to_display = min(args.top, len(div_element))
else:
    num_songs_to_display = len(div_element)

for i in div_element[:num_songs_to_display]:
    text = i.get_text()
    print(k, ":   ", text)
    k += 1


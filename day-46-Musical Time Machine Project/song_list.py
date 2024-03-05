import requests
from bs4 import BeautifulSoup


class SearchSong:
    def __init__(self, date):
        self.date = date
        self.url = f"https://www.billboard.com/charts/hot-100/{self.date}/"
        self.song_list = []
        self.search_song_list()

    def search_song_list(self):
        response = requests.get(self.url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        chart = soup.find_all(name="div", class_="o-chart-results-list-row-container")

        for song_container in chart:
            song = song_container.find(name="h3")
            # remove clutter from song
            song_name = song.string.replace("\n", "").replace("\t", "")
            self.song_list.append(song_name)







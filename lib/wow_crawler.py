import logging
import re
import requests
from bs4 import BeautifulSoup

from lib.wow_constants import BASE_URL
from lib.wow_info import WOWStage, WOWLevel


class Crawler:
    __response = ""
    __soup = None
    __main_page_data = []
    __current_index = 0
    __current = None

    def __main_page(self, url):
        self.__response = requests.get(url)
        self.__soup = BeautifulSoup(self.__response.content, "html.parser")
        links = self.__soup.find_all("a", {"class": "na"})
        stages = []

        for link in links:
            match = re.match(r'(.+?) - (.+?) \((\d+-\d+)\)', link.text)

            country = ""
            landmark = ""

            if match:
                country = match.group(1)
                landmark = match.group(2)

            level_ref = link["href"]

            stages.append(WOWStage(country, landmark, BASE_URL + level_ref))

        return stages

    def __level_data(self, url):
        self.__response = requests.get(url)
        self.__soup = BeautifulSoup(self.__response.content, "html.parser")
        links = self.__soup.find_all("a", {"class": "na"})
        levels = []

        for link in links:
            match = re.match(r'(.+?) - (.+?) - \((.+?)\)', link.text)

            level = 0
            letters = ""
            words_href = link["href"]

            if match:
                level = match.group(2).split(" ")[1]
                letters = match.group(3)

            levels.append(WOWLevel(level, letters, BASE_URL + words_href))

        return levels

    def __word_data(self, url):
        self.__response = requests.get(url)
        self.__soup = BeautifulSoup(self.__response.content, "html.parser")
        word_table = self.__soup.find("div", {"class": "words"})
        return word_table.text.strip().split("\n")

    def crawl(self):
        logging.info("Fetching all stages basic information")
        self.__main_page_data = self.__main_page(BASE_URL)

    def has_next(self):
        return self.__current_index < (len(self.__main_page_data) - 1)

    def next(self):
        if self.has_next():
            self.__current = self.__main_page_data[self.__current_index]
            self.__current_index += 1
            return self.__current
        else:
            return None

    def current(self):
        return self.__current

    def current_stage(self):
        logging.info("Getting current stages")
        stage = self.current()

        logging.info(f"{stage.country} - {stage.landmark}")

        levels = self.__level_data(stage.levels_href)

        for l in range(len(levels)):
            logging.info(f"\t{levels[l].level_number} - {stage.landmark}")
            answers = self.__word_data(levels[l].answers_href)
            logging.info(f"\t\t{answers}")
            levels[l].answers = answers

        stage.levels = levels

        return stage

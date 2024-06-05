import json
from abc import ABC, abstractmethod
import requests


class Parser(ABC):
    """Abstract class for working with websites API with vacancies"""
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def load_vacancies(self, keyword):
        pass


class HH(Parser):
    """class for working with HeadHunter API"""

    def __init__(self):
        self.area = 113  # Russia by default
        self.url = 'https://api.hh.ru/vacancies'
        self.vacancies = []
        self.params = {'area': self.area, 'text': ''}

    def load_vacancies(self, keyword=''):
        self.params['text'] = keyword  # adding keyword to url
        response = requests.get(self.url, params=self.params).json()['items']
        with open('data/vacancies.json', 'w', encoding='utf-8') as file:
            json.dump(response, file, ensure_ascii=False, indent=4)
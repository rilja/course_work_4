import json
from abc import ABC, abstractmethod


class VacancySaver(ABC):
    """Abstract class for saving data"""
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass

    @abstractmethod
    def choose_vacancy(self, keyword='all', salary_range='', top_count=10):
        pass


class JSONSaver(VacancySaver):
    def __init__(self):
        super().__init__()

    def add_vacancy(self, vacancy):
        with open('data/vacancies_from_HH.json', encoding='utf-8') as file:
            data = json.load(file)
            for i in data['Vacancies']:
                if i == vacancy.__dict__:
                    print('Vacancy already added')
                    break
            data['Vacancies'].append(vacancy.__dict__)
            with open('data/vacancies_from_HH.json', 'w', encoding='utf-8') as outfile:
                json.dump(data, outfile, ensure_ascii=False, indent=2)

    def delete_vacancy(self, vacancy):
        pass

    def choose_vacancy(self, keyword='all', salary_range='', top_count=10):
        pass

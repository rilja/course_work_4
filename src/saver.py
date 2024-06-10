import json
from abc import ABC, abstractmethod


class VacancySaver(ABC):
    """Abstract class for saving data"""
    @abstractmethod
    def __init__(self):
        self.is_added = False
        pass

    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass


class JSONSaver(VacancySaver):
    """class for saving data in json file"""
    def __init__(self):
        super().__init__()

    def add_vacancy(self, vacancy):
        """adds vacancy to the file"""

        with open('data/vacancies_from_HH.json', encoding='utf-8') as file:
            data = json.load(file)
            for i in data['Vacancies']:
                if i == vacancy.__dict__:
                    self.is_added = True
            if not self.is_added:
                data['Vacancies'].append(vacancy.__dict__)
                with open('data/vacancies_from_HH.json', 'w', encoding='utf-8') as outfile:
                    json.dump(data, outfile, ensure_ascii=False, indent=2)

    def delete_vacancy(self, vacancy):
        """"delete vacancy from the file"""

        try:
            with open('data/vacancies_from_HH.json', encoding='utf-8') as file:
                data = json.load(file)
                data['Vacancies'].remove(vacancy.__dict__)
                with open('data/vacancies_from_HH.json', 'w', encoding='utf-8') as outfile:
                    json.dump(data, outfile, ensure_ascii=False, indent=2)
        except ValueError:
            print('No such vacancy in the file')

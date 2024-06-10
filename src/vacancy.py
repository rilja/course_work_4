from abc import ABC, abstractmethod


class BaseVacancy(ABC):
    """Abstract class for creating vacancies from API"""
    @abstractmethod
    def __init__(self, identification, name, url, salary, description, requirements):
        self.id = identification
        self.name = name
        self.url = url
        self.salary = salary if salary else 0
        self.description = description
        self.requirements = requirements

    @classmethod
    def cast_to_object_list(cls, data):
        pass


class Vacancy(BaseVacancy):
    def __init__(self, identification, name, url, salary, description, requirements):
        super().__init__(identification, name, url, salary, description, requirements)

    @classmethod
    def cast_to_object_list(cls, data):
        vacancies = []
        for i in data:
            vacancy = cls(i.get('id'),
                          i.get('name'),
                          i.get('alternate_url'),
                          i.get('salary'),
                          i.get('description'),
                          i.get('requirements'))
            vacancies.append(vacancy)

        return vacancies

    @staticmethod
    def get_vacancies_by_salary(vacancies: list, salary_range: str):
        salary_range = salary_range.split(' - ')
        filtered_vacancies = []
        for i in vacancies:
            if salary_range[1] >= i.get('salary').get('from') >= salary_range[0] or salary_range[1] >= i.get('salary').get('to') >= salary_range[0]:
                filtered_vacancies.append(i)
        return filtered_vacancies

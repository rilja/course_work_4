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
        lower_range = int(salary_range[0])
        upper_range = int(salary_range[1])
        filtered_vacancies = []
        for i in vacancies:
            if i.salary:
                if i.salary.get('from'):
                    if upper_range >= i.salary.get('from') >= lower_range:
                        filtered_vacancies.append(i)
        return filtered_vacancies

    @staticmethod
    def get_top_vacancies(vacancies: list, top: int):
        filtered_vacancies = []
        salary_list = []
        for i in vacancies:
            if i.salary:
                if i.salary.get('from'):
                    salary_list.append(i.salary.get('from'))
        salary_list.sort(reverse=True)
        for salary in salary_list:
            for i in vacancies:
                if i.salary:
                    if i.salary.get('from') == salary:
                        filtered_vacancies.append(i)
        return filtered_vacancies[0:top]






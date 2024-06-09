from src.parser import HH
from src.vacancy import Vacancy

if __name__ == '__main__':
    hh1 = HH()
    hh_vacancies = hh1.load_vacancies('python')
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
    print(vacancies_list)

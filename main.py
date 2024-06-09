from src.parser import HH
from src.saver import JSONSaver
from src.vacancy import Vacancy

if __name__ == '__main__':
    hh1 = HH()
    hh_vacancies = hh1.load_vacancies('python')
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
    json_saver = JSONSaver()
    json_saver.add_vacancy(vacancies_list[0])
    json_saver.add_vacancy(vacancies_list[1])
    json_saver.add_vacancy(vacancies_list[1])


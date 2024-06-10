from src.parser import HH
from src.saver import JSONSaver
from src.vacancy import Vacancy


# Function for user interaction
def user_interaction():
    # asking user for keyword
    keyword_word = input("Введите ключевое слово для поиска вакансий: ")

    # Creating an instance of a class to work with the API of job sites
    hh_api = HH()

    # Receiving vacancies from hh.ru in JSON format
    hh_vacancies = hh_api.load_vacancies(keyword_word)

    # Converting a dataset from JSON to a list of objects
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

    # Saving information about vacancies to a JSON file
    json_saver = JSONSaver()
    for i in vacancies_list:
        json_saver.add_vacancy(i)

    top_n = int(input("Введите количество вакансий для вывода в топ N: "))

    salary_range = input("Введите диапазон зарплат: ")  # Пример: 100000 - 150000

    ranged_vacancies = Vacancy.get_vacancies_by_salary(vacancies_list, salary_range)
    top_vacancies = Vacancy.get_top_vacancies(ranged_vacancies, top_n)
    print(top_vacancies)  # print result


if __name__ == "__main__":
    user_interaction()

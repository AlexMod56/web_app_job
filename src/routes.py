from flask import Blueprint, render_template, request
from src.scraper import fetch_vacancies_hh, load_cities, get_city_id
from src.parser import parse_hh_vacancies
import logging

bp = Blueprint('routes', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():

    vacancies = []
    error_message = None

    cities = load_cities()

    if request.method == 'POST':

        query = request.form.get('query')
        city_name = request.form.get('city')
        pages = request.form.get('pages')

        if not query:
            error_message = "Введите запрос для поиска вакансий."
        else:
            logging.info(f"Поиск вакансий для: {query}, регион: {city_name}")

            city_id = get_city_id(city_name, cities)

            if city_id:
                try:
                    pages = int(pages)
                    if pages < 1:
                        raise ValueError("Неверное количество страниц")
                except ValueError:
                    error_message = "Количество страниц должно быть от 1."

                else:

                    all_html_pages = fetch_vacancies_hh(query=query, area=city_id, max_pages=pages)

                    if all_html_pages:
                        vacancies = parse_hh_vacancies(all_html_pages)
                    else:
                        error_message = "Не удалось получить данные, попробуйте позже."

            else:
                error_message = f"Город '{city_name}' не найден. Проверьте правильность ввода."

    return render_template('index.html', vacancies=vacancies, error_message=error_message)

import requests
import logging
import json
import os

def load_cities():
    with open(os.path.join(os.path.dirname(__file__), "cities.json"), "r", encoding="utf-8") as file:
        cities = json.load(file)
    return cities

def get_city_id(city_name, cities):
    return cities.get(city_name)

def fetch_vacancies_hh(query="Developer", area=1, max_pages=10):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    url = "https://hh.ru/search/vacancy"

    all_vacancies_html = []

    for page in range(max_pages):

        params = {"text": query, "area": area, "page": page}

        try:

            logging.info(f"Запрос страницы {page + 1}")
            response = requests.get(url, params=params, headers=headers)
            all_vacancies_html.append(response.text)

        except requests.exceptions.RequestException as e:

            logging.error(f"Ошибка при запросе страницы {page + 1}: {e}")
            break

    return all_vacancies_html
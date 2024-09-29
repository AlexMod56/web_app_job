# Скрапер вакансий

## Описание
Это веб-приложение, разработанное с использованием Flask, 
которое позволяет пользователям искать вакансии на hh.ru по запросу и региону. 
Результаты поиска отображаются в удобном интерфейсе с возможностью выбора количества страниц 
для поиска. Пользователи могут вводить название города, чтобы искать вакансии по 
определённым регионам, а также указывать количество страниц для отображения результатов.

## Запуск
1. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   
2. Запустите приложение:
   ```bash
   python run.py
   
3. Перейдите в браузер по адресу http://127.0.0.1:5000/ для поиска вакансий.

## Основные файлы
* scraper.py - запросы к сайтам вакансий.
* parser.py - парсинг данных.
* cities.json - список городов и их ID для поиска.
* routes.py - основные маршруты приложения.
* logging_config.py - настройка логирования.
* index.html - Шаблон HTML для отображения результатов.
* requirements.txt - список зависимостей.

### Основные библиотеки

Flask - для разработки веб-приложения.
requests - для выполнения HTTP-запросов к hh.ru.
BeautifulSoup (bs4) - для парсинга HTML страниц.
lxml - для поддержки работы BeautifulSoup.
logging - для логирования ошибок и событий.

## Использование
1. Откройте веб-страницу приложения.
2. Введите запрос для поиска вакансий (например, "Python разработчик").
3. Укажите название города (например, "Москва", "Санкт-Петербург").
4. Укажите количество страниц (от 1).
5. Нажмите кнопку "Поиск", чтобы получить список вакансий.

## Расширение проекта
Поддержка других сайтов: В проект можно интегрировать поддержку других платформ для поиска работы, таких как LinkedIn.
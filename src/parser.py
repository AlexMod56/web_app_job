from bs4 import BeautifulSoup

def parse_hh_vacancies(all_html_pages):

    vacancies = []

    for html_content in all_html_pages:

        soup = BeautifulSoup(html_content, "lxml")

        for item in soup.find_all("div", attrs={'data-qa': 'vacancy-serp__vacancy vacancy-serp__vacancy_standard vacancy-serp-item_clickme'}):
            title = item.find("a", attrs={'data-qa': 'serp-item__title'}).text
            href = item.find('a', attrs={'data-qa': 'serp-item__title'})['href']
            company = item.find('a', attrs={'data-qa': 'vacancy-serp__vacancy-employer'}).text

            vacancies.append({"title": title, "company": company, "href": href})

    return vacancies

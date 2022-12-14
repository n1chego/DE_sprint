import requests as req
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import time
import json

headers = {
    'User-Agent':UserAgent().chrome
}
data = dict(data=[])
i=0
while i < 1:
    url = f'https://hh.ru/search/vacancy?text=python+%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA&salary=&area=1&ored_clusters=true&enable_snippets=true&page={i}&hhtmFrom=vacancy_search_list'
    response = req.get(url, headers=headers)
    if response.status_code != 200:
        break
    i += 1
    soup = BeautifulSoup(response.text, "lxml")
    tags = soup.find_all(attrs={'data-qa': 'serp-item__title'})

    for tag in tags:
        
        time.sleep(2)
        object_url = tag.attrs['href']
        object_response = req.get(object_url, headers=headers)
        object_soup = BeautifulSoup(object_response.text, "lxml")
        tag_salary = object_soup.find(attrs={'data-qa': 'vacancy-salary'})
        tag_experience = object_soup.find(attrs={'data-qa': 'vacancy-experience'})
        tag_location = (
            object_soup.find(attrs={'data-qa': 'vacancy-view-raw-address'}) or 
            object_soup.find(attrs={'data-qa': 'vacancy-view-location'})
        )
        vacancy = {
            "title": tag.text,
            "work experience": tag_experience.text,
            "salary": tag_salary.text,
            "region": tag_location.text
        }
        data['data'].append(vacancy)
print(data)
with open("data_json", "w") as file:
    json.dump(data, file, ensure_ascii=False)


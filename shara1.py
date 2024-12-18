import requests
from bs4 import BeautifulSoup
import csv

# URL страницы, которую вы хотите запросить
url = 'http://example.com'  # Замените на нужный URL

# Выполняем GET-запрос
response = requests.get(url)

# Создаем объект BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Открываем CSV-файл для записи
with open('output.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Записываем заголовок
    writer.writerow(['Заголовок', 'Subtitle'])
    
    # Находим все элементы с классом "subtitle-big faq__heading"
    main_titles = soup.find_all('h2', class_='subtitle-big faq__heading')
    
    # Проходим по каждому заголовку и находим соответствующие подзаголовки
    for main_title in main_titles:
        # Находим родительский элемент, чтобы искать подзаголовки внутри него
        parent = main_title.find_parent('li')
        if parent:
            # Находим все подзаголовки внутри родительского элемента
            subtitles = parent.find_all('h3', class_='subtitle')
            for subtitle in subtitles:
                writer.writerow([main_title.text, subtitle.text])

print("Данные успешно записаны в output.csv")

import collections

import pandas as pd
from collections import defaultdict, Counter
from pprint import pprint


# def make_report(log_file_name, report_template_file_name, report_output_file_name):

# 7 самых популярных браузеров по посещаемости
#     # Чтение и анализ данных из Excel
cols = [3, 6]
excel_data = pd.read_excel('logs.xlsx', usecols=cols, engine='openpyxl')
#Даты в столбце "Дата посещения" переводим в месяцы
for i in range(len(excel_data)):
    excel_data.iloc[i, 1] = excel_data.iloc[i, 1].month
# print(excel_data)
# Преобразуем переменную excel_data в словарь с помощью метода to_dict()
# Результат передаем в переменную excel_data_dict
excel_data_dict = excel_data.to_dict(orient='records')
# pprint(excel_data_dict[:4])

# Создаем словарь browser_dict с заранее заданным типом значений
browser_dict = defaultdict(int)

for element in excel_data_dict:
    # Добавляем элемент в словарь sales_dict
    # element['Браузер'] - название Браузера
    # Если ключа с таким названием в sales_dict нет, то будет значение 0,
    # таким образом мы просто увеличим его на 1
    browser_dict[element['Браузер']] += 1

# Создаем объект Counter из полученного словаря и используем метод most_common, чтобы определить рейтинг популяроности браузеров
most_common_sales = Counter(browser_dict).most_common(7)

# Формируем словарь браузеров по порядку популяности: 1й - самый популярный, последний - наимение популярный
number_of_browser_visits = {} # Ключи словаря - наименования браузеров
for i in range(len(most_common_sales)):
    number_of_browser_visits[most_common_sales[i][0]] = []

# Собираем данные по посещениям браузеров
browser_data = {} # Словарь для данных
for i in number_of_browser_visits.keys(): # Проходим по ключам словаря - наименования браузеров
    for element in excel_data_dict: # и проходим по данным посещения браузеров
        if element['Браузер'] == i: # Если имя браузера из БД равно имени браузера в словаре популярности,
            number_of_browser_visits[i].append(element['Дата посещения']) # отправляем значение месяца в список по значению ключа в словаре популярности
    letter_counter = collections.Counter(number_of_browser_visits[i]) # Считаем кол-во вхождений по каждому месяцу
    browser_data[i] = dict(collections.OrderedDict(sorted(letter_counter.items()))) # Сортируем по возрастанию и добавляем в словарь данных

month_list = (excel_data.iloc[:, 1]).tolist()
month_list_counter = collections.Counter(month_list)  # Считаем кол-во вхождений по каждому месяцу
month_list_counter = dict(collections.OrderedDict(sorted(month_list_counter.items())))  # Сортируем по возрастанию и добавляем в словарь данных

print(month_list_counter)

#
#     # Открываем файл шаблона отчета report_template.xlsx
#     wb = load_workbook(filename=report_template_file_name, data_only=True)
#
#     # Выполняем запись данных в объект wb
#     …
#
#     # Сохраняем файл-отчет
#     wb.save(report_output_file_name)

import collections

import pandas as pd
from collections import defaultdict, Counter
from pprint import pprint

def data_visits(log_file_name):
    # Чтение и анализ данных из Excel, берём только колонки с именами браузеров "Браузер" и "Дата посещения"
    cols = [3, 6]
    excel_data = pd.read_excel(log_file_name, usecols=cols, engine='openpyxl')
    #Даты в столбце "Дата посещения" переводим в месяцы
    for i in range(len(excel_data)):
        excel_data.iloc[i, 1] = excel_data.iloc[i, 1].month
    # print(excel_data)
    # Преобразуем переменную excel_data в словарь с помощью метода to_dict(). Результат передаем в переменную excel_data_dict
    excel_data_dict = excel_data.to_dict(orient='records')
    # pprint(excel_data_dict[:4])

    # Создаем словарь для подсчёта кол-ва посещений по каждому из браузеров - browser_dict с заранее заданным типом значений
    browser_dict = defaultdict(int)
    # Считаем кол-во посещений по каждому из браузеров
    for element in excel_data_dict:
        # Добавляем элемент в словарь browser_dict, element['Браузер'] - название Браузера
        # Если ключа с таким названием в browser_dict нет, то будет значение 0, таким образом мы просто увеличим его на 1
        browser_dict[element['Браузер']] += 1
    # pprint(browser_dict)

    # Создаем объект Counter из полученного словаря browser_dict
    # и используем метод most_common, чтобы определить рейтинг 7ми наиболее популярных браузеров
    most_common_visits = Counter(browser_dict).most_common(7)
    # print(most_common_sales)

    # Формируем словарь браузеров 7ми наиболее популярных браузеров для сбора данных по посещениям браузеров
    # по порядку популяности: 1й - самый популярный, последний - наимение популярный
    number_of_browser_visits = {} # Ключи словаря - наименования браузеров
    for i in range(len(most_common_visits)):
        number_of_browser_visits[most_common_visits[i][0]] = []
    # print(number_of_browser_visits)

    # Собираем данные по посещениям браузеров по месяцам и записываем в новый словарь browser_data
    browser_data = {} # Словарь для данных
    for i in number_of_browser_visits.keys(): # Проходим по ключам словаря - наименования браузеров
        for element in excel_data_dict: # и проходим по данным посещения браузеров
            if element['Браузер'] == i: # Если имя браузера из БД равно имени браузера в словаре популярности,
                number_of_browser_visits[i].append(element['Дата посещения']) # отправляем значение месяца в список по значению ключа в словаре популярности
        letter_counter = collections.Counter(number_of_browser_visits[i]) # Считаем кол-во вхождений по каждому месяцу у каждого браузера
        browser_data[i] = dict(collections.OrderedDict(sorted(letter_counter.items()))) # Сортируем месяцы(ключи) по возрастанию и добавляем в словарь данных
    # print(browser_data)

    browser_pop_list = []
    for i in number_of_browser_visits.keys():
        browser_pop_list.append(i)

    month_list = [] #Список месяцев посещений популярных браузеров
    for i in range(len(excel_data)):
        if excel_data.iloc[i, 0] in browser_pop_list:
            month_list.append(excel_data.iloc[i, 1])
    # print(browser_pop_list)

    month_list_counter = collections.Counter(month_list)  # Считаем кол-во вхождений по каждому месяцу
    month_list_counter = dict(collections.OrderedDict(sorted(month_list_counter.items())))  # Сортируем по возрастанию и добавляем в словарь данных

    # print(month_list_counter)

    return browser_data, browser_pop_list, month_list_counter

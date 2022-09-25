import collections
import pandas as pd
from collections import defaultdict, Counter
from pprint import pprint

def data_visits(log_file_name):
    # Чтение и анализ данных из Excel, берём только колонки с именами браузеров и "Дата посещения"
    cols = ['Браузер', 'Дата посещения']
    excel_data = pd.read_excel(log_file_name, usecols=cols, engine='openpyxl')
    #Даты в столбце "Дата посещения" переводим в месяцы
    for i in range(len(excel_data)):
        excel_data.iloc[i, 1] = excel_data.iloc[i, 1].month
    # print(excel_data)

    # Преобразуем excel_data в словарь
    excel_data_dict = excel_data.to_dict(orient='records')
    # pprint(excel_data_dict[:4])

    # Создаем словарь для подсчёта кол-ва посещений по каждому из браузеровс заранее заданным типом значений
    # для нахождения наиболее попцулярных браузеров
    # Ключи - наименования браузеров
    browser_dict = defaultdict(int)
    # Считаем кол-во посещений по каждому из браузеров за все месяцы
    for element in excel_data_dict:
        browser_dict[element['Браузер']] += 1
    # pprint(browser_dict)

    # Создаем объект Counter из полученного словаря browser_dict
    # и используем метод most_common, для определения рейтинга 7ми наиболее популярных браузеров
    most_common_visits = Counter(browser_dict).most_common(7)
    # print(most_common_sales)

    # Формируем словарь браузеров 7ми наиболее популярных браузеров для сбора данных по посещениям браузеров
    # по порядку популяности: 1й - самый популярный, последний - наимение популярный
    number_visits_of_browser_dict = {} # Ключи словаря - наименования браузеров
    for i in range(len(most_common_visits)):
        number_visits_of_browser_dict[most_common_visits[i][0]] = []
    # print(number_of_browser_visits)

    # Собираем данные по посещениям браузеров по месяцам и записываем в новый словарь browser_data
    browser_pop_list = [] # Для суммарных значений посещений по месяцам по всем популярным браузерам
    browser_data = {} # Словарь для значений посещений по месяцам по браузерам по отдельности
    for i in number_visits_of_browser_dict.keys(): # Проходим по ключам словаря - наименования браузеров
        for element in excel_data_dict: # и проходим по данным посещения браузеров
            if element['Браузер'] == i: # Если имя браузера из БД равно имени браузера в словаре популярности,
                number_visits_of_browser_dict[i].append(element['Дата посещения']) # отправляем значение месяца в список по значению ключа в словаре популярности
                browser_pop_list.append(element['Дата посещения']) # отправляем значение месяца в список по значению ключа в словаре популярности
        letter_counter = collections.Counter(number_visits_of_browser_dict[i]) # Считаем кол-во вхождений по каждому месяцу у каждого браузера
        browser_data[i] = dict(collections.OrderedDict(sorted(letter_counter.items()))) # Сортируем месяцы(ключи) по возрастанию и добавляем в словарь данных
    # pprint(browser_data)

    # Словарь суммарных значений продаж по месяцам по всем популярным браузерам
    all_visits_pop_browser_months_dict = dict(collections.OrderedDict(sorted(collections.Counter(browser_pop_list).items())))  # Сортируем по возрастанию и добавляем в словарь данных
    # pprint(all_visits_pop_browser_month_dict)

    return browser_data, all_visits_pop_browser_months_dict

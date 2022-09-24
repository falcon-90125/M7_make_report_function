import collections
import pandas as pd
from collections import defaultdict, Counter
from pprint import pprint

#по готовности функции - удалить
log_file_name = 'logs.xlsx'

def popular_goods(log_file_name):
    # Чтение и анализ данных из Excel, берём только колонки с именами браузеров "Браузер" и "Дата посещения"
    cols = [6, 7]
    excel_data = pd.read_excel(log_file_name, usecols=cols, engine='openpyxl')

    #Даты в столбце "Дата посещения" переводим в месяцы
    for i in range(len(excel_data)):
        excel_data.iloc[i, 0] = excel_data.iloc[i, 0].month
    # print(excel_data)

    # Преобразуем переменную excel_data в словарь с помощью метода to_dict(). Результат передаем в переменную excel_data_dict
    excel_data_dict = excel_data.to_dict(orient='records')
    # pprint(excel_data_dict[0])

    # Создаем словарь для подсчёта кол-ва посещений по каждому из браузеров - browser_dict с заранее заданным типом значений
    goods_dict = defaultdict(int)

    # Считаем кол-во посещений по каждому из браузеров
    for element in excel_data_dict:
        # Добавляем элемент в словарь browser_dict, element['Браузер'] - название Браузера
        # Если ключа с таким названием в browser_dict нет, то будет значение 0, таким образом мы просто увеличим его на 1
        good_str = element['Купленные товары']
        good_list = good_str.split(',')
        for i in range(len(good_list)):
            good = good_list[i]
            goods_dict[good] += 1
    # print(goods_dict)

    # Создаем объект Counter из полученного словаря browser_dict
    # и используем метод most_common, чтобы определить рейтинг 7ми наиболее популярных браузеров
    most_common_goods = Counter(goods_dict).most_common(7)
    # print(most_common_goods)

    # Формируем словарь браузеров 7ми наиболее популярных браузеров для сбора данных по посещениям браузеров
    # по порядку популяности: 1й - самый популярный, последний - наимение популярный
    sales_goods = {}  # Ключи словаря - наименования браузеров
    for i in range(len(most_common_goods)):
        sales_goods[most_common_goods[i][0]] = []
    # pprint(sales_goods)

    # Собираем данные по посещениям браузеров по месяцам и записываем в новый словарь browser_data
    sales_months = [] # Для итоговых значений по месяцам по всем браузерам
    sales_goods_data = {}  # Словарь для данных по месяцам по браузерам по отдельности
    for i in sales_goods.keys():  # Проходим по ключам словаря - наименования браузеров
        for element in excel_data_dict:  # и проходим по данным посещения браузеров
            good_str = element['Купленные товары']
            good_list = good_str.split(',')
            for ig in range(len(good_list)):
                good = good_list[ig]
                if good == i:  # Если имя браузера из БД равно имени браузера в словаре популярности,
                    sales_goods[i].append(element['Дата посещения'])  # отправляем значение месяца в список по значению ключа в словаре популярности
                    sales_months.append(element['Дата посещения'])
            letter_counter = collections.Counter(sales_goods[i])  # Считаем кол-во вхождений по каждому месяцу у каждого браузера
            sales_goods_data[i] = dict(collections.OrderedDict(sorted(letter_counter.items())))  # Сортируем месяцы(ключи) по возрастанию и добавляем в словарь данных
    # print(sales_goods_data)

    months_counter = collections.Counter(sales_months)
    sales_months_data = dict(collections.OrderedDict(sorted(months_counter.items())))  # Сортируем месяцы(ключи) по возрастанию и добавляем в словарь данных

    # print(sales_months_data)
    return sales_goods_data, sales_months_data

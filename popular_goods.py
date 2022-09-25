import collections
import pandas as pd
from collections import defaultdict, Counter
from pprint import pprint

def popular_goods(log_file_name):
    # Чтение и анализ данных из Excel, берём только колонки с наименованиями товаров и "Дата посещения"
    cols = ['Дата посещения', 'Купленные товары']
    excel_data = pd.read_excel(log_file_name, usecols=cols, engine='openpyxl')

    #Даты в столбце "Дата посещения" переводим в месяцы
    for i in range(len(excel_data)):
        excel_data.iloc[i, 0] = excel_data.iloc[i, 0].month
    # print(excel_data)

    # Преобразуем excel_data в словарь
    excel_data_dict = excel_data.to_dict(orient='records')
    # pprint(excel_data_dict[0])

    # Создаем словарь для подсчёта общего кол-ва купленых товаров с заранее заданным типом значений
    # для нахождения наиболее попцулярных товаров
    # Ключи - наименования товаров
    sales_goods_dict = defaultdict(int)
    # Считаем кол-ва купленых товаров за все месяцы
    for element in excel_data_dict: # Проходим по строкам купленых товаров
        good_list = element['Купленные товары'].split(',') # Строку с товарами разбиваем на список по разделителю
        for i in range(len(good_list)): # Проходим по полученному списку наименований товаров
            sales_goods_dict[good_list[i]] += 1 # Добавляем кол-во по ключу
    # print(sales_goods_dict)

    # Создаем объект Counter из полученного словаря sales_goods_dict
    # и используем метод most_common, чтобы определения рейтинга 7ми наиболее популярных товаров
    most_common_goods = Counter(sales_goods_dict).most_common(7)
    # print(most_common_goods)

    # Формируем словарь 7ми наиболее популярных товаров для сбора данных по продажам по месяцам
    # по порядку популяности: 1й - самый популярный, последний - наимение популярный
    pop_goods_dict = {}
    for i in range(len(most_common_goods)): # Ключи словаря - наименования товаров
        pop_goods_dict[most_common_goods[i][0]] = [] # Значения - список продаж по месяцам
    # pprint(pop_goods_dict)

    # Собираем данные по продажам товаров по месяцам и записываем в новый словарь sales_goods_data
    sales_months_list = [] # Для суммарных значений продаж по месяцам по всем популярным товарам
    sales_goods_data = {}  # Словарь для значений продаж по месяцам по товарам по отдельности
    for i in pop_goods_dict.keys():  # Проходим по ключам словаря - наименования товаров
        for element in excel_data_dict:  # и проходим по строкам купленых товаров
            good_list = element['Купленные товары'].split(',') # Строку с товарами разбиваем на список по разделителю
            for ig in range(len(good_list)): # Проходим по полученному списку наименований товаров
                if good_list[ig] == i:  # Если товар из БД есть в словаре популярных товаров,
                    pop_goods_dict[i].append(element['Дата посещения']) # отправляем значение месяца в список по значению ключа в словаре популярности
                    sales_months_list.append(element['Дата посещения']) # и отправляем значение месяца в список суммарных значений продаж по месяцам по всем популярным товарам
            letter_counter = collections.Counter(pop_goods_dict[i])  # Считаем кол-во вхождений по каждому месяцу у каждого товара
            sales_goods_data[i] = dict(collections.OrderedDict(sorted(letter_counter.items()))) # Сортируем месяцы(ключи) по возрастанию и добавляем в словарь данных
    # pprint(sales_goods_data)

    # Словарь суммарных значений продаж по месяцам по всем популярным товарам
    all_sales_pop_goods_months_dict = dict(collections.OrderedDict(sorted(collections.Counter(sales_months_list).items())))
    # pprint(sales_months_dict)
    return sales_goods_data, all_sales_pop_goods_months_dict

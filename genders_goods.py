import collections
import pandas as pd
from collections import defaultdict, Counter
log_file_name = 'logs.xlsx'
def genders_goods(log_file_name):
    # Чтение и анализ данных из Excel, берём только колонки с наименованиями товаров и "Дата посещения"
    cols = ['Пол', 'Купленные товары']
    excel_data = pd.read_excel(log_file_name, usecols=cols, engine='openpyxl')

    # Преобразуем excel_data в словарь
    excel_data_dict = excel_data.to_dict(orient='records')
    # pprint(excel_data_dict[0])

    # Создаем списки мужских и женских товаров для подсчёта общего кол-ва купленых товаров
    # для нахождения наиболее и наименее попцулярных товаров
    mens_goods_list = []
    woomens_goods_list = []
    # Считаем кол-ва купленых товаров за все месяцы
    for element in excel_data_dict: # Проходим по строкам купленых товаров
        if element['Пол'] == 'м':
            good_list = element['Купленные товары'].split(',') # Строку с товарами разбиваем на список по разделителю
            for i in range(len(good_list)): # Проходим по полученному списку наименований товаров
                mens_goods_list.append(good_list[i])
        else:
            good_list = element['Купленные товары'].split(',') # Строку с товарами разбиваем на список по разделителю
            for i in range(len(good_list)): # Проходим по полученному списку наименований товаров
                woomens_goods_list.append(good_list[i])

    genders_goods_list = []
    for i in mens_goods_list, woomens_goods_list:
        letter_counter_goods = collections.Counter(i)
        # Методом most_common отсортируем товары по популярности в порядке убывания
        letters_most_common = letter_counter_goods.most_common()
        genders_goods_list.append(letters_most_common[0][0]) # Наиболее популярные товары
        genders_goods_list.append(letters_most_common[:-(len(letter_counter_goods)+1):-1][0][0]) # Наименее популярные товары

    # print(goods_list)

    return genders_goods_list

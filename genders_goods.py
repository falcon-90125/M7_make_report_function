import collections
import pandas as pd
from collections import defaultdict, Counter

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

    # Считаем количество вхождений наименований товаров в мужских и женских списках
    letter_counter_mens_goods = collections.Counter(mens_goods_list)
    letter_counter_woomens_goods = collections.Counter(woomens_goods_list)

    # Методом most_common отсортируем товары по популярности в порядке убывания
    letters_most_common_mens_goods = letter_counter_mens_goods.most_common()
    letters_most_common_woomens_goods = letter_counter_woomens_goods.most_common()

    # Наиболее популярные товары
    pop_mens_goods = letters_most_common_mens_goods[0][0]
    pop_woomens_goods = letters_most_common_woomens_goods[0][0]

    # print(pop_mens_goods)
    # print(pop_woomens_goods)

    # Наименее популярные товары
    no_pop_mens_goods = letters_most_common_mens_goods[:-(len(letter_counter_mens_goods)+1):-1][0][0]
    no_pop_woomens_goods = letters_most_common_woomens_goods[:-(len(letter_counter_woomens_goods)+1):-1][0][0]

    # print(no_pop_mens_goods)
    # print(no_pop_woomens_goods)

    return pop_mens_goods, pop_woomens_goods, no_pop_mens_goods, no_pop_woomens_goods

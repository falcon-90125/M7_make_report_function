import collections

import pandas as pd
from collections import defaultdict, Counter
from pprint import pprint
from openpyxl import load_workbook
from data_visits import data_visits
from popular_goods import popular_goods

# 7 самых популярных браузеров по посещаемости
log_file_name = 'logs.xlsx'
report_template_file_name = 'report_template.xlsx'
report_output_file_name = 'report_template_output.xlsx'

def make_report(log_file_name, report_template_file_name, report_output_file_name): #, report_template_file_name, report_output_file_name
    browser_data, browser_pop_list, month_list_counter = data_visits(log_file_name)
    sales_goods_data, sales_months_data = popular_goods(log_file_name)

    # Открываем файл шаблона отчета report_template.xlsx
    wb = load_workbook(filename=report_template_file_name, data_only=True)
    ws = wb[wb.sheetnames[0]]

    # Выполняем запись данных в объект wb
    for i, val in enumerate(browser_pop_list):
        cell_i = ws.cell(row=5+i, column=1)
        cell_i.value = val
        for month in range(len(month_list_counter)):
            numberOfVisits = browser_data[val][month+1]
            cell_month = ws.cell(row=5+i, column=2+month)
            cell_month.value = numberOfVisits
            allInMonthVal = month_list_counter
            cell_all_in_month = ws.cell(row=12, column=2+month)
            cell_all_in_month.value = allInMonthVal[month+1]

    for i, val in enumerate(sales_goods_data.keys()):
        cell_i = ws.cell(row=19+i, column=1)
        cell_i.value = val

    # Сохраняем файл-отчет
    wb.save(report_output_file_name)

make_report(log_file_name, report_template_file_name, report_output_file_name)

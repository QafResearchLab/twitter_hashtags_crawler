import xlsxwriter
import json

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('results.xlsx')

dictionary = [
    'ارحلوالننترككم',
    'ارحلوا_لن_نترككم',
    'انهزام_امريكا',
    'قدماستقالةفاشل',
    'قدم_استقالة_فاشل',
    'الكاظميزعيمالمافيات',
    'الكاظمي_زعيم_المافيات',
]

for dic in dictionary:
    worksheet = workbook.add_worksheet(f'{dic}')

    # Start from the first cell. Rows and columns are zero indexed.
    row = 0
    col = 0

    f = open(f"{dic}.txt", "r", encoding="utf-8")
    data = json.loads(f.readline())

    # Iterate over the data and write it out row by row.
    # for item, cost in (data):
    for item in (data):
        # print(item)
        worksheet.write(row, col, str(item['id']))
        worksheet.write(row, col+1, item['username'])
        worksheet.write(row, col+2, item['datetime'])
        worksheet.write(row, col+3, item['content'])
        worksheet.write(row, col+4, item['url'])
        row += 1

workbook.close()

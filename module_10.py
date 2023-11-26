import requests
from pprint import pprint
import gspread
import json


def call_api_github(username):
    """
    Чтение данных с api github
    :param username:
    :return:
    """
    # Имя пользователя github
    #username = input('Введите имя пользователя: ')
    # url для запроса
    url = f"https://api.github.com/users/{username}"
    # делаем запрос и возвращаем json
    user_data = requests.get(url).json()
    pprint(user_data)
    return user_data

gc = gspread.service_account(filename='my-project-intellect-406217-92dd3afa93b9.json')
wb = gc.open_by_url('https://docs.google.com/spreadsheets/d/1rOIvOOKtkE7oYebvW3BBy0CvrfJuVqqPY1jpLtvFWqw/edit#gid=0')
worksheet = wb.get_worksheet(0)


def save_data(username):
    """
    Сохранение данных в таблицу
    :param username:
    :return:
    """
    gc = gspread.service_account(filename='my-project-intellect-406217-92dd3afa93b9.json')
    wb = gc.open_by_url(
        'https://docs.google.com/spreadsheets/d/1rOIvOOKtkE7oYebvW3BBy0CvrfJuVqqPY1jpLtvFWqw/edit#gid=0')
    worksheet = wb.get_worksheet(0)
    dict_data = call_api_github(username)
    val = worksheet.acell('A1').value
    if val:
        x = 1
        while True:
            if worksheet.cell(1, x).value:
                x += 1
                continue
            else:
                i = 1
                for key in dict_data.keys():
                    worksheet.update_cell(i, x, dict_data[key])
                    i += 1
                break
    else:
        i = 1
        for key in dict_data.keys():
            worksheet.update(f'A{i}', key)
            worksheet.update(f'B{i}', dict_data[key])
            i += 1


def get_json_user(username):
    """
    Получение записи по имени пользователя
    :param username:
    :return:
    """
    gc = gspread.service_account(filename='my-project-intellect-406217-92dd3afa93b9.json')
    wb = gc.open_by_url(
        'https://docs.google.com/spreadsheets/d/1rOIvOOKtkE7oYebvW3BBy0CvrfJuVqqPY1jpLtvFWqw/edit#gid=0')
    worksheet = wb.get_worksheet(0)
    y = 1
    while True:
        if worksheet.cell(y, 1).value == 'login':
            break
        elif not worksheet.cell(y, 1).value:
            print('Скорее всего данных нет или не верная таблица')
            break
        y += 1
    res_dict = {}
    x = 2
    while True:
        if worksheet.cell(y, x).value == username:
            idx = 0
            key_dikt = worksheet.col_values(1)
            vol_dict = worksheet.col_values(x)
            for key in key_dikt:
                res_dict[key] = vol_dict[idx]
                idx += 1
            break
        elif not worksheet.cell(y, x).value:
            break
        x += 1

    #return json.dumps(res_dict)
    return res_dict


def get_json_all():
    """
    Получение всех записей
    :return:
    """
    gc = gspread.service_account(filename='my-project-intellect-406217-92dd3afa93b9.json')
    wb = gc.open_by_url(
        'https://docs.google.com/spreadsheets/d/1rOIvOOKtkE7oYebvW3BBy0CvrfJuVqqPY1jpLtvFWqw/edit#gid=0')
    worksheet = wb.get_worksheet(0)
    res = []
    x = 2
    while worksheet.cell(1, x).value:
        one_dict = {}
        idx = 0
        key_dikt = worksheet.col_values(1)
        vol_dict = worksheet.col_values(x)
        for key in key_dikt:
            one_dict[key] = vol_dict[idx]
            idx += 1
        res.append(one_dict)
        x += 1
    #return json.dumps(res)
    return res


if __name__ == '__main__':
    save_data('slavsent')
    print(get_json_user('slavsent'))
    print(get_json_all())

from datetime import datetime

# Перше завдання
date = "1995vvdfvdfл90зdvdfvd10"


def get_days_from_today(date):
    data_editing = ''
    for i in date:
        if i in '1234567890':
            data_editing += i
        else:
            data_editing += ''
    try:
        date_string = datetime.strptime(data_editing, "%Y%m%d").date()
        today = datetime.today().date()
        return (today - date_string).days
    except ValueError:
        return 'Невірно введена дата'


print('Перше завдання результат: ', get_days_from_today(date))

# Друге завдання

import random


def get_numbers_ticket(min, max, quantity):
    list_num_ticket = []
    if min >= 1 and max - min >= quantity:
        try:
            while len(list_num_ticket) < quantity:
                num = random.randint(min, max)
                if num in list_num_ticket:
                    continue
                else:
                    list_num_ticket.append(num)
            return sorted(list_num_ticket)
        except ValueError:
            return list_num_ticket
    else:
        return list_num_ticket


num_min = 1
num_max = 1000
quantity = 10

print('Друге завдання результат: ', get_numbers_ticket(num_min, num_max, quantity))


# Третє завдання

import re


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]


def normalize_phone(phone_number):

    pattern = r"\d+"
    matches = ''.join(re.findall(pattern, phone_number))

    if len(matches) == 10:
        matches = ('+38' + matches)

    if len(matches) == 12:
        matches = ('+' + matches)
    
    return matches


sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)


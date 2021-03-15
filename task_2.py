"""
1. Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя пользователя и
 почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден, выбросить исключение ValueError.
  Пример:
# >>> email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
    raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru
Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении; имеет ли смысл в
данном случае использовать функцию re.compile()?
2. * (вместо 1) Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) для получения информации
вида: (<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>, <response_size>),
например:

raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-"
"Debian APT-HTTP/1.3 (0.9.7.9)"'
parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')
Примечание: вы ограничились одной строкой или проверили на всех записях лога в файле? Были ли особенные строки? Можно ли
 для них уточнить регулярное выражение?
"""

import re


# ------ Задание 1 -------
def email_parse(email_address):
    email_valid = re.compile(r'([a-z0-9_.-]+)@([a-z]+\.[a-z]+)', flags=re.IGNORECASE)
    if email_valid.match(email_address):
        res = email_valid.findall(email_address)[0]
        return {"username": res[0], "domain": res[1]}
    else:
        raise ValueError("Not e-mail.")


email1 = "ansdf-sds.organiz@facebook.com"
email2 = "ansdf-sds.organiz@facebookcom"
try:
    print(email_parse(email1))
    print(email_parse(email2))
except ValueError as exc:
    print("e-mail valid")
print()


# ------ Задание 2 -------
def parse_data(st):
    RE_PARSE = re.compile(r"[a-z0-9.+:/]+", flags=re.IGNORECASE)
    p_l = RE_PARSE.findall(st)
    return p_l[0], p_l[1] + p_l[2], p_l[3], p_l[4], p_l[7], p_l[8]


with open("nginx_logs.txt", "r", encoding="utf-8") as f:
    for s in f:
        print(parse_data(s))

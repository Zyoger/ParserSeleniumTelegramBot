import parser_selenium

URL = 'https://bask.ru/catalog/kurtka-bask-vorgol-v2-20212/'
tag = "span"
name = ""
number = 5

prise = parser.get_prise(URL, tag, name, number)
print(prise)

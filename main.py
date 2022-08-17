import re
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter =",")
    contacts_list = list (rows)

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код
res2 = []
for contacts in contacts_list:
    contact_text = (",".join(map(str,contacts)))
    pattern_tel = re.compile(r"(\+7|8)(\ ?\(?)(\d{3})(\)?\ ?\-?)(\d{3})\-?(\d{2})\-?(\d{2})?(\ ?\(?)?(доб.)?\ ?(\d{4})?\)?")
    res = pattern_tel.sub(r"+7(\3)\5-\6-\7 \9\g<10>", contact_text)
    pattern_name = re.compile(r"(lastname|\w*)(\ |,)(firstname|\w*)(\ |\,)(surname|\,|\w*),*(organization|[а-яёА-ЯЁ]{3,6})?,*(position|[а-яёА-ЯЁc\ –]*)?,,")
    res1 = pattern_name.sub(r"\1, \3, \5, \6, \7, ", res).split(",")
    res2.append(res1)

contacts_list_new = []

def merger(list1, list2):
    result = []
    for i in range(len(list1)):
        if list1[i] >= list2[i]:
            result.append(list1[i])
        else:
            result.append(list2[i])
    contacts_list_new.append(result)

d = []

for a in range(len(res2)):
    c = a + 1
    for b in range(c,len(res2)):
        if res2[a][0] == res2[b][0]:
            merger(res2[a], res2[b])
            d.append(a)
            d.append(b)

for d1 in reversed (d):
    res2.pop(d1)

for a in range(len(res2)):    #
    contacts_list_new.append(res2[a])
pprint(contacts_list_new)
# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
 datawriter = csv.writer(f, delimiter =',')
 # Вместо contacts_list подставьте свой список
 datawriter.writerows(contacts_list_new)






import re

s = "La fête de Noël est passée très vite!.. Tout le monde est déjà rentré chez soi."
list_s = s.split()                              # преобразовали строку в список

diacritics = r'[^a-zA-Zа-яА-ЯёЁ0-9 .,:;!?«»r''"‎/\{}()<>@&№#^*$  ]'
diacritics_in_s = re.findall(diacritics, s)     # нашли все диакритики в строке
diacritics_set = set(diacritics_in_s)           # найденное преобразуем в множество уникальных диакритик
print(diacritics_set)
diacritic_words = []

for i in diacritics_set:                       # прошлись всеми диакритиками строки
    for j in list_s:                           # по строке, преобразованной в список
        if i in j:
            diacritic_words.append(j)
print(set(diacritic_words))                    # множество уникальных слов с диакритикой (déjà один раз)

import re

line = "Мищенкова 06/05/1993; Клячко 28.11.1989; Шейфер 04 02 1989."

REGEX_YEAR = r'\d{4}'
year_result = re.findall(REGEX_YEAR, line)
print(sorted(year_result))

all_dates = []
REGEX_DATE = r'((\d+[/\. ]\d+[/\. ]\d+)|(\d{4}))'
# REGEX_DATE = r'(\d+.\d+.\d+)|(\d{4})'
date_result = re.findall(REGEX_DATE, line)
for res in date_result:
    all_dates.append(res[0])
print(all_dates)


def extract_dates(line):
    REGEX_DATE = r'((\d+[/\. ]\d+[/\. ][12]\d{3})|([12]\d{3}))'
    date_result = re.findall(REGEX_DATE, line)
    all_dates = []
    for res in date_result:
        all_dates.append(res[0])
    return all_dates
print(extract_dates(line))


date_list = []
file_name = 'D:/TULEVAISUUS/corpora/НКРЯ финский/Kotiin karkotettavaksi.fi.xml'
with open(file_name, 'r', encoding='UTF-8') as file:
    for line in file:
        date_list += extract_dates(line)
print(date_list)
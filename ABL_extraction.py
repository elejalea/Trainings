import re

def extract_ABL(line):
    REGEX_ABL1 = r'[A-Za-zÄÖäö]+sta\b'
    REGEX_ABL2 = r'[A-Za-zÄÖäö]+stä\b'
    ABL1_result = re.findall(REGEX_ABL1, line)
    ABL2_result = re.findall(REGEX_ABL2, line)
    return ABL1_result, ABL2_result


ABL1_result = []
ABL2_result = []
file_name = 'D:/TULEVAISUUS/corpora/НКРЯ финский/Kotiin karkotettavaksi.fi.xml'
with open(file_name, 'r', encoding='UTF-8') as file:
    for line in file:
        current1, current2 = extract_ABL(line)
        ABL1_result += current1
        ABL2_result += current2
print(ABL1_result, '\n', ABL2_result,'\n','TOTAL_sta: ', len(ABL1_result), '\n', 'TOTAL_stä: ', len(ABL2_result))
print(' UNIQUE_sta: ', len(set(ABL1_result)), '\n', 'UNIQUE_stä: ', len(set(ABL2_result)))
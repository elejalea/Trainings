txt = 'Октябрь, десятый! месяц? года. Ноябрь? одинадцатый! месяц, года.'
words = txt.split()
# for word in words:
#      word = word.strip(".,!?")
#      print(word)

for i,word in enumerate(words):
    word = word.strip(".,!?")
    words[i] = word
    print(word)
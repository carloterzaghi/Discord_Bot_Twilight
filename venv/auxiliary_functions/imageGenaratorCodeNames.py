import random
from tabulate import tabulate

def generatorImageGame(path):
    list_words = []
    selected_words = []
    words_ = open(f"./venv/dictionares/{path}", encoding="utf8")
    for i in words_:
        list_words.append((i[:-1] if i[-1:] == '\n' else i).capitalize())

    random_word = random.choice(list_words)
    while len(selected_words) != 25:
        if random_word not in selected_words:
            selected_words.append(random_word) 
        else:
            random_word = random.choice(list_words)

    fiveXfiveList = []
    n = 0
    mini_list = []

    for i in selected_words:
        n += 1
        mini_list.append(i.replace(' ','\n') if len(i.split()) > 1 else i)
        if n == 5:
            fiveXfiveList.append(mini_list)
            n = 0
            mini_list = []

    return tabulate(fiveXfiveList)
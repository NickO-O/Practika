vacavaca = dict()  # словарь с вакансиями трудоустройства
with open("vacancy.csv", encoding="utf-8") as file:
    next(file)
    for i in file:
        a = i.strip().split(";")
        vacavaca[a[-1]] = vacavaca.get(a[-1], [])
        vacavaca[a[-1]].append((a[-2], int(a[0]), a[1]))

supergood = (max(vacavaca, key=lambda x: len(vacavaca[x])))

for i in vacavaca[supergood]:
    print(f"({i[0]}, {i[1]}, {i[2]})")
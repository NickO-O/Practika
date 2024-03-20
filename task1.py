vac = dict()  # Словарь вакансий
with open("vacancy.csv", encoding="utf-8") as file:  # Открываю Файл
    next(file)
    for i in file:
        a = i.strip().split(";")
        k = vac.get(a[-1], (0, 0))[0]
        if k < int(a[0]):
            vac[a[-1]] = (int(a[0]), a[-2])

with open("vacancy_new.csv", "w", encoding="utf-8") as w:  # Записываю в файл
    w.write("company;role;Salary\n")
    for i in vac:
        w.write(i + ";" + vac[i][1] + ";" + str(vac[i][0]) + "\n")

s = sorted(vac.keys(), key=lambda x: vac[x][0], reverse=True)[:3]
for i in s:
    print(f"{i} - {vac[i][1]} - {vac[i][0]}")
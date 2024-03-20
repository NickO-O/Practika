salary = []  # Список с вакансиями
with open("vacancy.csv", encoding="utf-8") as file:
    next(file)
    for i in file:
        a = i.strip().split(";")
        salary.append((a[-1], a[-2], a[0]))

while True:
    str = (input())
    if str == "None":
        break
    glag = False
    for i in salary:
        if i[0] == str:
            print(f"В {str} найдена вакансия: {i[1]}. З/п составит: {i[-1]}")
            glag = True
    if not glag:
        print("К сожалению, ничего не удалось найти")
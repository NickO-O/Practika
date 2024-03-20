slave = dict()  # Словарь с зарплатами

with open("vacancy.csv", encoding="utf-8") as file:
    next(file)
    for i in file:
        a = i.strip().split(";")
        slave[a[1].strip().lower()] = slave.get(a[1].strip().lower(), [])
        slave[a[1].strip().lower()].append(int(a[0]))

for i in slave:  # Вычисляю среднюю зарплату
    slave[i] = sum(slave[i])/len(slave[i])

with open("vacancy_procent.csv", "w", encoding="utf-8") as file:
    file.write("Salary;Work_Type;Company_Size;Role;Company;percent\n")
    with open("vacancy.csv", encoding="utf-8") as file1:
        next(file1)
        for i in file1:
            a = i.strip().split(";")
            file.write(i.strip())
            file.write(";")
            percent = int(a[0])/slave[a[1].strip().lower()]*100
            file.write(str(percent))
            file.write("\n")
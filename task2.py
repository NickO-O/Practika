
def partition(shelf, left, right, pivot_index):
    """
    Вставляет элемент в правильную позицию

    :param shelf: То, что нужно отсортировать
    :param left: Левый индекс
    :param right: Правый индекс
    :param pivot_index: инжекс элемента, который нужно вставить
    :return: Не возвращает ничего, изменяет переданный список
    """
    pivot = shelf[pivot_index]
    shelf.insert(right, shelf.pop(pivot_index))
    store_index = left
    for i in range(left, right):
        if shelf[i][-1] < pivot[-1]:
            shelf.insert(store_index, shelf.pop(i))
            store_index = store_index + 1
    shelf.insert(store_index, shelf.pop(right))  # перемещает pivot на правильную позицию
    return store_index

def qsort(shelf, left, right):
    """
    Функция qsort-быстрая сортировка

    :param shelf: То, что нужно отсортировать
    :param left: Левый индекс
    :param right: Правый индекс
    :return: Не возвращает ничего, изменяет переданный список
    """
    if left < right:
        pivot_index = left
        pivot_new_index = partition(shelf, left, right, pivot_index)
        qsort(shelf, left, pivot_new_index - 1)
        qsort(shelf, pivot_new_index + 1, right)

robots = dict() # словарь количества работников
cls = dict()
with open("vacancy.csv", encoding="utf-8") as file:
    next(file)
    for i in file:
        a = i.strip().split(";")
        robots[a[-1]] = int(a[2])
        if a[-2] == "классный руководитель":
            cls[a[-1]] = a[0]

lst = list(robots.items())
qsort(lst, 0, len(lst) - 1)
i = list(filter(lambda x: x[0] in cls, lst))[0]
print(f"В компании {i[0]} есть заданная профессия: классный руководитель, з/п в такой компании составит: {cls[i[0]]}")

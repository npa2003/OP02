numbers = [1, 2, 3, 4, 5]

names = [ "Нина", "Андрей"]

a = [1, 56, -90, 6.7, True, None, "text"]

print("Просто список")
print(names)
print()

names.append("Кирилл")
print("Добавили Кирилла")
print(names)
print()

names.remove("Андрей")
print("Удалили Андрея")
print(names)
print()

delete = names.pop(0)
print("Удалили 0-ого")
print(names)
print(delete)
print()

a = names.index("Кирилл")
print("Вынули индекс Кирилла")
print(a)
print()

names.append("Кирилл")
names.append("Андрей")
print("Добавили Кирилла и Андрюшку")
print(names)
print("Посчитали Кирюшек")
а = names.count("Кирилл")
print(a)
print()

names.sort()
print("Отсортировали")
print(names)
print()

print("Максимальный")
print(max(names))
print(names)
print()

print("Суммируем")
a = sum(names)
print(a)
print()

names.clear()
print("Очистили")
print(names)




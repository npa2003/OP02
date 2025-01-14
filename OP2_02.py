a = []
print(" Создали")
for i in range(3):
    a.append(i*2)
    print(a[i])

print(" Добавили")
for i in range(2):
    a.insert(0,i+5)
    print(a)

print(" Отсортировали в обратном")
a.sort(reverse=True)
print(a)

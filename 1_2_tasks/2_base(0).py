my_tuple = (1, "Hello", True, 2, "FinUniversity", False, 3, "Python", True, 4)
# Создание кортежа (неизменяемого списка) с различными элементами.

index1 = int(input("Введите первый индекс (от 0 до 9): "))
# Запрос у пользователя первого индекса для доступа к элементу кортежа.
index2 = int(input("Введите второй индекс (от 0 до 9): "))
# Запрос у пользователя второго индекса для доступа к элементу кортежа.

element1 = my_tuple[index1]
# Получение элемента кортежа по первому введенному индексу.
element2 = my_tuple[index2]
# Получение элемента кортежа по второму введенному индексу.

print(f"Элемент с индексом {index1}: {element1}")
print(f"Элемент с индексом {index2}: {element2}")
# Вывод элементов, соответствующих введенным индексам.

slice_elements = my_tuple[0:3]
# Создание нового кортежа, содержащего элементы из исходного кортежа с индексами от 0 до 2 (эксклюзивно).
print("Элементы в диапазоне [0:3]:", slice_elements)
# Вывод элементов в указанном диапазоне.

print("Все элементы кортежа:", end=" ")
for item in my_tuple:
    print(item, end=" ")
# Вывод всех элементов исходного кортежа в одной строке, разделенных пробелами.
print()

copied_tuple = my_tuple * 2
# Создание нового кортежа, который является удвоенной копией исходного кортежа.
print("Копия кортежа, умноженная на 2:")
print(copied_tuple)
# Вывод удвоенной копии исходного кортежа.

immutable_var = "Water", 2024, True
print(immutable_var)
# После того как вводятся данные в переменную
# Кортеж становится неизменяемым, чтобы сохранить их нетронутыми для дальнейшего использования.
# Это свидетельствует то что команда
# immutable_var[0] = "Fire"
# При компиляции, указывает на то что данное обращение к элементу 0 и его новое присвоение невозможно

mutable_list = [25, False]
mutable_list[0] = 36
mutable_list[1] = "Spring"
mutable_list.append(True)
print(mutable_list)

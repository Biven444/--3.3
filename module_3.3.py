def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print("Разное количество аргументов:")
print_params()
print_params(10)
print_params(25)
print_params ([1, 2, 3])

print("Распаковка параметров:")
values_list = [42, 'Привет', False]
values_dict = {'a': 3.14, 'b': 'Тест', 'c': None}
print_params(*values_list)
print_params(**values_dict)

print("Распаковка + отдельные параметры:")
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)  

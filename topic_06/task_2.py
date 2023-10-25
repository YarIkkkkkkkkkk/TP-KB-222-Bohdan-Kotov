# Список словників із прикладами імен та оцінок
sp = [{'name': 'Anna', 'grade': 40},
        {'name': 'Peter', 'grade': 35},
        {'name': 'Michael', 'grade': 88},
        {'name': 'Ivan', 'grade': 50},
        {'name': 'Nadja', 'grade': 30},
        {'name': 'Vitalii', 'grade': 55},
        {'name': 'Alexander', 'grade': 83},
        {'name': 'Boris', 'grade': 92},
        {'name': 'Sergey', 'grade': 30},
        {'name': 'Eugene', 'grade': 75},
        {'name': 'Bohdan', 'grade': 92}]

parameter = input("Виберіть ключ для сортування : ")

def sort_data(sp, parameter):
    if parameter == 'name':
        return sorted(sp, key=lambda x: x['name'])
    elif parameter == 'grade':
        return sorted(sp, key=lambda x: x['grade'])
    else:
        print("Неправильний ключ сортування.")
        return sp

# Виведення відсортованого списку
sorted_data = sort_data(sp, parameter)

for item in sorted_data:
    print(f"Ім'я: {item['name']}, Оцінка: {item['grade']}")
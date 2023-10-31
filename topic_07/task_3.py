class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

students = [
    Student("Віктор", 19),
    Student("Григорій", 21),
    Student("Богдан", 19),
    Student("Степан", 25),
    Student("Марія", 24),
    Student("Ярослав", 28)
]

sort= input("Якщо бажаєте сортувати за віком введіть 'В',якщо сортувати за алфавітом введіть 'А' ")

if sort == 'А':
        students = sorted(students, key=lambda x: x.name)
else:
        students = sorted(students, key=lambda x: x.age)

for student in students:
    print(f"Ім'я: {student.name}, Вік: {student.age}")

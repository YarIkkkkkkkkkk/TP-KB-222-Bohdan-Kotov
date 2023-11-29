from Student import Student
class StudentList:
    def __init__(self):
        self.students = []

    def printAllList(self):
        for elem in self.students:
            strForPrint = "Student name is " + elem.name + ",  Phone is " + elem.phone + ", Gender is " + elem.gender + ", Country is " + elem.country
            print(strForPrint)

    def addNewElement(self):
        name = input("Please enter student name: ")
        phone = input("Please enter student phone: ")
        gender = input("Please enter student gender: ")
        country = input("Please enter student country: ")
        insertPosition = 0
        for item in self.students:
            if name > item.name:
                insertPosition += 1
            else:
                break
        self.students.insert(insertPosition, Student(name, phone, gender, country))
        print("New element has been added")

    def deleteElement(self):
        name = input("Please enter name to be deleted: ")
        deletePosition = -1
        for item in self.students:
            if name == item.name:
                deletePosition = self.students.index(item)
                break
        if deletePosition == -1:
            print("Element was not found")
        else:
            del self.students[deletePosition]

    def updateElement(self):
        name = input("Please enter name to be updated: ")
        for index, elem in enumerate(self.students):
            if name == elem.name:
                new_name = input("Please enter new name: ")
                new_phone = input("Please enter new phone number: ")
                new_gender = input("Please enter new gender: ")
                new_country = input("Please enter new country: ")
                updated_item = Student(new_name, new_phone, new_gender, new_country)
                del self.students[index]
                insertPosition = 0
                for pos, elem in enumerate(self.students):
                    if new_name > elem.name:
                        insertPosition = pos + 1
                    else:
                        break
                self.students.insert(insertPosition, updated_item)
                print("Element has been updated")
                break
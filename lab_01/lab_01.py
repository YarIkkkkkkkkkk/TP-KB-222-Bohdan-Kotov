list = [
    {"name":"Bob", "phone":"0631234567", "gender":"man", "country":"Ukraine"},
    {"name":"Emma", "phone":"0631234567", "gender":"woman", "country":"USA"},
    {"name":"Jon",  "phone":"0631234567", "gender":"man", "country":"France"},
    {"name":"Zak",  "phone":"0631234567", "gender":"man", "country":"Ukraine"}
]

def printAllList():
    for elem in list:
        strForPrint = "Student name is " + elem["name"] + ",  Phone is " + elem["phone"] + ", Gender is " + elem["gender"] + ", Country is " + elem["country"]
        print(strForPrint)
    return

def addNewElement():
    name = input("Pease enter student name: ")
    phone = input("Please enter student phone: ")
    gender = input("Please enter student gender: ")
    country = input("Please enter student country: ")
    newItem = {"name": name, "phone": phone , "gender": gender , "country": country}
    insertPosition = 0
    for item in list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    list.insert(insertPosition, newItem)
    print("New element has been added")
    return

def deleteElement():
    name = input("Please enter name to be delated: ")
    deletePosition = -1
    for item in list:
        if name == item["name"]:
            deletePosition = list.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Dele position " + str(deletePosition))
        del list[deletePosition]
    return


def updateElement():
    name = input("Please enter name to be updated: ")
    for index, elem in enumerate(list):
        if name == elem["name"]:
            new_name = input("Please enter new name: ")
            new_phone = input("Please enter new phone number: ")
            new_gender = input("Please enter new gender: ")
            new_country = input("Please enter new country: ")
            updated_item = {"name": new_name, "phone": new_phone, "gender": new_gender, "country": new_country}
            del list[index]
            insertPosition = 0
            for pos, elem in enumerate(list):
                if new_name > elem["name"]:
                    insertPosition = pos + 1
                else:
                    break
            list.insert(insertPosition, updated_item)
            print("Element has been updated")
            break
    else:
        print("Element not found")


def main():
    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match chouse:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Existing element will be updated")
                updateElement()
                printAllList()
            case "D" | "d":
                print("Element will be deleted")
                deleteElement()
            case "P" | "p":
                print("List will be printed")
                printAllList()
            case "X" | "x":
                print("Exit()")
                break
            case _:
                print("Wrong chouse")


main()
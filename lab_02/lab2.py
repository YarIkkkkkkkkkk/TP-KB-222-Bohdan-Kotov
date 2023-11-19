import csv
import sys

def get_data(file_name):
    list=[]
    with open(file_name) as file:
        reader = csv.DictReader(file)
        for row in reader:
            list.append({"name": row["name"], "phone": row["phone"], "gender": row["gender"], "country": row["country"]})
    return list
def save_data(file_name,list):
    with open(file_name, "w", newline='') as csvfile:
        fieldnames = ["name","phone","gender","country"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(list)



def printAllList(list):
    for elem in list:
        strForPrint = "Student name is " + elem["name"] + ",  Phone is " + elem["phone"] + ", Gender is " + elem["gender"] + ", Country is " + elem["country"]
        print(strForPrint)
    return

def addNewElement(list):
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

def deleteElement(list):
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


def updateElement(list):
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
    print("Element not found")


def main():
    if len(sys.argv) != 2:
        sys.exit(1)
    
    file_name = sys.argv[1]
    list = get_data(file_name)

    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match chouse:
            case "C" | "c":
                print("New element will be created:")
                addNewElement(list)
                printAllList(list)
            case "U" | "u":
                print("Existing element will be updated")
                updateElement(list)
                printAllList(list)
            case "D" | "d":
                print("Element will be deleted")
                deleteElement(list)
            case "P" | "p":
                print("List will be printed")
                printAllList(list)
            case "X" | "x":
                print("Exit()")
                save_data(file_name,list)
                break
            case _:
                print("Wrong chouse")


if __name__ == "__main__":
    main()
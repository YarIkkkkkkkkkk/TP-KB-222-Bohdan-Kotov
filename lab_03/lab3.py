import sys
from Utils import FileManager
from StudentList import StudentList

def main():
    list = StudentList()
    if len(sys.argv) != 2:
        sys.exit(1)

    file_name = sys.argv[1]
    FileManager.get_data(file_name, list)

    while True:
        choice = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        if choice.lower() == "c":
            print("New element will be created:")
            list.addNewElement()
            list.printAllList()
        elif choice.lower() == "u":
            print("Existing element will be updated")
            list.updateElement()
            list.printAllList()
        elif choice.lower() == "d":
            print("Element will be deleted")
            list.deleteElement()
            list.printAllList()
        elif choice.lower() == "p":
            print("List will be printed")
            list.printAllList()
        elif choice.lower() == "x":
            print("Exit()")
            FileManager.save_data(file_name, list)
            break
        else:
            print("Wrong choice")

if __name__ == "__main__":
    main()

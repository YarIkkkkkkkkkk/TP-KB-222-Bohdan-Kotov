from Student import Student
import csv
class FileManager:
    @staticmethod
    def get_data(file_name, list):
        list.students = []
        with open(file_name, 'r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                list.students.append(Student(row[0], row[1], row[2], row[3]))
        return list

    @staticmethod
    def save_data(file_name, list):
        with open(file_name, "w") as file:
            file.write("name,phone,gender,country\n")
            for elem in list.students:
                rov = f"{elem.name},{elem.phone},{elem.gender},{elem.country}\n"
                file.write(rov)
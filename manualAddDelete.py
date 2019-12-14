import csv


def update_employee_manually(action):
    existing_list = read_existing_file()
    user_input = employee_input_data()
    if action == "add":
        if user_input in existing_list:
            print("Employee already in the list.")
            exit(0)
        else:
            write_to_list(add_employee_manually(user_input, existing_list))
            print("{} was added to the list.".format(user_input[1].title()))
    if action == "delete":
        if user_input in existing_list:
            write_to_list(delete_employee_manually(user_input, existing_list))
            print("{} was deleted from the list".format(user_input[1].title()))
        else:
            print("No employee was found to delete.")


def read_existing_file():
    existing_employee_list = []
    with open("full employee list.csv", 'r', newline="") as to_list:
        reader = csv.reader(to_list)
        next(reader)
        for row in reader:
            existing_employee_list.append(row)
    return existing_employee_list


def add_employee_manually(user_input, existing_list):
    to_list = []
    for each in existing_list:
        to_list.append(each)
    to_list.append(user_input)
    return to_list


def write_to_list(to_list):
    with open('full employee list.csv', 'w', newline="") as full_list:
        writer = csv.writer(full_list)
        writer.writerow(["id", "name", "phone", "age"])
        writer.writerows(to_list)


def delete_employee_manually(user_input, existing_list):
    to_list = []
    for each in existing_list:
        to_list.append(each)
        if user_input in to_list:
            to_list.remove(each)
    return to_list


def employee_input_data():
    id_input = _id_input_error_handle()
    name_input = _name_input_error_handle()
    phone_input = _phone_input_error_handle()
    age_input = _age_input_error_handle()
    input_data = [str(id_input), name_input, phone_input, str(age_input)]
    return input_data


def _id_input_error_handle():
    flag = True
    while flag:
        try:
            id_input = input("Enter id: ").strip()
            id_input = int(id_input)
            assert id_input > 0
            flag = False
        except ValueError:
            print("Id must be a number")
        except AssertionError:
            print("Id must be a positive number")
        else:
            return id_input


def _name_input_error_handle():
    flag = True
    while flag:
        try:
            name_input = input("Enter name: ")
            name_input = name_input.title().strip()
            spl = []
            if " " in name_input:
                spl = name_input.split()
            else:
                assert name_input.isalpha()
            for each in spl:
                assert (each.isalpha())
            flag = False
        except AssertionError:
            print("Please type letters only")
        else:
            return name_input


def _phone_input_error_handle():
    flag = True
    while flag:
        try:
            phone_input = input("Enter phone number: ").strip()
            assert phone_input.isnumeric()
            flag = False
        except AssertionError:
            print("Please enter numbers only")
        else:
            return phone_input


def _age_input_error_handle():
    flag = True
    while flag:
        try:
            age_input = input("Enter age: ").strip()
            age_input = int(age_input)
            assert age_input > 0
            flag = False
        except ValueError:
            print("Age must be a number")
        except AssertionError:
            print("Age must be a positive number.")
        else:
            return age_input

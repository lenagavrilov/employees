import csv


def update_employee_from_file(action):
    from_list = get_data_from_list()
    to_list = retrieve_existing_data()
    updated_employee_list = []
    count_updated_records = 0
    for each in to_list:
        updated_employee_list.append(each)
    if action == "add":
        write_to_file(add_employee_from_list(from_list,
                                             updated_employee_list,
                                             count_updated_records))
    if action == "delete":
        write_to_file(delete_employee_from_list(from_list,
                                                updated_employee_list,
                                                count_updated_records))


def add_employee_from_list(from_list,
                           updated_employee_list,
                           count_updated_records):
    for employee in from_list:
        if employee not in updated_employee_list:
            updated_employee_list.append(employee)
            count_updated_records += 1
            name = employee[1]
            print("{} was added to the list."
                  .format(name.title()))
    print_add_results(count_updated_records)
    return updated_employee_list


def delete_employee_from_list(from_list,
                              updated_employee_list,
                              count_updated_records):
    for employee in from_list:
        if employee in updated_employee_list:
            updated_employee_list.remove(employee)
            count_updated_records += 1
            name = employee[1]
            print("{} was removed from the list."
                  .format(name.title()))
    print_remove_results(count_updated_records)
    return updated_employee_list


def get_data_from_list():
    from_list = []
    with open("employee list.csv", 'r') as fromFile:
        reader = csv.reader(fromFile)
        next(reader)
        for row in reader:
            from_list.append(row)
        if not from_list:
            print("Your list is empty.")
            exit(0)
        for each in from_list:
            if not each:
                from_list.remove(each)
            if len(each) != 4:
                print("There should be exactly 4 values. "
                      "Check this line: {}.".format(each))
                print("No data was changed in the main list.")
                exit(0)
    data_validation(from_list)
    for each in from_list:
        each[1] = each[1].title()
    return from_list


def retrieve_existing_data():
    to_list = list()
    with open("full employee list.csv", 'r') as toFile:
        reader = csv.reader(toFile)
        next(reader)
        for row in reader:
            to_list.append(row)
    for each in to_list:
        if not each:
            to_list.remove(each)
    return to_list


def data_validation(from_list):
    _id_input_from_list_error_handle(from_list)
    _name_input_from_list_error_handle(from_list)
    _phone_input_from_list_error_handle(from_list)
    _age_input_from_list_error_handle(from_list)
    return from_list


def write_to_file(updated_employee_list):
    with open('full employee list.csv', 'w', newline="") as inputFile:
        writer = csv.writer(inputFile)
        writer.writerow(["id", "name", "phone", "age"])
        writer.writerows(updated_employee_list)


def print_add_results(count_updated_records):
    if count_updated_records == 0:
        print("No new employees were found.")
        exit(0)
    else:
        print("Total number of added employees: {}."
              .format(count_updated_records))


def print_remove_results(count_updated_records):
    if count_updated_records == 0:
        print("No employees were found to delete.")
        exit(0)
    else:
        print("Total number of deleted employees: {}."
              .format(count_updated_records))


def _id_input_from_list_error_handle(employee_to_add):
    flag = True
    while flag:
        for each in employee_to_add:
            if not each:
                pass
            try:
                id_input = each[0]
                assert int(id_input) > 0
                flag = False
            except ValueError:
                print("Id must be a number")
                print("Check employee {}.".format(each))
                exit(0)
            except AssertionError:
                print("Id must be a positive number")
        return id_input.strip()


def _name_input_from_list_error_handle(employee_to_add):
    flag = True
    while flag:
        for each in employee_to_add:
            try:
                name_input = each[1].title()
                spl = []
                if " " in name_input:
                    spl = name_input.split()
                else:
                    assert name_input.isalpha()
                for name in spl:
                    assert (name.isalpha())
                flag = False
            except AssertionError:
                print("Name must contain letters only")
                print("Check this line: {}.".format(each))
                exit(0)
        return name_input.strip()


def _phone_input_from_list_error_handle(employee_to_add):
    flag = True
    while flag:
        for each in employee_to_add:
            try:
                phone_input = each[2]
                phone_input = phone_input.strip()
                assert phone_input.isnumeric()
                flag = False
            except AssertionError:
                print("Phone number is not correct. Must be numbers only.")
                print("Check this line: {}".format(each))
                print("No employees were added.")
                exit(0)
        return phone_input.strip()


def _age_input_from_list_error_handle(employee_to_add):
    flag = True
    while flag:
        for each in employee_to_add:
            try:
                age_input = each[3].strip()
                age_input = int(age_input)
                assert age_input > 0
                flag = False
            except ValueError:
                print("Age must be a number.  Check this line: {}."
                      .format(each))
                print("No employees were added")
                exit(0)
            except AssertionError:
                print("Age must be a positive number. Check this line: {}"
                      .format(each))
                print("No employees were added.")
                exit(0)
        return age_input

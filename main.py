import addDeleteFromList
import manualAddDelete
import attendance

def employer_vs_employee():
    who_are_you = input("If you are an employer, type '1'. \n"
                        "If you are an employee, type '2'. \n")\
        .strip()
    if who_are_you == '1':
        employer_action()
    elif who_are_you == '2':
        employee_action()
    else:
        print("Didn't get who you are. Try again!")


def employee_action():
    what_to_do = input("To add entry time type 'entry'. \n"
                       "To add exit time type 'exit'. \n")\
        .strip()
    if what_to_do == 'entry':
        attendance.add_entry('start')
    elif what_to_do == 'exit':
        attendance.add_entry('finish')
    else:
        print("Didn't get your choice.")


def employer_action():
    what_to_do = input("To add employee(s) type 'add'. \n"
                       "To delete employee(s) type 'delete'.\n")\
        .strip()
    what_to_do = what_to_do.lower()
    if what_to_do == 'add':
        adding()
    elif what_to_do == 'delete':
        deleting()
    else:
        print("Your choice is not valid.")
        exit(0)


def adding():
    action = input("To add employee manually type M.\n"
                   "To add employee from the list type L.")
    action = action.upper().strip()
    print("Adding employee(s)...")
    if action == 'M':
        manualAddDelete.update_employee_manually("add")
    elif action == "L":
        path = input("Enter file location: ").strip()
        addDeleteFromList.update_employee_from_file("add", path)
    else:
        print("Cannot get your choice.")
        exit(0)


def deleting():
    action = input("To delete employee manually type m.\n"
                   "To delete employee from the list type l.")
    action = action.upper().strip()
    print("Deleting employee(s)...")
    if action == 'M':
        manualAddDelete.update_employee_manually('delete')
    elif action == "L":
        path = input("Enter file location: ").strip()
        addDeleteFromList.update_employee_from_file("delete", path)
    else:
        print("Cannot get your choice.")
        exit(0)


if __name__ == "__main__":
    employer_vs_employee()

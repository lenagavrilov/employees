import addDeleteFromList
import manualAddDelete


def user_action():
    what_to_do = input("To add employee(s) type 'add'. \n"
                       "To delete employee(s) type 'delete'.\n")\
        .strip()
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
        manualAddDelete.update_employee_manually('add')
    elif action == "L":
        addDeleteFromList.update_employee_from_file("add")
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
        addDeleteFromList.update_employee_from_file("delete")
    else:
        print("Cannot get your choice.")
        exit(0)


if __name__ == "__main__":
    user_action()

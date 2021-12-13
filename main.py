"""PhoneBook
"""
from os import system
import sys


def add():
    """add user to phoneboot
    """
    clear_screen()
    name = "empty"
    number = "empty"
    while name and number:
        name = input("Enter Contact 'Name'(just enter to go to 'menu'): ")
        if not name:
            break
        number = input("Enter Contact 'Number'(just enter to go to 'menu'): ")
        if not number:
            break
        with open("database.txt", "a") as database:
            data = f"{name}:{number}\n"
            database.write(data)

        print(f"Added '{name}' to Contacts\n")

    menu()


def search():
    """search in phonebook
    """
    clear_screen()
    input_ = "empty"
    while input_:
        input_ = input(
            "Enter anythings to 'Search' it(just enter to go to 'menu'): ")
        if not input_:
            break
        find = False
        with open("database.txt", "r") as database:
            lines = database.readlines()
            for line in lines:
                if input_ in line:
                    find = True
                    line = line.strip().split(":")
                    print(f"{line[0]} -> {line[1]}")
        if not find:
            print("Name or Number Not Found")
        print()

    menu()


def show():
    """show all data in phonebook
    """
    clear_screen()
    with open("database.txt", "r") as database:
        lines = database.readlines()
        if lines:
            for line in lines:
                if line:
                    line = line.strip().split(":")
                    print(f"{line[0]} -> {line[1]}")
        else:
            print("No Any Contacts!")
    input("\nEnter to Go To Menu...")
    menu()


def delete():
    """delete user from phonebook
    """
    clear_screen()
    name = "empty"
    while name:
        name = input(
            "Enter contact name to 'Delete' it(just enter to go to 'menu'): ")
        if not name:
            break
        find = False
        with open("database.txt", "r") as database:
            lines = database.readlines()
            new_data = ''
            for line in lines:
                if name == line.strip().split(":")[0]:
                    find = True
                    print(f"Contact '{name}' Deleted")
                    continue
                new_data += line
        with open("database.txt", "w") as database:
            database.write(new_data)

        if not find:
            print(f"Contact '{name}' Not Found")
        print()

    menu()


def exit_():
    """exit from application
    """
    clear_screen()
    sys.exit()


def clear_screen():
    """clear screen
    """
    system("clear")


menu_dict = {
    "Add": add,
    "Search": search,
    "Show": show,
    "Delete": delete,
    "Exit": exit_,
}
menu_list = [
    "Add",
    "Search",
    "Show",
    "Delete",
    "Exit",
]


def menu():
    """phonebook menu
    """
    clear_screen()
    print("PhoneBook Menu...")
    for index, option in enumerate(menu_list):
        print(f"{option}({index+1})")
    input_ = input("Choose Option(enter index): ")
    while input_ not in ("1", "2", "3", "4", "5"):
        print("Please just enter 1, 2, 3, 4 or 5")
        input_ = input("Choose Option(enter index): ")
    index_choose = int(input_[0])
    function = menu_dict[menu_list[index_choose-1]]
    function()


if __name__ == "__main__":
    try:
        with open("database.txt", "x"):
            pass
    except FileExistsError:
        pass

    menu()

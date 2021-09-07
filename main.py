from prettytable import PrettyTable
import random
import string
import sys

animal_dic = {}


# ~~~~~~~~~~~~~~~~~~ Functions(): ~~~~~~~~~~~~~~~~~~~
def main():
    # ~~~~~~~~~~~~~~ User's choise ~~~~~~~~~~~~~~~
    while True:
        instrucctions()
        user_input = input("\nWhat do you want to do? "
                           "(a, d, u, l, e): ").lower()
        if user_input == "a":
            add_animal()
        elif user_input == "d":
            delete_animal()
        elif user_input == "u":
            update_animal()
        elif user_input == "l":
            print_register()
        elif user_input == "e":
            exit_program()
        elif not user_input:
            print("please, enter something!")


def instrucctions():
    print('\nAnimal registry program:'
          '\n1: Enter A or a to add new animal.'
          '\n2: Enter D or d to delete a animal'
          '\n3: Enter U or u to update animal.'
          '\n4: Enter L or l to check list of animals. '
          '\n5: Enter E or e to exit the program.')


def print_register():
    x = PrettyTable(["ID", "Scientific Name", "Common Name"])
    for animal_data in animal_dic:
        x.add_row([animal_data, animal_dic[animal_data]["scientific_name"],
                   animal_dic[animal_data]["common_name"]])

    print(x.get_string(title="Animal Registry"))


def random_id():
    random_string = ''.join(random.choices(string.ascii_uppercase
                                           + string.digits, k=4))
    return random_string


def add_animal():
    animal_id = random_id()
    scientific_name = input("\nPlease enter the scientific name: ").title()
    common_name = input("\nPlease enter the common name: ").title()
    data = {animal_id: {'scientific_name': scientific_name,
                        'common_name': common_name}}
    if not scientific_name and not common_name:
        print("You must write something!")
    else:
        animal_dic.update(data)


def delete_animal():
    animal_id = input("\nEnter the animal ID you want delete: ").upper()
    if animal_id in animal_dic:
        choice = input("Delete (y/n)").lower()
        if choice == "yes" or choice == "y":
            del animal_dic[animal_id]
            print(f"{animal_id} register has been deleted!")
    else:
        print("\n>ID not found. Check list pressing 'L'")


def update_animal():
    animal_id = input("\nEnter the animal ID you want update: ").upper()
    # If key in dictionary, if key is equal to ID (animal_id)
    for animal in animal_dic:
        if animal == animal_id:
            choice = input(f"Update register {animal_id}? (y/n): ").lower()
            if choice == "yes" or choice == "y":
                # Changing names
                scientific_name = input("Write a new"
                                        "scientific name: ").title()
                common_name = input("Write a new common name: ").title()
                if not scientific_name and not common_name:
                    print("You must write something!")
                else:
                    animal_dic[animal]['scientific_name'] = scientific_name
                    animal_dic[animal]['common_name'] = common_name
                    print("Register updated!")
                    print_register()
        else:
            print("\n>ID not found. Check list pressing 'L'")


def exit_program():
    sys.exit("Goodbye!")


if __name__ == "__main__":
    main()

# shopping_list_manager.py

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    shopping_list = []

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            item = input("Enter item to add: ").strip()
            if item:  # avoid adding empty strings
                shopping_list.append(item)
                print(f"'{item}' added to the shopping list.\n")
            else:
                print("No item entered. Nothing added.\n")

        elif choice == '2':
            item = input("Enter item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' removed from the shopping list.\n")
            else:
                print(f"'{item}' not found in the shopping list.\n")

        elif choice == '3':
            if shopping_list:
                print("Current shopping list:")
                for idx, it in enumerate(shopping_list, start=1):
                    print(f"{idx}. {it}")
                print()  # blank line for spacing
            else:
                print("Shopping list is empty.\n")

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()

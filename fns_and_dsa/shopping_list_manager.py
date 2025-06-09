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
        choice = input("Enter your choice: ")
        choice = choice.strip()
        if choice == '1':
            choice = choice.strip()
            shopping_list.append()
        elif choice == '2':
            choice = choice.strip()
            shopping_list.remove()
        elif choice == '3':
            choice = choice.strip()
            print(shopping_list)
        elif choice == '4':
            choice = choice.strip()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. please try again.")

    if __name__ == "__main__":
        main()





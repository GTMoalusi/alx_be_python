shopping_list = []

def add_item(item):
    shopping_list.append(item)
    return f"Item '{item}' added to the shopping list."

def remove_item(item):
    if item in shopping_list:
        shopping_list.remove(item)
        return f"Item '{item}' removed from the shopping list."
    else:
        return f"Error: Item '{item}' not found in the shopping list."
    
def view_list():
    if shopping_list:
        return "Shopping List:\n" + "\n".join(shopping_list)
    else:
        return "Shopping list is empty."  
    
def clear_list():
    shopping_list.clear()
    return "Shopping list cleared."

def display_menu():
   print("Shopping List Manager Menu")
   print("1. Add item")
   print("2. Remove item")
   print("3. View list")
   print("4. Clear list")
   print("5. Exit")

def run_shopping_list_manager():
    
    while True:
        # Display the menu options to the user
        print(display_menu())

        # Get the user's choice
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            # Add item functionality
            item_to_add = input("Enter the item to add: ")
            print(add_item(item_to_add))
        elif choice == '2':
            # Remove item functionality
            item_to_remove = input("Enter the item to remove: ")
            print(remove_item(item_to_remove))
        elif choice == '3':
            # View list functionality
            print(view_list())
        elif choice == '4':
            # Clear list functionality
            print(clear_list())
        elif choice == '5':
            # Exit the program
            print("Exiting Shopping List Manager. Goodbye!")
            break  # Break out of the while loop to end the program
        else:
            # Handle invalid menu choices
            print("Invalid choice. Please enter a number between 1 and 5.")

# Run the manager when the script is executed
if __name__ == "__main__":
    run_shopping_list_manager()

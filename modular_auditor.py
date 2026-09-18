inventory = 0
entries = 0
rejected_entries = 0

# Loop to continuously prompt the user for input until they choose to exit
while True:
    user_input = input("\nPlease enter the number of items to add to inventory or type 'exit' to quit: ")
    entries += 1 
    if user_input.lower() == 'exit':
        entries -= 1  # Decrement entries count since 'exit' is not a valid entry
        print("Total Units Processed:", inventory)
        print("Total entries made:", entries)
        break

    # Checks for negative numbers   
    if user_input.startswith('-') and user_input[1:].replace('.', '').isdigit(): # Checks for int/float negative numbers by replacing the "." in case of negative float numbers
        print("Invalid input. Please enter a non-negative integer number or type 'exit' to quit.")
        rejected_entries += 1
        continue

    # Checks for handle invalid input (non-integer values)    
    if not user_input.isdigit():
        print("Invalid input. Please enter an integer number or type 'exit' to quit.")
        rejected_entries += 1
        continue

    items_to_add = int(user_input) # Convert the user input to an integer
    inventory += items_to_add

    # Check if inventory exceeds 500 units
    if inventory > 500:
        print("Inventory exceed 500 units.", "Current units:", inventory)
        print("Number of entries:", entries)
        print("Number of Failed/Rejected Entries:", rejected_entries)
        break

    print("Inventory updated. Current stock:", inventory)
    print("Number of entries:", entries)
    print("Number of Failed/Rejected Entries:", rejected_entries)



 


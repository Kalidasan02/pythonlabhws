# Start with an empty inventory list
inventory = []

# Function to add an item to the inventory
def add_item(item):
    inventory.append(item)
    print(f"Added '{item}' to the inventory.")

# Recursive function to count items in the list
def count_items(items):
    # Base Case: if the list is empty, return 0
    if not items:
        return 0
    # Recursive Step: count 1 for the current item and recurse for the rest
    return 1 + count_items(items[1:])

# Main function
def main():
    # Add items using add_item function
    add_item("dog food")
    add_item("cat toy")
    add_item("bird cage")
    add_item("fish tank")

    print("\n--- Inventory List ---")

    # Lambda function to display each item
    show_item = lambda item: print(f"Item in Stock: {item}")

    # Loop through each item and display it
    for item in inventory:
        show_item(item)

    # Count total number of items
    total = count_items(inventory)
    print(f"\nTotal number of items in stock: {total}")

# Run the program
main()

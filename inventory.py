inventory = {}

def add_item(item: str, price: float, stock: int) -> None:
    if item in inventory:
        print(f"Error: Item '{item}' already exists.")
    else:
        inventory[item] = {"price": price, "stock": stock}
        print(f"Item '{item}' added successfully.")

def update_stock(item: str, quantity:int) -> None:
    if item not in inventory:
        print(f"Error: Item '{item}' not found.")
    else:
        old_stock = inventory[item]["stock"]
        inventory[item]["stock"] += quantity
        if inventory[item]["stock"] < 0:
            print(f"Error: Insufficient stock for '{item}'.")
            inventory[item]["stock"] = old_stock
        else:
            print(f"Stock for '{item}' updated successfully.")

add_item("Apple", 0.5, 100)
add_item("Banana", 0.2, 50)
add_item("Apple", 0.6, 30)  # Should print an error
update_stock("Apple", -20)
update_stock("Banana", 30)
update_stock("Orange", 10)  # Should print an error
update_stock("Apple", -90)
print(inventory)  
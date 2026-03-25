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

def check_availability(item:str) -> None:
    if item in inventory:
        return inventory[item]["stock"]
    else:
        return "Item not found"

def sales_report(sales: dict) -> str:
    total = 0
    for item, quantity in sales.items():
        if item not in inventory:
            print(f"Error: Item '{item}' not found.")
            continue
        elif inventory[item]["stock"] < quantity:
            print(f"Error: Insufficient stock for '{item}'.")
            continue
        else:
            inventory[item]["stock"] -= quantity
            total += quantity * inventory[item]["price"]
    return f"Total revenue: ${total:.2f}"

add_item("Apple", 0.5, 50)
add_item("Banana", 0.2, 60)
sales = {"Apple": 30, "Banana": 20, "Orange": 10} 
print(sales_report(sales))
print(inventory)
        

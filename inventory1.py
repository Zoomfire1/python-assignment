inventory = {
    'pen': (10, 50),
    'pencil': (5, 100),
    'eraser': (8, 75)
}

def update_quantity(item_name, quantity_sold):
  
    if item_name in inventory:
        price, current_quantity = inventory[item_name]
        if quantity_sold <= current_quantity:
           
            inventory[item_name] = (price, current_quantity - quantity_sold)
            print(f"Updated {item_name}: {inventory[item_name]}")
        else:
            print(f"Not enough {item_name} in stock.")
    else:
        print(f"Error: {item_name} does not exist in the inventory.")

update_quantity('pen', 10)
update_quantity('pencil', 150) 
update_quantity('eraser', 5)

print(inventory)


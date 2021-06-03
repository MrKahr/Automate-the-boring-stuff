def display_inventory(inventory):
    print("Inventory:")
    item_total = 0
    # loop through all the items in the inventory
    for items, amount in inventory.items():
        # print items and the amount of items
        # NOTE: No plurals
        print(str(items) + " " + str(amount))
        item_total = item_total + amount
    print("Total number of items: " + str(item_total))

def add_to_inventory(inventory, added_items):
    for items in dragon_loot:
        # if the item is already in inventory, add 1 to the type.
        if items in inv:
            inv[items] = inv[items] + 1
        # if the item is not in inventory
        else:
            inventory[items] = 1
    return(inv)

inv = {'gold coin': 42, 'rope': 1}
display_inventory(inv)

dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)



stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def display_inventory(inventory):
    print('Inventory:')

    item_total = 0

    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v

    print('Total number of items: %s' % item_total)


display_inventory(stuff)

dragon_loot = ['rope', 'torch', 'ruby']


def add(inv, loot):
    for thing in loot:
        if thing in inv:
            inv[thing] += 1
        else:
            inv[thing] = 1

    display_inventory(inv)


print('-' * 30)

add(stuff, dragon_loot)

class Item:

    def __init__(self, id):
        self.properties = {}

        if id == "hat":
            self.name = "Hat"
            self.type = "head"
            self.properties["def"] = 1
            self.properties["durability"] = 20
        elif id == "basic_sword":
            self.name = "Basic Sword"
            self.type = "weapon"
            self.properties["atk"] = 3
            self.properties["durability"] = 100

    def __str__(self):
        return f"{self.name} (type: {self.type})"
    

class Inventory:
    def __init__(self):
        self.backpack = []
        self.eqp = {}
        self.eqp["head"] = None
        self.eqp["body"] = None
        self.eqp["feet"] = None
        self.eqp["weapon"] = None
    
    def add_item(self, i):
        if isinstance(i, Item):
            self.backpack.append(i)

    def show_backpack(self):
        print("\nBackpack contents:")

        if len(self.backpack) == 0:
            print("Empty.")


        for i in range(len(self.backpack)):
            print(f"{i+1}: {self.backpack[i]}")



    def drop_item(self, index):
        if index < 1 or index > len(self.backpack):
            print("Invalid index.")
            return
        
        self.backpack.pop(index-1)



    def equip(self, index):
        if index < 1 or index > len(self.backpack):
            print("Invalid index.")
            return
        
        item = self.backpack.pop(index-1)

        if item.type not in self.eqp.keys():
            print("Item cannot be equipped.")
            self.backpack.append(item)
            return
        
        if self.eqp[item.type] is not None:
            self.backpack.append(self.eqp[item.type])

        self.eqp[item.type] = item

    def show_eqp(self):

        print("\nEquipment:")

        for item_type in self.eqp.keys():
            if self.eqp[item_type] is None:
                print(item_type, ": empty")
            
            else:
                print(f"{item_type}: {self.eqp[item_type]}")
    
    def unequip(self, slot):
        if slot not in self.eqp.keys():
            print("Invalid slot.")
            return

        if self.eqp[slot] is None:
            print("Slot already empty.")
            return
        
        item = self.eqp[slot]
        self.backpack.append(item)
        self.eqp[slot] = None

    def get_stats(self):
        combat_stats = {
            "atk": 0,
            "def": 0
        }
        for item in self.eqp.values():
            if item is not None:
                for prop,val in item.properties.items():
                    if prop in combat_stats.keys():
                        combat_stats[prop] += val
        return combat_stats


inv = Inventory()
inv.add_item(Item("hat"))
inv.add_item(Item("basic_sword"))

inv.show_backpack()

inv.equip(1)
inv.show_backpack()
inv.show_eqp()
print(inv.get_stats())
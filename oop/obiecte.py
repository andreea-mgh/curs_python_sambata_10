class Item:

    # self = proprietati ale fiecarui item in parte
    
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
            self.properties["attack"] = 3
            self.properties["durability"] = 100
    
    def __str__(self):
        return f"{self.name} (type: {self.type})"
    

class Inventory:
    
    def __init__(self):
        self.slot_head = None
        self.slot_body = None
        self.slot_feet = None
        self.slot_weapon = None
        self.backpack = []
    
    def add_item(self, item):
        if isinstance(item, Item):
            self.backpack.append(item)
    
    def show_backpack(self):
        if len(self.backpack) == 0:
            print("Backpack is empty.")
        else:
            print("\nBackpack contents:")
            for i in range(len(self.backpack)):
                print(f"{i+1}: {self.backpack[i]}")
    
    def drop_item(self, index):
        if index < 1 or index >= len(self.backpack) + 1:
            print("invalid index")
            return
        
        self.backpack.pop(index-1)
        # push = adauga un element
        # pop  = scoate un element

    def equip(self, index):
        if index < 1 or index >= len(self.backpack) + 1:
            print("invalid index")
            return
        
        item = self.backpack.pop(index-1)

        if item.type not in ['head', 'body', 'feet', 'weapon']:
            print("item cannot be equipped")
            return

        if item.type == 'head':
            if self.slot_head is not None:
                self.backpack.append(self.slot_head)
            self.slot_head = item

        if item.type == 'body':
            if self.slot_body is not None:
                self.backpack.append(self.slot_body)
            self.slot_body = item
        
        if item.type == 'feet':
            if self.slot_feet is not None:
                self.backpack.append(self.slot_feet)
            self.slot_feet = item

        if item.type == 'weapon':
            if self.slot_weapon is not None:
                self.backpack.append(self.slot_weapon)
            self.slot_weapon = item

    def show_equipment(self):
        print()

        if self.slot_head is None:
            print("Head: Empty")
        else:
            stats = ""
            for stat, val in self.slot_head.properties.items():
                stats += f"- {stat}: {val}\n"
            print(f"Head: {self.slot_head.name}\n{stats}")
        
        if self.slot_body is None:
            print("Body: Empty")
        else:
            stats = ""
            for stat, val in self.slot_body.properties.items():
                stats += f"- {stat}: {val}\n"
            print(f"Body: {self.slot_body.name}\n{stats}")
        
        if self.slot_feet is None:
            print("Feet: Empty")
        else:
            stats = ""
            for stat, val in self.slot_feet.properties.items():
                stats += f"- {stat}: {val}\n"
            print(f"Feet: {self.slot_feet.name}\n{stats}")

        if self.slot_weapon is None:
            print("Weapon: Empty")
        else:
            stats = ""
            for stat, val in self.slot_weapon.properties.items():
                stats += f"- {stat}: {val}\n"
            print(f"Weapon: {self.slot_weapon.name}\n{stats}")

    def get_stats(self):
        current_stats = {
            "attack": 0,
            "defense": 0
        }
        for item in [self.slot_head, self.slot_body, self.slot_feet, self.slot_weapon]:
            if item is not None:
                current_stats["attack"] += item.properties.get('attack', 0)
                current_stats["defense"] += item.properties.get('def', 0)
        
        for stat, val in current_stats.items():
            print(stat, val)




inv = Inventory()
inv.add_item(Item('hat'))
inv.add_item(Item('basic_sword'))
inv.show_backpack()
inv.equip(1)
inv.show_equipment()
inv.get_stats()
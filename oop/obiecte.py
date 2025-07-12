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

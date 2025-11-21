

def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def input_str(prompt):
    while True:
        try:
            return str(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a Word.")




class Inv():
    def __init__(self):
        self.container = []
        self.weight= 0


    def get_contents(self):
        item=[]
        for i in self.container:
            item.append(i.name)
        return  item


    def get_weight(self):
        return self.weight


        
        
    def add_item(self,item):
        self.container.append(item)
        self.weight+= item.weight
        
        

    def remove_item(self,item):
        self.container.remove(item)
        self.weight -= item["weight"]
    
    def equip_item(self):
        pass


    def unequip_item(self):
        pass

    def use_item(self,item):
        if item.useable==1:
            item.amount-=1
            if item.amount<=0:
                print(f"{item.name} has been removed")
                self.container.remove(item)
                self.weight-=item.weight
        else:
            print("this item can't be used")


class Item():
    def __init__(self, name:str, weight:int, value:int, amount:int, useable:int):
        self.name=name
        self.weight=weight
        self.value=value
        self.amount=amount
        self.useable=useable



    def print_stats(self):
        print("item name: ", self.name)
        print("item weight: ", self.weight)
        print("item value: ", self.value)
        print("item amount: ", self.amount)
    
    def make_item(self):
        self.name=input_str("what is this item called")
        self.weight=input_int(f"how heavy is this {self.name} ")    
        self.value=input_int(f"how valuable is the {self.name}")
        self.amount=input_int(f"how much of this {self.name} do you have")
        self.useable=input_int(f"is this {self.name} usable press [1] for yess or press[0] for nOO ")




player = Inv()


tomato = Item("tomato",10,5,1,1)

lead_thrower=Item("thrower",10,50,1,0)


tomato.print_stats()

player.add_item(tomato)

print(player.get_contents())





player.use_item(tomato)

print(player.get_contents())


print(player.get_weight())


while True :
    
    new_item= Item(None,None,None,None,None)

    new_item.make_item()

    new_item.print_stats()

    player.add_item(new_item)

    print(player.get_contents())  

    if  10 == len(player.get_contents()) :
        break     
    else:
        pass







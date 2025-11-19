

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



def make_item():
        name_item=input_str("what is this item called")
        weight_item=input_int(f"how heavy is this {name_item} ")    
        value_item=input_int(f"how valuable is the {name_item}")
        amount_item=input_int(f"how much of this {name_item} do you have")

        name_item
        return 
        

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



class Item():
    def __init__(self,name,weight,value,amount):
        self.name=name
        self.weight=weight
        self.value=value
        self.amount=amount


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




player = Inv()


tomato = Item("tomato",10,5,1)



tomato.print_stats()



print(player.get_contents())


print(player.get_weight())


while True :
    
    new_item= Item(None,None,None,None)

    new_item.make_item()

    new_item.print_stats()

    player.add_item(new_item)

    print(player.get_contents())  

    if  10 == len(player.get_contents()) :
        break     
    else:
        pass







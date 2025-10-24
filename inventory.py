def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")



class inv():
    def __init__(self):
        self.container = []
        self.weight= 0

    def get_contents(self):
        return self.container

    def get_weight(self):
        return self.weight


        

        

    def add_item(self,item):
        self.container.append(item)
        self.weight += item["weight"]

    def remove_item(self,item):
        self.container.remove(item)
        self.weight -= item["weight"]


class item():
    def __init__(self,name ,weight,value,amount):
        self.name=name
        self.weight=weight
        self.value=value
        self.amount=amount


        

    

    def print_stats(self):
        print("item name: ", self.name)
        print("item weight: ", self.weight)
        print("item value: ", self.value)
        print("item amount: ", self.amount)
        



    

player = inv()

tomato =item(10,5,1)

tomato.new_item()

tomato.print_stats()

player.add_item(tomato)
print(player.get_contents())




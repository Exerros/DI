# class Farm:
#     def __init__(self,name,):
#         self.name = name
#         self.animals={}
        
#     def add_animal(self, animal, count=1):
#         if animal in self.animals:
#             self.animals[animal] += count
#         else:
#             self.animals[animal] = count
    
# cow=Farm("cow")


class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = {}
    
    def add_animal(self, animal, amount=1):
        if animal in self.animals:
            self.animals[animal] += amount
        else:
            self.animals[animal] = amount
            
    def get_info(self):
        result = f"{self.name}'s farm \n \n"
        for animal, amount in self.animals.items():
            result += f"{animal} : {amount}\n"
        result += "\n E-I-E-I-0!"
        return result
            
        
danny=Farm("Danny")
danny.add_animal("dog" , 12)
danny.add_animal("dog" , 3)
danny.add_animal("wolf" , 2)
danny.add_animal("bear" , 1)
danny.add_animal("dragon" , 3)
danny.add_animal("dragon" , 2)

print(danny.get_info())

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
        result += "\n    E-I-E-I-0!"
        return result
    
    def get_animal_types(self):
        animals_name= list(self.animals.keys())
        animals_name.sort()
        return animals_name
    
    def get_short_info(self):
        animals=' '.join(self.get_animal_types())
        return (f"{self.name}'s farm has {animals} ")
            
        
danny=Farm("Danny")
danny.add_animal("dog" , 12)
danny.add_animal("dog" , 3)
danny.add_animal("wolf" , 2)
danny.add_animal("bear")
danny.add_animal("dragon" , 3)
danny.add_animal("dragon" , 2)

print(danny.get_info())
print(danny.get_animal_types())
print(danny.get_short_info())
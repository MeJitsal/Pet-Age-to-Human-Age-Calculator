
import math
class age_calculator: 
    def __init__ (self,pet,name):
        self.pet=pet.lower()
        self.name=name.title()

    def calculate (self, pet_age):
        if self.pet=="cat":
            return round(15.5*(math.pow(pet_age,0.536)),1)
        elif self.pet!="cat":
            print("Please enter 'dog' or 'cat'.")
    
        if self.pet=="dog":
            return round(12.3+(5.09*pet_age)+ (-0.07* math.pow(pet_age,2)))
        
pet_name=input("Enter your pet's name:")
pet_type = input("Enter your pet type:")
pet_age= float(input("Enter your pet's age: (in years)"))
pet_calculator=age_calculator(pet_type,pet_name)
print("Your ",pet_calculator.pet, " named ", pet_calculator.name," is", pet_calculator.calculate(pet_age)," years old in human years.")
if pet_calculator.calculate(pet_age)>60:
    print("Wow, that's pretty old!")
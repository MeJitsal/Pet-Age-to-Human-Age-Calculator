pet_type= input("Enter your pet type:").lower()
pet_age= int(input("Enter your pet's age: (whole numbers only)"))
if pet_type=="dog":
    if pet_age==1:
        print ("Your ", pet_type, " is 15 years old in human years.")
    elif pet_age==2:
        print ("Your ", pet_type, "is 24 years old in human years.")
    elif pet_age >2:
        print("Your ", pet_type, "is ", 24+(pet_age*5), "years old in human years.")
if pet_type=="cat":
    if pet_age==1:
        print ("Your ", pet_type, " is 15 years old in human years.")
    elif pet_age==2:
        print ("Your ", pet_type, "is 24 years old in human years.")
    elif pet_age >2:
        print("Your ", pet_type, "is ", 24+(pet_age*4), "years old in human years.")
        

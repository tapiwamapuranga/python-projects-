from menu import menu
displayMenu=menu()


def makeIngridients(self):
        foodItem=input("Enter the food you want to make")
        numberOfpple=input("Enter the number number of people")
pass


def makeRecipe(self):
        foodItem=input("Enter the food you want to make")
        i=input("how many ingridients do you have ")
        x=0
        while x in range(i):
            #ingridients[x] =input("Enter the available ingridient")
            quantity=input("Enter the quantity of ingridients")
pass


def selectSpecialRecipe():
    choice=displayMenu.specialMenupe()
    if choice==1:
        print("here is your Fried Rice Recipe")
    elif choice==2:
        print("here is your chinese quesh recipe")
    elif choice==3:
        print("here is your Maklaeli recipe")
    elif choice==4:
        print("here is your Papaziana recipe")
    elif choice==5:
        print("here is your Pepe recipe")
    elif choice==6:
        makeIngridients()
    else:
        print("Invalid input ")
        option=input("Do you want to try again [Y/N]")
        if option=='y' or option=='Y':
            selectRecipe()
        else:
            displayMenu.welcomeNote()
pass            


def selectSpecialIngridient():
    choice=displayMenu.specialMenupe()
    if choice==1:
        print("here is your Fried Rice ingridient")
    elif choice==2:
        print("here is your chinese quesh ingridient")
    elif choice==3:
        print("here is your Maklaeli ingridient")
    elif choice==4:
        print("here is your Papaziana ingridients")
    elif choice==5:
        print("here is your Pepe ingridients")
    elif choice==6:
        makeIngridients()
    else:
        print("Invalid input ")
        option=input("Do you want to try again [Y/N]")
        if option=='y' or option=='Y':
            selectRecipe()
        else:
            displayMenu.welcomeNote()
pass            

def selectRecipe():
    choice=displayMenu.availableRecipe()
    if choice==1:
        print("here is your sadza recipe")
    elif choice==2:
        print("here is your recipe")
    elif choice==3:
        print("here is your recipe")
    elif choice==4:
        print("here is your recipe")
    elif choice==5:
        print("here is your recipe")
    elif choice==6:
        makeRecipe()
    else:
        print("Invalid input ")
        option=input("Do you want to try again [Y/N]")
        if option=='y' or option=='Y':
            selectRecipe()
        else:
            displayMenu.welcomeNote()
pass            


def selectIngridients():
    choice=displayMenu.availableIngridients()
    if choice==1:
        print("here is your sadza ingridients")
    elif choice==2:
        print("here is your rice ingridients")
    elif choice==3:
        print("here is your means ingridients")
    elif choice==4:
        print("here is your pease ingridients")
    elif choice==5:
        print("here is your ingridients")
    elif choice==6:
        makeIngridients()
    else:
        print("Invalid input ")
        option=input("Do you want to try again [Y/N]")
        if option.lower=='y':
            selectRecipe()
        else:
            option=input("Do you want a Special Dish [Y/N]")
            if option.lower()=='y':
                selectSpecialIngridient()
            else:
             displayMenu.welcomeNote()
pass





choice=displayMenu.userDetails()
if choice.lower()=="recipe":
    selectRecipe()
elif choice.lower()=="ingridients":
    selectIngridients()
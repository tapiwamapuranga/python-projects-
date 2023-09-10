from codeWizardTask01 import Inventory

inventory = Inventory()

def menu():
    choice=int(input("\t\tMENU\n\t\t1. Add ITEM\n\t\t2. Update Item\n\t\t3. Check Item Details\n\t\t:>"))
    if choice==1:
        count=int(input("How many items do you want to add :"))
        while count>=1:
            itemId=input("Enter the item ID eg:\'I0001\': ")
            itemName=input("Enter the Item Name: ")
            itemQuantity=input("Input the quantity: ")
            price=input("Enter the price: ")
            inventory.add_item(itemId, itemName,itemQuantity,price)
            count-=1
        pass
    elif choice==2:
        itemId=input("Enter the item ID for the product you want to update: ")
        itemQuantity=input("Input the quantity in stock: ")
        price=input("Enter the price: ")
        inventory.update_item(itemId, itemQuantity, price)
    elif choice==3:
        itemId=input("Enter the item ID for the product you want to check: ")
        print(inventory.check_item_details("itemId"))
    else: print("Invalid option")
pass

while True:
    menu()
    option=input("Do you want to perform another action: ")
    if option.lower()=='y':
        menu()
    elif option.lower()=='n':
        print("\t\tThank You!!")
        break
    else: 
        print("\t\tExiting Now...")
        break
pass
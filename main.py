from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu=Menu()
coffee_maker=CoffeeMaker()
money_machine=MoneyMachine()


coffee_names=menu.get_items()
coffee_names_list=coffee_names.split('/')
coffee_names_list.pop()

   
while True:
    user_order = input(f"  What would you like? ({coffee_names}): ").lower()
    
    if menu.find_drink(user_order)!=None:
        menu_item=menu.find_drink(user_order)
        
    if user_order == "off":
        print("The coffee machine is turning off..")
        break
    elif user_order == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_order in coffee_names_list:
        if coffee_maker.is_resource_sufficient(menu_item) and money_machine.make_payment(menu_item.cost):
            coffee_maker.make_coffee(menu_item)  
    else:
        print("Sorry that item is not available.")
    
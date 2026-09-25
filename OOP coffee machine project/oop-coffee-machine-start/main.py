from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
drinks={
    MenuItem("espresso",50,0,18,1.5),
    MenuItem("latte",200,150,24,2.5),
    MenuItem("cappuccino",250,100,24,3.0)
}

rep=CoffeeMaker()
menu=Menu()
profit=MoneyMachine()

machine="run"
while machine=="run":
    choice=input(f"What would you like? ({menu.get_items()}): ")
    if choice=="off":
        machine="stop"
    elif choice == "report":
        rep.report()
        profit.report()
    else:
        drink=menu.find_drink(choice)
        if rep.is_resource_sufficient(drink):
            if profit.make_payment(drink.cost):
                rep.make_coffee(drink)















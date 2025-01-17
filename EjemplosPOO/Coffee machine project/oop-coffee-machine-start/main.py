
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine=MoneyMachine()
coffee_maker=CoffeeMaker() 
menu=Menu()
is_on=True

money_machine.report()
coffee_maker.report()

while is_on:
    options=menu.get_items()
    choice=input(f'¿Qué te gustaría tomar? ({options}):')
    if choice=='off':
        is_on=False
    elif choice=='report':
        coffee_maker.report()
        money_machine.report()
    else: 
        drink=menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)


import streamlit as st
import requests
import pandas as pd
import plotly.express as px

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import streamlit as st

st.title("Máquina de café")
st.write("Disfruta de un café hoy")


# STEP5: Organizamos las entradas y el botón en columnas para evitar desplazamiento vertical
# Ej.: Castellon --> lat = 39.98567, long=-0.04935
col1, col2 = st.columns([1, 1])
with col1:
    choice = st.selectbox('Introduce tu selección', ('expresso', 'late', 'capuccino'))
with col2:
    lon = st.number_input("Introduce el dinero:", value=0.0, format="%.2f", step=0.02)

fetch_button = st.button("Obtén tu café")

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
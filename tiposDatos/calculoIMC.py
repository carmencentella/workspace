#programa que calcula el imc de una persona
peso=float(input('Introduzca su peso en kg: '))
altura=float(input('Ahora introduzca su altura en metros: '))
imc=round(peso/(altura*altura),2)
print(f'Su imc es {imc}')
if(imc<18.5):
    print('Su peso es insuficiente')
elif(18.5<imc<24.9):
    print('Su peso es normal')
elif(25<imc<29.9):
    print('Usted tiene sobrepeso')
else:
    print('Usted tiene obesidad')
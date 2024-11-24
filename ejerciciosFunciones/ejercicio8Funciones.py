def bisiesto(año):
    if año%4==0:
        año='bisiesto'
    else:
        año='no'
    return año
mesescon31=[1,3,5,7,8,10,12]
mesescon30=[4,6,9,11]
def diasdelmes(mes,bisiesto):
    dias=0  
    if mes in mesescon31:
        dias=31
    elif mes==2:
        if 'bisiesto':
            dias=29
        else:
            dias=28
    else:
        dias=30
    return dias
anyo=int(input('Indica un año y te diré los días que han pasado desde el 1 de Enero de este: '))
import datetime
from datetime import datetime
hoy=datetime.now()
diastotales=hoy.day
while anyo<hoy.year:
    anyo+=1
    for i in range(1,13):
        diasmes=diasdelmes(i,bisiesto(anyo))
        diastotales+=diasmes
for i in range (1,hoy.month):
    diastotales+=diasdelmes(i,bisiesto(anyo))
print(f'El día juliano desde el 1 de enero de {anyo} es {diastotales}')


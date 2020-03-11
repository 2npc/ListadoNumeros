#programa hecho por Kevin G y Jon L
#es un programa que te compara los numeros de una lista creada en este mismo archivo.

from Media import med
from MasPeq import pq
from SegundoPeq import segundoPequeño
from ElGrande import M2G
from grande import MG

list=[]
num=(int(input('de cuantos numeros quieres la lista?')))
for i in range(num):
    l=int(input('pon un numero'))
    list.append(l)
    z=1
while z!=0:
    print('*****************************')
    print('*1. el numero más pequeño   *')
    print('*2. el numero más grande    *')
    print('*3. el 2º numero más pequeño*')
    print('*4. el 2º numero más grande *')
    print('*5. sacar media de la lista *')
    print('*0. salir del programa      *')
    print('*****************************')
    z=int(input('elige una opcion: '))

    if(z==1):
        pq(list)
    if(z==2):
        MG(list)
    if (z == 3):
        segundoPequeño(list)
    if (z == 4):
        M2G(list)
    if (z==5):
        med(list)


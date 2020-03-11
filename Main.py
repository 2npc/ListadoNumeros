#programa hecho por Kevin G y Jon L
#es un programa que te compara los numeros de una lista creada en este mismo archivo.
import SegundoPequeño
import MasPequeño



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
    print('*0. salir del programa      *')
    print('*****************************')
    z=int(input('elige una opcion: '))

from fileinput import close
from module import *

#opilased=["Maks","Andr","Art","Den"]
#opilased=["Rebane","Zurko","Popov","Rboinkov"]
#puudumised=[12,42,11,50]
#puudumised=[0,5,104,2]
#puudumised=[666,48,89,1002]

opilased=[]
puudumised=[]
kool(opilased,puudumised)

while True:
    print("\n\n\n")
    print(opilased)
    print(puudumised)
    print()
    menu=int(input('0-Sulge\n1-Top\n2-Sort\n3-Komissioon\n4-Eemaldamine\n5-Dobavlenie\nValige:\n'))
    if menu == 0:
        break
    elif menu == 1:
        top(opilased,puudumised)
    elif menu == 2:
        sort(opilased,puudumised)
    elif menu == 3:
        komiss(opilased,puudumised)
    elif menu == 4:
        eemaldamine(opilased,puudumised)
    elif menu == 5:
        dobavlenie(opilased,puudumised)
    else:
        print("Kirjuta õige arv")
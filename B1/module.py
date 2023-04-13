from math import *

def kool(o:list,p:list):
    """
    """
    while True:
        try:
            a = int(input('Sisestage opilased arv: '))
            break
        except ValueError:
            print("Sisestus peab olema täisarv!")
    for i in range(a):
        nimi = input('Sisestage nimi: ').title()
        puud = int(input('Sisestage puudumised arv: '))
        o.append(nimi)
        p.append(puud)
    return (o,p)


def top(o:list,p:list): 
    """
    """
    topop=int(input("Kui palju topõpilasi soovite näha? "))
    kopia=p.copy()
    for j in range(topop):
        ind=kopia.index(min(kopia))
        print(f"{j+1} inimene - {o[ind]} puudumised: {p[ind]}")
        kopia.pop(ind)
        kopia.insert(ind,max(p)+1)

def sort(o:list,p:list): 
    """
    """
    kopia=p.copy()
    for j in range(len(p)):
        ind=kopia.index(min(kopia))
        print(f"{p[ind]}-{o[ind]}")
        kopia.pop(ind)
        kopia.insert(ind,max(p)+1)

def komiss(o:list,p:list):
    """
    """
    for i in o:
        gfdhbc = o.index(i)
        if p[gfdhbc] >= 50:
            print("------------")
            print(f"Opilane {o[gfdhbc]} mineb komisiooni")
            print("------------")

def eemaldamine(o:list,p:list):
    """
    """
    nimi=(input("Sisesta opilane perenimi: "))
    if nimi in o:
        n=o.count(nimi)
        for j in range(n):
            ind=o.index(nimi)
            if p[ind]>=100:
                o.pop(ind)
                p.pop(ind)
                print("Õpilane oli eemaldatud")
            else:
                print("Sellel õpilasel on liiga vähe puudumiseid!")
                print(o,p)
    else:
        print("Selle nimega õpilast pole!")

def dobavlenie(o:list,p:list):
    """
    """
    uusop = input("Sisestage uus opilane nimi: ")
    o.append(uusop)
    p.append(0)
    print(uusop)
    print(o,p)
    
    

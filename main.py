from random import randrange
print("Lawoulet")
print(" ")
print("Se yon jwèt kote se òdinatè a ki pral chwazi yon nonb nan enteval [0,500] , ou menm wap eseye devine nonb sa.")
print("Ou ap gen 5 chans, pouw jwenn nonb sa ke òdinatè a chwazi a. ")
print(" ")
start = True
while start:
    num_ordinate = randrange(0, 500)
    chans = 5
    while chans > 0:
        num_user = int(input('Antre on nonb :'))
        if num_user == num_ordinate:
            print("Bravo ou genyen !")
            break
        elif num_user > num_ordinate:
            print("nonb ou antre a tro gro antre on pi piti")
            chans -= 1
        elif num_user < num_ordinate:
            print("nonb ou antre a tro piti antre on pi gro")
            chans -= 1
        if chans == 0:
            print(" Ou pedi! ")
            print("Bon nomb lan te", num_ordinate)
            break
        print("Ou rete", chans , "chans")



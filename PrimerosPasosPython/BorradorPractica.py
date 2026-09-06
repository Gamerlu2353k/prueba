import random 
n=0
v=int(input("Añada la vida del jugador: "))
while v>0:
    print(f"tu vida es de: {v}")
    n+=1
    v-=random.randint(1,30)
else:
    print(f"perdistes despues de {n} intentos")
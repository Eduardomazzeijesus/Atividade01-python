import os 

print('''
██████╗░██████╗░░█████╗░░░░░░██╗███████╗████████╗░█████╗░  ██╗███╗░░░███╗██████╗░░█████╗░██████╗░
██╔══██╗██╔══██╗██╔══██╗░░░░░██║██╔════╝╚══██╔══╝██╔══██╗  ██║████╗░████║██╔══██╗██╔══██╗██╔══██╗
██████╔╝██████╔╝██║░░██║░░░░░██║█████╗░░░░░██║░░░██║░░██║  ██║██╔████╔██║██████╔╝███████║██████╔╝
██╔═══╝░██╔══██╗██║░░██║██╗░░██║██╔══╝░░░░░██║░░░██║░░██║  ██║██║╚██╔╝██║██╔═══╝░██╔══██║██╔══██╗
██║░░░░░██║░░██║╚█████╔╝╚█████╔╝███████╗░░░██║░░░╚█████╔╝  ██║██║░╚═╝░██║██║░░░░░██║░░██║██║░░██║
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░╚════╝░╚══════╝░░░╚═╝░░░░╚════╝░  ╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝

███████╗  ██████╗░░█████╗░██████╗░
██╔════╝  ██╔══██╗██╔══██╗██╔══██╗
█████╗░░  ██████╔╝███████║██████╔╝
██╔══╝░░  ██╔═══╝░██╔══██║██╔══██╗
███████╗  ██║░░░░░██║░░██║██║░░██║
╚══════╝  ╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝''')

n1 = int(input("digite o primeiro numero:"))

resto = n1 % 2 

if( resto == 0):
    print("o seu numero é par ")

elif(resto > 0 and n1 >= 1 ):
    print("o seu numero é impar")



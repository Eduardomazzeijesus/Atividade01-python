import os 

print('''
██████╗░██████╗░░█████╗░░░░░░██╗███████╗████████╗░█████╗░
██╔══██╗██╔══██╗██╔══██╗░░░░░██║██╔════╝╚══██╔══╝██╔══██╗
██████╔╝██████╔╝██║░░██║░░░░░██║█████╗░░░░░██║░░░██║░░██║
██╔═══╝░██╔══██╗██║░░██║██╗░░██║██╔══╝░░░░░██║░░░██║░░██║
██║░░░░░██║░░██║╚█████╔╝╚█████╔╝███████╗░░░██║░░░╚█████╔╝
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░╚════╝░╚══════╝░░░╚═╝░░░░╚════╝░

██████╗░░█████╗░░██████╗██╗████████╗██╗██╗░░░██╗░█████╗░  ███████╗
██╔══██╗██╔══██╗██╔════╝██║╚══██╔══╝██║██║░░░██║██╔══██╗  ██╔════╝
██████╔╝██║░░██║╚█████╗░██║░░░██║░░░██║╚██╗░██╔╝██║░░██║  █████╗░░
██╔═══╝░██║░░██║░╚═══██╗██║░░░██║░░░██║░╚████╔╝░██║░░██║  ██╔══╝░░
██║░░░░░╚█████╔╝██████╔╝██║░░░██║░░░██║░░╚██╔╝░░╚█████╔╝  ███████╗
╚═╝░░░░░░╚════╝░╚═════╝░╚═╝░░░╚═╝░░░╚═╝░░░╚═╝░░░░╚════╝░  ╚══════╝

███╗░░██╗███████╗░██████╗░░█████╗░████████╗██╗██╗░░░██╗░█████╗░
████╗░██║██╔════╝██╔════╝░██╔══██╗╚══██╔══╝██║██║░░░██║██╔══██╗
██╔██╗██║█████╗░░██║░░██╗░███████║░░░██║░░░██║╚██╗░██╔╝██║░░██║
██║╚████║██╔══╝░░██║░░╚██╗██╔══██║░░░██║░░░██║░╚████╔╝░██║░░██║
██║░╚███║███████╗╚██████╔╝██║░░██║░░░██║░░░██║░░╚██╔╝░░╚█████╔╝
╚═╝░░╚══╝╚══════╝░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░╚═╝░░░░╚════╝░ ''')

n1 = int(input("digite o numero: "))

os.system("cls")

print("resultado final\n")
print("=========================== \n")
print("o seu numero é", n1)

if(n1 <= 0):
    print("seu numero negativo")

elif(n1 >= 1):
    print("seu numero é positivo")
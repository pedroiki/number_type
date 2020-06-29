# this scrip will read 2 numbers and ask the user , which operation the user wanna do it.

a = float(input("give me one number: "))         #1
b = float(input("choose another number: "))         #2
operação = input("which operation want to do it: \n1- par or impar\n2- para positive or negative\n3- para int or float\n")
ope = int(input("choose a operation: "))       #will get option 1 , 2 and 3 from menu
if ope == 1 or ope == 2 or ope == 3:
    if ope == 1 and a%2 == 0 and b%2 == 0:     #select option 1, with the module of a e b por 2 == 0, pair
        print("pair numbers")
    elif ope == 1 and a%2 == 0 and b%2 != 0:
        print("A é pair e B é impar")
    elif ope == 1 and a%2 != 0 and b%2 == 0:
        print("A é impar e B é pair")
    elif ope == 1 and a%2 != 0 and b%2 != 0:    #select option 1 with the module of a e b por 2 != 0, impar
        print("Impair number")
    elif ope == 2 and a>0 and b>0:              #select operation 2 with a e b bigger than 0, positive
        print("positive number")
    elif ope == 2 and a>0 and b<0:
        print("A é positive e B é negative")
    elif ope == 2 and a<0 and b>0:
        print("A é negative e B é positive")
    elif ope == 2 and a <=0 and b <=0:
        print("Neutral numbers or negative")
    else:
        print(type(a))                           #here will tell positive or negative
        print(type(b))
else:
    print("inválid")

import os

def menu():
    opcion = 'X'
    opciones_posibles = ['1', '2', '3', '4', 'X']
    control = True
    while control: 
        os.system("CLS")
        print("******* MENU *******")
        print("* Opcion 1    -> 1 *")
        print("* Opcion 2    -> 2 *")
        print("* Opcion 3    -> 3 *")
        print("* Opcion 4    -> 4 *")
        print("********************")
        opcion = input("Introduzca su opcion: ")
        if opcion in opciones_posibles:
            control = False
        else:
            print("Opcion invalida")
    return opcion

#PRUEBA UNITARIA
if __name__ == "__main__":
    opc = menu()
    if opc == '1':
        print("UNO")
    else:
        print("Otro")
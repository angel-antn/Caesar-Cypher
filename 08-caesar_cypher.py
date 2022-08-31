import os

alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

#shift=shift%26 => mas facil, aplicacion:

def caesar(text, shift, type="codificada"):
    if type=="decodificada":
        shift*=-1
    new_text=""
    shift=shift%26
    for i in text:
        if i in alphabet:
            pos=alphabet.index(i)
            new_pos=pos+shift
            if new_pos>=len(alphabet):
                new_pos-=len(alphabet)
            new_text+=alphabet[new_pos]
        else:
            new_text+=i
    print(f"Tu palabra {type}: "+new_text)
    
#codigo original
# def codificar(text, shift):
#     new_text=""
#     for i in text:
#         if i in alphabet:
#             pos=alphabet.index(i)
#             new_pos=pos+shift
#             while new_pos>len(alphabet)-1:
#                 new_pos-=len(alphabet)
#             new_text+=alphabet[new_pos]
#         else:
#             new_text+=i
#     print("Tu palabra encriptada: "+new_text)

# def decodificar(text, shift):
#     new_text=""
#     for i in text:
#         if i in alphabet:
#             pos=alphabet.index(i)
#             new_pos=pos-shift
#             while new_pos<0:
#                 new_pos+=len(alphabet)
#             new_text+=alphabet[new_pos]
#         else:
#             new_text+=i
#     print("Tu palabra desencriptada: "+new_text)

def salir():
    validar=True
    while validar:
        os.system("cls")
        print(logo+'\n')
        print("Desea seguir utilizando el programa?:\n1-si\n2-no")  
        o=input("=>")
        if o=="1":
            return False
        elif o=="2":
            return True
        else:
            print("Su respuesta no pudo ser procesada...")
            input("Presione cualquier tecla para continuar...")

stop=False
while not stop:
    validar=True
    while validar:
        os.system("cls")
        print(logo+'\n')
        print("Indique que desea hacer:\n1-Codificar\n2-Decodificar")  
        o=input("=>")
        if(o!="1" and o!="2"):
            print("Su respuesta no pudo ser procesada...")
            input("Presione cualquier tecla para continuar...")
        else:
            validar=False
    if o=="1":
        validar=True
        while validar:
            validar=False
            os.system("cls")
            print(logo+'\n')
            text=input("ingrese la palabra que desea codificar: ").lower()
            try:
                shift=int(input("Ingrese el numero para codificar el texto: "))
            except ValueError:
                print("Su respuesta no pudo ser procesada...")
                input("Presione cualquier tecla para continuar...")
                validar=True
        caesar(text, shift)
    else:
        validar=True
        while validar:
            validar=False
            os.system("cls")
            print(logo+'\n')
            text=input("ingrese la palabra que desea decodificar: ").lower()
            try:
                shift=int(input("Ingrese el numero para decodificar el texto: "))
            except ValueError:
                print("Su respuesta no pudo ser procesada...")
                input("Presione cualquier tecla para continuar...")
                validar=True
        caesar(text, shift, "decodificada")
    input("Presione cualquier tecla para continuar...")
    stop=salir()
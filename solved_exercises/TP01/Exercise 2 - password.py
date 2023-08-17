"""
Exercise 2:
    
Haga un programa que pregunte: Nombre, fecha de nacimiento y DNI y los combine 
de manera elegante para obtener posibles passwords de HomeBanking u otras 
aplicaciones. (recuerde que usualmente la clave debe ser de 8 caracteres, 
al menos 2 letras, al menos 2 números, y no puede contener fragmentos de la 
fecha de nacimiento, nombre o DNI). Consejo: use el orden del alfabeto y/o el 
pad númerico de celulares viejos para interconvertir números-letras 
(piense que un string no es otra cosa que una cadena (lista?) de caracteres
individuales.
    
"""
import random

# Generates alphabet in lower case
alphabet = list(map(chr, [*range(97, 123)]))

numeric_pad = {'a': '2', 'b': '2', 'c': '2', 'd': '3', 'e': '3', 'f': '3', 'g': '4',
              'h': '4', 'i': '4', 'j': '5', 'k': '5', 'l': '5', 'm': '6', 'n': '6',
              'o': '6', 'p': '7', 'q': '7', 'r': '7', 's': '7', 't': '8', 'u': '8',
              'v': '8', 'w': '9', 'x': '9', 'y': '9', 'z': '9'}



def pwd_gen(name, birthdate, dni):
    '''
    Function that selects 2 random chars from name, 2 random nrs from birthdate
    and 2 random numbers from dni.
    Then transforms nrs to letters using alphabet and chars to numbers using 
    the numeric pad.
    Finally it shuffles the 8 elements of the list and joins them in a string

    Returns: A string with 8 elements
    '''
    random_sel = random.choices(name.lower(), k=2) + random.choices(birthdate, k=3) + random.choices(dni, k=3)

    pwd = []
    for item in random_sel:
        if item.isdigit():
            item = alphabet[int(item)]
            pwd.append(item)
        else:
            item = numeric_pad[item]
            pwd.append(item)
    
    random.shuffle(pwd)    
    pwd = ''.join(pwd)
    return pwd
    
#%%

name = input("Enter your name: ")
birthdate = input("Enter your birthdate (ddmmyyyy): ")
dni = input("Enter yout ID number: ")

password = pwd_gen(name, birthdate, dni)

print(f'Your password is :{password}')





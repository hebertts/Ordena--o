import random
import os
from prettytable import PrettyTable
import sort

import names


def Menu():
    choice = 0
    os.system('cls')
    print('+'+'-'*51+'+')
    print('|                     Menu Principal                |')
    print('+'+'-'*51+'+')
    menu_principal = PrettyTable(['      OPÇÃO      ', '       ITEM     '])
    menu_principal.align['OPÇÃO'] = 'c'
    menu_principal.align['ITEM'] ='l'
    menu_principal.add_row(['1','números aleatóios crescente'])
    menu_principal.add_row(['2','números aleatóios decrescente'])
    menu_principal.add_row(['3','Seus números crescente'])
    menu_principal.add_row(['4','Seus números decrescente'])
    menu_principal.add_row(['5','Seus nomes Crescente'])
    menu_principal.add_row(['6','Seus nomes descrescente'])
    menu_principal.add_row(['7','Nomes aletórios crescente'])
    menu_principal.add_row(['8','Nomes aletórios decrescente'])
    print(menu_principal)
    print('+'+'-'*51+'+')
    
    choice = int(input('Escolha: '))
    if choice == 7:
        arr_str = []
        for _ in range(5):
            arr_str.append(names.get_full_name())
        print_decorated_list('Lista',arr_str,choice)
        print('\n')   
        sort.ascending_order(arr_str)
        print_decorated_list('Decrescente',arr_str,choice)
    if choice == 8:
        arr_str = []
        for _ in range(5):
            arr_str.append(names.get_full_name())
        print_decorated_list('Lista',arr_str,choice)
        print('\n')
        sort.descending_order(arr_str)
        print_decorated_list('Decrescente',arr_str,choice)
    if choice == 1:
        arr = list(range(5,20))
        random.shuffle(arr)
        print_decorated_list('Lista',arr,choice)
        print('\n')
        sort.ascending_order(arr)
        print_decorated_list('Crescente',arr,choice)
    if choice == 2:
        arr = list(range(5,10))
        random.shuffle(arr)
        print_decorated_list('Lista',arr,choice)
        print('\n')
        sort.descending_order(arr)
        print_decorated_list('Decrescente',arr,choice)
    if choice == 3:
        arr = list(map(int,input("Digite seus números separados por vírgula: ").split(',')))
        print_decorated_list('Lista',arr,choice)
        print('\n')
        sort.ascending_order(arr)
        print_decorated_list('Crescente',arr,choice)
    if choice == 4:
        arr = list(map(int,input("Digite seus números separados por vírgula: ").split(',')))
        print_decorated_list('Lista',arr,choice)
        print('\n')
        sort.descending_order(arr)
        print_decorated_list('Decrescente',arr,choice)
    if choice == 5:
        arr = list(map(str,input("Digite nomes separados por vírgula: ").split(',')))
        print_decorated_list('Lista',arr,choice)
        print('\n')
        sort.ascending_order(arr)
        print_decorated_list('Crescente',arr,choice)
    if choice == 6:
        arr = list(map(str,input("Digite nomes separados por vírgula: ").split(',')))
        print_decorated_list('Lista',arr,choice)
        print('\n')
        sort.descending_order(arr)
        print_decorated_list('decrescente',arr,choice)
def print_decorated_list(title, ordered_list,choice):
    if 5 <= choice <= 8:
        count = len(ordered_list)*16
    else:
        count = len(ordered_list)*4
    print("+" + "-" * count + "+")
    print(f"|{title.center(count)}|")
    print("+" + "-" * count + "+")
    print("|" + "-".join(map(str, (ordered_list))).center(count) + "|")
    print("+" + "-" * count + "+")

    

Menu()
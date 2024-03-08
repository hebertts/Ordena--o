import random
import os
from prettytable import PrettyTable
import Testes.sort as sort

import names


def Menu():
    choice = 0
    os.system('cls')
    print('+'+'-'*52+'+')
    print('|                     Menu Principal                 |')
    print('+'+'-'*52+'+')
    menu_principal = PrettyTable(['      OPÇÃO      ', '       ITEM     '])
    menu_principal.align['OPÇÃO'] = 'c'
    menu_principal.align['ITEM'] ='l'
    menu_principal.add_row(['1','Números aleatórios crescente'])
    menu_principal.add_row(['2','Números aleatórios decrescente'])
    menu_principal.add_row(['3','Seus números crescente'])
    menu_principal.add_row(['4','Seus números decrescente'])
    menu_principal.add_row(['5','Seus nomes crescente'])
    menu_principal.add_row(['6','Seus nomes descrescente'])
    menu_principal.add_row(['7','Nomes aleatórios crescente'])
    menu_principal.add_row(['8','Nomes aleatórios decrescente'])
    print(menu_principal)
    
    
    choice = int(input('Escolha: '))
    if choice == 7:
        arr_str = []
        number_max = int(input('Digite a quantidade máxima desejada: '))
        for _ in range(number_max):
            arr_str.append(names.get_full_name())
        print(f'Sua lista contém {number_max} nomes aleatórios')
        print('\n')   
        sort.ascending_order(arr_str)
        print_decorated_list('Crescente',arr_str)
    if choice == 8:
        arr_str = []
        number_max = int(input('Digite a quantidade máxima desejada: '))
        for _ in range(number_max):
            arr_str.append(names.get_full_name())
        print(f'Sua lista contém {number_max} nomes aleatórios')
        print('\n')
        sort.descending_order(arr_str)
        print_decorated_list('Decrescente',arr_str)
    if choice == 1:
        number_max = int(input('Digite a quantidade máxima desejada: '))
        arr = list(range(1,number_max+1))
        random.shuffle(arr)
        print(f'Sua lista: vai de 1 a {number_max} aleatoriamente: ')
        print('\n')
        sort.ascending_order(arr)
        print_decorated_list('Crescente',arr)
    if choice == 2:
        number_max = int(input('Digite a quantidade máxima desejada: '))
        arr = list(range(1,number_max+1))
        random.shuffle(arr)
        print(f'Sua lista: vai de 1 a {number_max} aleatoriamente: ')
        print('\n')
        sort.descending_order(arr)
        print_decorated_list('Decrescente',arr)
    if choice == 3:
        arr = list(map(int,input("Digite seus números separados por vírgula: ").split(',')))
        print(f'Sua lista: '+', '.join(map(str, arr)))
        print('\n')
        sort.ascending_order(arr)
        print_decorated_list('Crescente',arr)
    if choice == 4:
        arr = list(map(int,input("Digite seus números separados por vírgula: ").split(',')))
        print(f'Sua lista ordenada:')
        print('\n')
        sort.descending_order(arr)
        print_decorated_list('Decrescente',arr)
    if choice == 5:
        arr = list(map(str,input("Digite nomes separados por vírgula: ").split(',')))
        print(f'Sua lista ordenada:')
        print('\n')
        sort.ascending_order(arr)
        print_decorated_list('Crescente',arr)
    if choice == 6:
        arr = list(map(str,input("Digite nomes separados por vírgula: ").split(',')))
        print(f'Sua lista ordenada:')
        print('\n')
        sort.descending_order(arr)
        print_decorated_list('decrescente',arr)
from prettytable import PrettyTable

def print_decorated_list(title, ordered_list):
    max_length = max(len(str(item)) for item in ordered_list) + 4
    num_columns = 7  # Número de colunas desejado

    table = PrettyTable()
    table.field_names = [f"Column {i}" for i in range(1, num_columns + 1)]
    for i in range(0, len(ordered_list), num_columns):
        row = ordered_list[i:i + num_columns]
        if len(row) < num_columns:
            row.extend([''] * (num_columns - len(row)))
        table.add_row(row)
   
    print(f'Lista ordenada {title}: ')
    print(table)


    

Menu()
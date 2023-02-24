# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 23:38:28 2023

@author: DIANA ZAMBRANO Y ANDRES FLORES
"""

import json

data_ferreteria = []

products = [
    {'nombre':'bombillo',
     'precio':'2 usd',
     'descripcion':'tipo led'
     },
    {'nombre':'adhesivo',
     'precio':'1 usd',
     'descripcion':'size 1in'
     },
]

data_base = data_ferreteria.append(products)

with open('data_ferreteria.json','w') as file:
    json.dump(data_ferreteria, file)
    
with open('data_ferreteria.json','r') as file:
    data_ferreteria = json.load(file)

content_data = {'nombre': '', 'precio':'', 'descripcion':''}

print('Bienvenido a tu ferreteria online.')

options = int(input('Usuario ingrese: \n1 ---> Si desea ver el catalogo original. \n2 ---> Si desea añadir un producto.'))


if options == 1 :
    
    print(data_ferreteria)
            
elif options == 2 :
    number_art = int(input('Indique cuantos articulos desea añadir:'))
    for i in range(number_art):
        content_data = {}
        nombre = input('Usuario ingrese el nombre del articulo: ')
        precio = input('Usuario ingrese el costo del articulo: ')
        descripcion = input('Usuario ingrese el tipo de articulo: ')
        content_data['nombre'] = nombre
        content_data['precio'] = precio
        content_data['descripcion'] = descripcion

        data_ferreteria.append(content_data)
    
        with open('data_ferreteria.json', 'w+') as file:
            json.dump(data_ferreteria,file)


else :
    print('Ha cometido un error.')
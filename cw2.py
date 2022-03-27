dodaj15 = lambda x: x + 15
pomnóżxy = lambda x, y: x * y

# print (pomnóżxy(5,5))
# print (dodaj15(15))

lista = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
         {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]


def myFunc(e):
    return e['model']


posortuj = lambda lista: lista.sort(key=myFunc)
# posortuj(lista)


# for item in lista:
#    print(item)

lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

potega2 = list(map(lambda x: pow(x, 2), lista2))
for item in potega2:
    print(item)
potega3 = list(map(lambda x: pow(x, 3), lista2))
for item in potega3:
    print(item)

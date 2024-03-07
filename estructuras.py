#Se declaran diccionarios= objetos

clienteUno = {
    "id":5,
    "nombre":"edif1",
    "consumo": 200
}


clienteDos = {
    "id":55,
    "nombre":"edif15",
    "consumo": 2003
}

#se declara una lista = arreglo

clientesAsociadas = [
    clienteUno,clienteDos
]

# y ahora que hago con esa lista 
#objetivo sera obtener la informacion de la lista
#recorrer una lista o arreglo 

'''for i in range (2):
    print(clientesAsociadas[i]["consumo"])'''

#programemos un foreach que es un for
# especializado en recorre arreglos (listas)
for cliente in clientesAsociadas:
    print(cliente["id"],'-->',cliente["consumo"],'Kwh')
    print(f"{cliente["id"]}-->{cliente['consumo']}Kwh")

# id ---> consumo 
# 5 ----> 200 kwh
    

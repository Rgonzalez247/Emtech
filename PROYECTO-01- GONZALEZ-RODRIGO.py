from lifestore_file import lifestore_products
from lifestore_file import lifestore_sales
from lifestore_file import lifestore_searches

intentos = 0
contraseñas = [123, 456, "hola", 879, 980]
contraseñaR = "123"
usuarios = "Rgonzalez"

#input para iniciar sesión, se utiliza la función for e if para poder arrojar mensajes de error en caso de que esté equivocasdo. la variable intentas va incrementando de acuerdo al número de veces que se intente ingresar con contraseña incorrecta.

# Escribir Usuario: Rgonzalez
# Escribir Contraseña: 123
print('Inicio de sesion')
for usuario in usuarios:
    usuario = input('Usuario: ')
    if usuario != usuarios:
        print("Usuario no reconocido")
    else:
        break
for contraseña in contraseñas:
    contraseña = input('Contraseña: ')
    if contraseña != contraseñaR:
        intentos += 1
        print("Intenta de nuevo")
        print("Número de intentos: " + str(intentos))
    else:
        print("")
        print("¡Bienvenido de vuelta!")
    break

print("")
print("")
print("Parte 1")
print("")
#Unidades Vendidas
prod1 = 0
prod2 = 0
prod3 = 0
prod4 = 0
prod5 = 0
prod6 = 0
prod7 = 0
prod8 = 0
prod10 = 0
prod11 = 0
prod12 = 0
prod13 = 0
prod17 = 0
prod18 = 0
prod21 = 0
prod22 = 0
prod25 = 0
prod28 = 0
prod29 = 0
prod31 = 0
prod33 = 0
prod40 = 0
prod42 = 0
prod44 = 0
prod45 = 0
prod46 = 0
prod47 = 0
prod48 = 0
prod49 = 0
prod50 = 0
prod51 = 0
prod52 = 0
prod54 = 0
prod57 = 0
prod60 = 0
prod66 = 0
prod67 = 0
prod74 = 0
prod84 = 0
prod85 = 0
prod89 = 0
prod94 = 0

num1 = 0

#Loop para sumar cuantas veces se vendió cada artículo
for ventas in lifestore_sales:
    if lifestore_sales[num1][1] == 1:
        prod1 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 2:
        prod2 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 3:
        prod3 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 4:
        prod4 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 5:
        prod5 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 6:
        prod6 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 7:
        prod7 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 8:
        prod8 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 10:
        prod10 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 11:
        prod11 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 12:
        prod12 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 13:
        prod13 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 17:
        prod17 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 18:
        prod18 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 21:
        prod21 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 22:
        prod22 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 25:
        prod25 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 28:
        prod28 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 29:
        prod29 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 31:
        prod31 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 33:
        prod33 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 40:
        prod40 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 42:
        prod42 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 44:
        prod44 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 45:
        prod45 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 46:
        prod46 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 47:
        prod47 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 48:
        prod48 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 49:
        prod49 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 50:
        prod50 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 51:
        prod51 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 52:
        prod52 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 54:
        prod54 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 57:
        prod57 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 60:
        prod60 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 66:
        prod66 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 67:
        prod67 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 74:
        prod74 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 84:
        prod84 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 85:
        prod85 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 89:
        prod89 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 94:
        prod94 += 1
        num1 += 1
        continue
        break

sales = [prod1, prod2, prod3, prod4, prod5, prod6, prod7, prod8, prod10, prod11, prod12, prod13, 0, 0, 0, prod17, prod18, 0, 0, prod21, prod22, 0, 0, prod25, 0,0, prod28, prod29, 0, prod31, 0, prod33, 0, 0, 0, 0, 0, 0, prod40, 0, prod42, 0, prod44, prod45, prod46, prod47, prod48, prod49, prod50, prod51, prod52, 0, prod54, 0, 0, prod57, 0, 0, prod60, 0, 0, 0, 0, 0, prod66, prod67, 0, 0, 0, 0, 0, 0, prod74, 0, 0, 0, 0, 0, 0, 0, 0, 0,prod84, prod85, 0, 0, 0, prod89, 0, 0, 0, 0, prod94]

#sales.sort(reverse=True)
sales2 = [['Producto 1', prod1], ['Producto 2', prod2], ['Producto 3', prod3],
          ['Proucto 4', prod4], ['Producto 5', prod5], ['Producto 6', prod6],
          ['Producto 7', prod7], ['Producto 8', prod8],
          ['Producto 10', prod10], ['Producto 11', prod11],
          ['Producto 12', prod12], ['Producto 13', prod13],
          ['Producto 17', prod17], ['Producto 18', prod18],
          ['Producto 21', prod21], ['Producto 22', prod22],
          ['Producto 25', prod25], ['Producto 28', prod28],
          ['Producto 29', prod29], ['Producto 31', prod31],
          ['Producto 33', prod33], ['Producto 40', prod40],
          ['Producto 42', prod42], ['Producto 44', prod44],
          ['Producto 45', prod45], ['Producto 46', prod46],
          ['Producto 47', prod47], ['Producto 48', prod48],
          ['Producto 49', prod49], ['Producto 50', prod50],
          ['Producto 51', prod51], ['Producto 52', prod52],
          ['Producto 54', prod54], ['Producto 57', prod57],
          ['Producto 60', prod60], ['Producto 66', prod66],
          ['Producto 67', prod67], ['Producto 74', prod74],
          ['Producto 84', prod84], ['Producto 85', prod85],
          ['Producto 89', prod89], ['Producto 94', prod94]]

#definir el valor "segundo"
def segundo(elem):
    return elem[1]

print("")
print("Resultado 1.1.1")
#ordenar tomando en cuenta el segundo elemento
sales2.sort(key=segundo, reverse=True)
print("Lista de Productos con sus Respectivas Cantidades Vendidas de Mayor a Menor:")
print("")
print(sales2[:5])

print("")
print("Resultado 1.2.1")
num2 = 0
categorias = []

for categoria in lifestore_products:
  if lifestore_products[num2][0] <97:
    cat = lifestore_products[num2][3]
    categorias.append(cat)
    num2 += 1
  else:
    break
categorias = list(dict.fromkeys(categorias))

sales2.sort(key=segundo)
print("Lista de Categorías con sus Respectivas Cantidades Vendidas de Menor a Mayor:")
print("")

num2 = 0
num3 = 1
for producto in lifestore_products:
  if lifestore_products[num2][0] == num3:
    lifestore_products[num2].append(sales[num2])
    num3 += 1
  elif num2 <= 96:
    num2 += 1

print('Programa no tiene suficiente capacidad como para correr todo el código, se queda atorado a la mitad de la corrida')

num4 = 0
num5 = 0
print(categorias[num5])
for producto in lifestore_products:
  if lifestore_products[num4][3] == categorias[num5] and lifestore_products[num4][0] < 49:
    print('Producto '+ str(lifestore_products[num4][0])+" / Vendidos: "+ str(lifestore_products[num4][5]))
    num4 += 1
  elif num5 <= 1 and lifestore_products[num4][0] < 49:
    num5 += 1
    print(categorias[num5])
  elif num5 <= 8 and lifestore_products[num4][0] < 49:
    print(categorias[num5])
    num5 += 1
  else:
    break

print('Se pone limitante a 49 porque programa no tiene capacidad de correr más lineas')

#Busquedas
prod1 = 0
prod2 = 0
prod3 = 0
prod4 = 0
prod5 = 0
prod6 = 0
prod7 = 0
prod8 = 0
prod9 = 0
prod10 = 0
prod11 = 0
prod12 = 0
prod13 = 0
prod15 = 0
prod17 = 0
prod18 = 0
prod21 = 0
prod22 = 0
prod25 = 0
prod26 = 0
prod27 = 0
prod28 = 0
prod29 = 0
prod31 = 0
prod33 = 0
prod35 = 0
prod39 = 0
prod40 = 0
prod42 = 0
prod44 = 0
prod45 = 0
prod46 = 0
prod47 = 0
prod48 = 0
prod49 = 0
prod50 = 0
prod51 = 0
prod52 = 0
prod54 = 0
prod56 = 0
prod57 = 0
prod59 = 0
prod60 = 0
prod63 = 0
prod66 = 0
prod67 = 0
prod70 = 0
prod73 = 0
prod74 = 0
prod76 = 0
prod80 = 0
prod84 = 0
prod85 = 0
prod89 = 0
prod91 = 0
prod93 = 0
prod94 = 0
prod95 = 0

num1 = 0

#Loop para sumar cuantas veces se buscó cada artículo
for busquedas in lifestore_searches:
    if lifestore_searches[num1][1] == 1:
        prod1 += 1
        num1 += 1
        continue
    elif lifestore_searches[num1][1] == 2:
        prod2 += 1
        num1 += 1
        continue
    elif lifestore_searches[num1][1] == 3:
        prod3 += 1
        num1 += 1
        continue
    elif lifestore_searches[num1][1] == 4:
        prod4 += 1
        num1 += 1
        continue
    elif lifestore_searches[num1][1] == 5:
        prod5 += 1
        num1 += 1
        continue
    elif lifestore_searches[num1][1] == 6:
        prod6 += 1
        num1 += 1
        continue
    elif lifestore_searches[num1][1] == 7:
        prod7 += 1
        num1 += 1
        continue
    elif lifestore_searches[num1][1] == 8:
        prod8 += 1
        num1 += 1
        continue
    elif lifestore_searches[num1][1] == 9:
        prod9 += 1
        num1 += 1
        continue
    elif lifestore_searches[num1][1] == 10:
        prod10 += 1
        num1 += 1
        continue
    elif lifestore_searches[num1][1] == 11:
        prod11 += 1
        num1 += 1
        continue
    elif lifestore_searches[num1][1] == 12:
        prod12 += 1
        num1 += 1
        continue
    elif lifestore_searches[num1][1] == 13:
        prod13 += 1
        num1 += 1
        continue
    elif lifestore_searches[num1][1] == 15:
        prod15 += 1
        num1 += 1
        continue
    elif lifestore_searches[num1][1] == 17:
        prod17 += 1
        num1 += 1
        continue
    elif lifestore_searches[num1][1] == 18:
        prod18 += 1
        num1 += 1
        continue
    elif lifestore_searches[num1][1] == 21:
        prod21 += 1
        num1 += 1
        continue
    elif lifestore_searches[num1][1] == 22:
        prod22 += 1
        num1 += 1
        continue
    elif lifestore_searches[num1][1] == 25:
        prod25 += 1
        num1 += 1
        continue
    elif lifestore_searches[num1][1] == 26:
        prod26 += 1
        num1 += 1
        continue
    elif lifestore_searches[num1][1] == 27:
        prod27 += 1
        num1 += 1
        continue
    elif lifestore_searches[num1][1] == 28:
        prod28 += 1
        num1 += 1
        continue
    elif lifestore_searches[num1][1] == 29:
        prod29 += 1
        num1 += 1
        continue
    elif lifestore_searches[num1][1] == 31:
        prod31 += 1
        num1 += 1
        continue
    elif lifestore_searches[num1][1] == 33:
        prod33 += 1
        num1 += 1
        continue
    elif lifestore_searches[num1][1] == 35:
        prod35 += 1
        num1 += 1
        continue
    elif lifestore_searches[num1][1] == 39:
        prod39 += 1
        num1 += 1
        continue
    elif lifestore_searches[num1][1] == 40:
        prod40 += 1
        num1 += 1
        continue
    elif lifestore_searches[num1][1] == 42:
        prod42 += 1
        num1 += 1
        continue
    elif lifestore_searches[num1][1] == 44:
        prod44 += 1
        num1 += 1
        continue
    elif lifestore_searches[num1][1] == 45:
        prod45 += 1
        num1 += 1
        continue
    elif lifestore_searches[num1][1] == 46:
        prod46 += 1
        num1 += 1
        continue
    elif lifestore_searches[num1][1] == 47:
        prod47 += 1
        num1 += 1
        continue
    elif lifestore_searches[num1][1] == 48:
        prod48 += 1
        num1 += 1
        continue
    elif lifestore_searches[num1][1] == 49:
        prod49 += 1
        num1 += 1
        continue
    elif lifestore_searches[num1][1] == 50:
        prod50 += 1
        num1 += 1
        continue
    elif lifestore_searches[num1][1] == 51:
        prod51 += 1
        num1 += 1
        continue
    elif lifestore_searches[num1][1] == 52:
        prod52 += 1
        num1 += 1
        continue
    elif lifestore_searches[num1][1] == 54:
        prod54 += 1
        num1 += 1
        continue
    elif lifestore_searches[num1][1] == 56:
        prod56 += 1
        num1 += 1
        continue
    elif lifestore_searches[num1][1] == 57:
        prod57 += 1
        num1 += 1
        continue
    elif lifestore_searches[num1][1] == 59:
        prod59 += 1
        num1 += 1
        continue
    elif lifestore_searches[num1][1] == 60:
        prod60 += 1
        num1 += 1
        continue
    elif lifestore_searches[num1][1] == 63:
        prod63 += 1
        num1 += 1
        continue
    elif lifestore_searches[num1][1] == 66:
        prod66 += 1
        num1 += 1
        continue
    elif lifestore_searches[num1][1] == 67:
        prod67 += 1
        num1 += 1
        continue
    elif lifestore_searches[num1][1] == 70:
        prod70 += 1
        num1 += 1
        continue
    elif lifestore_searches[num1][1] == 73:
        prod73 += 1
        num1 += 1
        continue
    elif lifestore_searches[num1][1] == 74:
        prod74 += 1
        num1 += 1
        continue
    elif lifestore_searches[num1][1] == 76:
        prod76 += 1
        num1 += 1
        continue
    elif lifestore_searches[num1][1] == 80:
        prod80 += 1
        num1 += 1
        continue
    elif lifestore_searches[num1][1] == 84:
        prod84 += 1
        num1 += 1
        continue
    elif lifestore_searches[num1][1] == 85:
        prod85 += 1
        num1 += 1
        continue
    elif lifestore_searches[num1][1] == 89:
        prod89 += 1
        num1 += 1
        continue
    elif lifestore_searches[num1][1] == 91:
        prod91 += 1
        num1 += 1
        continue
    elif lifestore_searches[num1][1] == 93:
        prod93 += 1
        num1 += 1
        continue
    elif lifestore_searches[num1][1] == 94:
        prod94 += 1
        num1 += 1
        continue
    elif lifestore_searches[num1][1] == 95:
        prod95 += 1
        num1 += 1
        continue
        break
print("")

busquedas = [prod1, prod2, prod3, prod4, prod5, prod6, prod7,prod8, prod9, prod10, prod11, prod12, prod13, prod15, prod17,prod18, prod21, prod22, prod25, prod26, prod27, prod28, prod29, prod31, prod33, prod35, prod39, prod40, prod42, prod44, prod45, prod46, prod47, prod48, prod49, prod50, prod51, prod52, prod54, prod56, prod57, prod59, prod60, prod63, prod66, prod67, prod70, prod73, prod74, prod80, prod84, prod85, prod89, prod91, prod93, prod94, prod95]

busquedas.sort(reverse=True)

busquedas2 = [['Producto 1', prod1], ['Producto 2', prod2], ['Producto 3', prod3],
          ['Proucto 4', prod4], ['Producto 5', prod5], ['Producto 6', prod6],
          ['Producto 7', prod7], ['Producto 8', prod8], ['Producto 9', prod9],
          ['Producto 10', prod10], ['Producto 11', prod11],
          ['Producto 12', prod12], ['Producto 13', prod13],
          ['Producto 15', prod15],
          ['Producto 17', prod17], ['Producto 18', prod18],
          ['Producto 21', prod21], ['Producto 22', prod22],
          ['Producto 25', prod25], ['Producto 26', prod26], ['Producto 27', prod27], ['Producto 28', prod28],
          ['Producto 29', prod29], ['Producto 31', prod31],
          ['Producto 33', prod33], ['Producto 35', prod35], ['Producto 39', prod39], ['Producto 40', prod40],
          ['Producto 42', prod42], ['Producto 44', prod44],
          ['Producto 45', prod45], ['Producto 46', prod46],
          ['Producto 47', prod47], ['Producto 48', prod48],
          ['Producto 49', prod49], ['Producto 50', prod50],
          ['Producto 51', prod51], ['Producto 52', prod52],
          ['Producto 54', prod54], ['Producto 56', prod56], ['Producto 57', prod57], ['Producto 59', prod59],
          ['Producto 60', prod60], ['Producto 63', prod63], ['Producto 66', prod66],
          ['Producto 67', prod67], ['Producto 70', prod70], ['Producto 73', prod73], ['Producto 74', prod74], ['Producto 80', prod80], 
          ['Producto 84', prod84], ['Producto 85', prod85],
          ['Producto 89', prod89], ['Producto 91', prod91], ['Producto 93', prod93], ['Producto 94', prod94], ['Producto 95', prod95]
          ]

def segundo(elem):
    return elem[1]

print("")
print("Resultado 1.1.2")
busquedas2.sort(key=segundo, reverse=True)
print("Lista de Productos con sus Respectivas Cantidades de Busquedas de Mayor a Menor:")
print("")
print(busquedas2[:10])

print("")
print("")
print("Parte 2")
print("")

#Unidades Vendidas
prod1 = 0
prod2 = 0
prod3 = 0
prod4 = 0
prod5 = 0
prod6 = 0
prod7 = 0
prod8 = 0
prod10 = 0
prod11 = 0
prod12 = 0
prod13 = 0
prod17 = 0
prod18 = 0
prod21 = 0
prod22 = 0
prod25 = 0
prod28 = 0
prod29 = 0
prod31 = 0
prod33 = 0
prod40 = 0
prod42 = 0
prod44 = 0
prod45 = 0
prod46 = 0
prod47 = 0
prod48 = 0
prod49 = 0
prod50 = 0
prod51 = 0
prod52 = 0
prod54 = 0
prod57 = 0
prod60 = 0
prod66 = 0
prod67 = 0
prod74 = 0
prod84 = 0
prod85 = 0
prod89 = 0
prod94 = 0

num1 = 0
#Loop para sumar cuantas veces se vendió cada artículo
for devoluciones in lifestore_sales:
  if lifestore_sales[num1][4] == 1:
    if lifestore_sales[num1][1] == 1:
      prod1 += 1
      num1 += 1
      continue
    elif lifestore_sales[num1][1] == 2:
      prod2 += 1
      num1 += 1
      continue
    elif lifestore_sales[num1][1] == 3:
      prod3 += 1
      num1 += 1
      continue
    elif lifestore_sales[num1][1] == 4:
      prod4 += 1
      num1 += 1
      continue
    elif lifestore_sales[num1][1] == 5:
      prod5 += 1
      num1 += 1
      continue
    elif lifestore_sales[num1][1] == 6:
      prod6 += 1
      num1 += 1
      continue
    elif lifestore_sales[num1][1] == 7:
      prod7 += 1
      num1 += 1
      continue
    elif lifestore_sales[num1][1] == 8:
      prod8 += 1
      num1 += 1
      continue
    elif lifestore_sales[num1][1] == 10:
      prod10 += 1
      num1 += 1
      continue
    elif lifestore_sales[num1][1] == 11:
      prod11 += 1
      num1 += 1
      continue
    elif lifestore_sales[num1][1] == 12:
      prod12 += 1
      num1 += 1
      continue
    elif lifestore_sales[num1][1] == 13:
      prod13 += 1
      num1 += 1
      continue
    elif lifestore_sales[num1][1] == 17:
      prod17 += 1
      num1 += 1
      continue
    elif lifestore_sales[num1][1] == 18:
      prod18 += 1
      num1 += 1
      continue
    elif lifestore_sales[num1][1] == 21:
      prod21 += 1
      num1 += 1
      continue
    elif lifestore_sales[num1][1] == 22:
      prod22 += 1
      num1 += 1
      continue
    elif lifestore_sales[num1][1] == 25:
      prod25 += 1
      num1 += 1
      continue
    elif lifestore_sales[num1][1] == 28:
      prod28 += 1
      num1 += 1
      continue
    elif lifestore_sales[num1][1] == 29:
      prod29 += 1
      num1 += 1
      continue
    elif lifestore_sales[num1][1] == 31:
      prod31 += 1
      num1 += 1
      continue
    elif lifestore_sales[num1][1] == 33:
      prod33 += 1
      num1 += 1
      continue
    elif lifestore_sales[num1][1] == 40:
      prod40 += 1
      num1 += 1
      continue
    elif lifestore_sales[num1][1] == 42:
      prod42 += 1
      num1 += 1
      continue
    elif lifestore_sales[num1][1] == 44:
      prod44 += 1
      num1 += 1
      continue
    elif lifestore_sales[num1][1] == 45:
      prod45 += 1
      num1 += 1
      continue
    elif lifestore_sales[num1][1] == 46:
      prod46 += 1
      num1 += 1
      continue
    elif lifestore_sales[num1][1] == 47:
      prod47 += 1
      num1 += 1
      continue
    elif lifestore_sales[num1][1] == 48:
      prod48 += 1
      num1 += 1
      continue
    elif lifestore_sales[num1][1] == 49:
      prod49 += 1
      num1 += 1
      continue
    elif lifestore_sales[num1][1] == 50:
      prod50 += 1
      num1 += 1
      continue
    elif lifestore_sales[num1][1] == 51:
      prod51 += 1
      num1 += 1
      continue
    elif lifestore_sales[num1][1] == 52:
      prod52 += 1
      num1 += 1
      continue
    elif lifestore_sales[num1][1] == 54:
      prod54 += 1
      num1 += 1
      continue
    elif lifestore_sales[num1][1] == 57:
      prod57 += 1
      num1 += 1
      continue
    elif lifestore_sales[num1][1] == 60:
      prod60 += 1
      num1 += 1
      continue
    elif lifestore_sales[num1][1] == 66:
      prod66 += 1
      num1 += 1
      continue
    elif lifestore_sales[num1][1] == 67:
      prod67 += 1
      num1 += 1
      continue
    elif lifestore_sales[num1][1] == 74:
      prod74 += 1
      num1 += 1
      continue
    elif lifestore_sales[num1][1] == 84:
      prod84 += 1
      num1 += 1
      continue
    elif lifestore_sales[num1][1] == 85:
      prod85 += 1
      num1 += 1
      continue
    elif lifestore_sales[num1][1] == 89:
      prod89 += 1
      num1 += 1
      continue
    elif lifestore_sales[num1][1] == 94:
      prod94 += 1
      num1 += 1
      continue
  else:
    num1 += 1
    continue
    break


devoluciones = [
    prod1, prod2, prod3, prod4, prod5, prod6, prod7, prod8, prod10, prod11,
    prod12, prod13, prod17, prod18, prod21, prod22, prod25, prod28, prod29,
    prod31, prod33, prod40, prod42, prod44, prod45, prod46, prod47, prod48,
    prod49, prod50, prod51, prod52, prod54, prod57, prod60, prod66, prod67,
    prod74, prod84, prod85, prod89, prod94
]
devoluciones.sort(reverse=True)
devoluciones2 = [['Producto 1', prod1], ['Producto 2', prod2], ['Producto 3', prod3],
          ['Proucto 4', prod4], ['Producto 5', prod5], ['Producto 6', prod6],
          ['Producto 7', prod7], ['Producto 8', prod8],
          ['Producto 10', prod10], ['Producto 11', prod11],
          ['Producto 12', prod12], ['Producto 13', prod13],
          ['Producto 17', prod17], ['Producto 18', prod18],
          ['Producto 21', prod21], ['Producto 22', prod22],
          ['Producto 25', prod25], ['Producto 28', prod28],
          ['Producto 29', prod29], ['Producto 31', prod31],
          ['Producto 33', prod33], ['Producto 40', prod40],
          ['Producto 42', prod42], ['Producto 44', prod44],
          ['Producto 45', prod45], ['Producto 46', prod46],
          ['Producto 47', prod47], ['Producto 48', prod48],
          ['Producto 49', prod49], ['Producto 50', prod50],
          ['Producto 51', prod51], ['Producto 52', prod52],
          ['Producto 54', prod54], ['Producto 57', prod57],
          ['Producto 60', prod60], ['Producto 66', prod66],
          ['Producto 67', prod67], ['Producto 74', prod74],
          ['Producto 84', prod84], ['Producto 85', prod85],
          ['Producto 89', prod89], ['Producto 94', prod94]]

def segundo(elem):
    return elem[1]

print("")
print("Resultado 2.1.1")
devoluciones2.sort(key=segundo, reverse=True)
print("Lista de Productos con sus Respectivas Devoluciones de Mayor a Menor:")
print("")
print(devoluciones2[:5])

print("")
print("Resultado 2.1.2")
devoluciones2.sort(key=segundo)
print("Lista de Productos con sus Respectivas Devoluciones de Menor a Mayor:")
print("")

num1 = 0
num2 = 0
for dev in devoluciones2:
  if devoluciones2[num1][1] > 0 and num2 <= 4:
    print(str(devoluciones2[num1][0])+": "+str(devoluciones2[num1][1]))
    num1 += 1
    num2 += 1
  else:
    num1 += 1

print("")
print("")
print("Parte 3")
print("")
print("")

#Ventas
prod1 = 0
prod2 = 0
prod3 = 0
prod4 = 0
prod5 = 0
prod6 = 0
prod7 = 0
prod8 = 0
prod10 = 0
prod11 = 0
prod12 = 0
prod13 = 0
prod17 = 0
prod18 = 0
prod21 = 0
prod22 = 0
prod25 = 0
prod28 = 0
prod29 = 0
prod31 = 0
prod33 = 0
prod40 = 0
prod42 = 0
prod44 = 0
prod45 = 0
prod46 = 0
prod47 = 0
prod48 = 0
prod49 = 0
prod50 = 0
prod51 = 0
prod52 = 0
prod54 = 0
prod57 = 0
prod60 = 0
prod66 = 0
prod67 = 0
prod74 = 0
prod84 = 0
prod85 = 0
prod89 = 0
prod94 = 0

num1 = 0

#Loop para sumar cuantas veces se vendió cada artículo
for ventas in lifestore_sales:
    if lifestore_sales[num1][1] == 1:
        prod1 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 2:
        prod2 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 3:
        prod3 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 4:
        prod4 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 5:
        prod5 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 6:
        prod6 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 7:
        prod7 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 8:
        prod8 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 10:
        prod10 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 11:
        prod11 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 12:
        prod12 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 13:
        prod13 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 17:
        prod17 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 18:
        prod18 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 21:
        prod21 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 22:
        prod22 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 25:
        prod25 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 28:
        prod28 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 29:
        prod29 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 31:
        prod31 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 33:
        prod33 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 40:
        prod40 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 42:
        prod42 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 44:
        prod44 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 45:
        prod45 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 46:
        prod46 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 47:
        prod47 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 48:
        prod48 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 49:
        prod49 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 50:
        prod50 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 51:
        prod51 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 52:
        prod52 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 54:
        prod54 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 57:
        prod57 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 60:
        prod60 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 66:
        prod66 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 67:
        prod67 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 74:
        prod74 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 84:
        prod84 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 85:
        prod85 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 89:
        prod89 += 1
        num1 += 1
        continue
    elif lifestore_sales[num1][1] == 94:
        prod94 += 1
        num1 += 1
        continue
        break

num2 = 0
#Multiplicacion de cantidad de productos vendidos por su respectivo precio
for ventas2 in lifestore_products:
  if lifestore_products[num2][0] == 1:
    prod1 = prod1*lifestore_products[num2][2]
    num2 += 1
    continue
  elif lifestore_products[num2][0] == 2:
    prod2 = prod2*lifestore_products[num2][2]
    num2 += 1
    continue
  elif lifestore_products[num2][0] == 3:
    prod3 = prod3*lifestore_products[num2][2]
    num2 += 1
    continue
  elif lifestore_products[num2][0] == 4:
    prod4 = prod4*lifestore_products[num2][2]
    num2 += 1
    continue
  elif lifestore_products[num2][0] == 5:
    prod5 = prod5*lifestore_products[num2][2]
    num2 += 1
    continue
  elif lifestore_products[num2][0] == 6:
    prod6 = prod6*lifestore_products[num2][2]
    num2 += 1
    continue
  elif lifestore_products[num2][0] == 7:
    prod7 = prod7*lifestore_products[num2][2]
    num2 += 1
    continue
  elif lifestore_products[num2][0] == 8:
    prod8 = prod8*lifestore_products[num2][2]
    num2 += 2
    continue
  elif lifestore_products[num2][0] == 10:
    prod10 = prod10*lifestore_products[num2][2]
    num2 += 1
    continue
  elif lifestore_products[num2][0] == 11:
    prod11 = prod11*lifestore_products[num2][2]
    num2 += 1
    continue
  elif lifestore_products[num2][0] == 12:
    prod12 = prod12*lifestore_products[num2][2]
    num2 += 1
    continue
  elif lifestore_products[num2][0] == 13:
    prod13 = prod13*lifestore_products[num2][2]
    num2 += 4
    continue
  elif lifestore_products[num2][0] == 17:
    prod17 = prod17*lifestore_products[num2][2]
    num2 += 1
    continue
  elif lifestore_products[num2][0] == 18:
    prod18 = prod18*lifestore_products[num2][2]
    num2 += 3
    continue
  elif lifestore_products[num2][0] == 21:
    prod21 = prod21*lifestore_products[num2][2]
    num2 += 1
    continue
  elif lifestore_products[num2][0] == 22:
    prod22 = prod22*lifestore_products[num2][2]
    num2 += 3
    continue
  elif lifestore_products[num2][0] == 25:
    prod25 = prod25*lifestore_products[num2][2]
    num2 += 3
    continue
  elif lifestore_products[num2][0] == 28:
    prod28 = prod28*lifestore_products[num2][2]
    num2 += 1
    continue
  elif lifestore_products[num2][0] == 29:
    prod29 = prod29*lifestore_products[num2][2]
    num2 += 2
    continue
  elif lifestore_products[num2][0] == 31:
    prod31 = prod31*lifestore_products[num2][2]
    num2 += 2
    continue
  elif lifestore_products[num2][0] == 33:
    prod33 = prod33*lifestore_products[num2][2]
    num2 += 7
    continue
  elif lifestore_products[num2][0] == 40:
    prod40 = prod40*lifestore_products[num2][2]
    num2 += 2
    continue
  elif lifestore_products[num2][0] == 42:
    prod42 = prod42*lifestore_products[num2][2]
    num2 += 2
    continue
  elif lifestore_products[num2][0] == 44:
    prod44 = prod44*lifestore_products[num2][2]
    num2 += 1
    continue
  elif lifestore_products[num2][0] == 45:
    prod45 = prod45*lifestore_products[num2][2]
    num2 += 1
    continue
  elif lifestore_products[num2][0] == 46:
    prod46 = prod46*lifestore_products[num2][2]
    num2 += 1
    continue
  elif lifestore_products[num2][0] == 47:
    prod47 = prod47*lifestore_products[num2][2]
    num2 += 1
    continue
  elif lifestore_products[num2][0] == 48:
    prod48 = prod48*lifestore_products[num2][2]
    num2 += 1
    continue
  elif lifestore_products[num2][0] == 49:
    prod49 = prod49*lifestore_products[num2][2]
    num2 += 1
    continue
  elif lifestore_products[num2][0] == 50:
    prod50 = prod50*lifestore_products[num2][2]
    num2 += 1
    continue
  elif lifestore_products[num2][0] == 51:
    prod51 = prod51*lifestore_products[num2][2]
    num2 += 1
    continue
  elif lifestore_products[num2][0] == 52:
    prod52 = prod52*lifestore_products[num2][2]
    num2 += 2
    continue
  elif lifestore_products[num2][0] == 54:
    prod54 = prod54*lifestore_products[num2][2]
    num2 += 3
    continue
  elif lifestore_products[num2][0] == 57:
    prod57 = prod57*lifestore_products[num2][2]
    num2 += 3
    continue
  elif lifestore_products[num2][0] == 60:
    prod60 = prod60*lifestore_products[num2][2]
    num2 += 6
    continue
  elif lifestore_products[num2][0] == 66:
    prod66 = prod66*lifestore_products[num2][2]
    num2 += 1
    continue
  elif lifestore_products[num2][0] == 67:
    prod67 = prod67*lifestore_products[num2][2]
    num2 += 7
    continue
  elif lifestore_products[num2][0] == 74:
    prod74 = prod74*lifestore_products[num2][2]
    num2 += 10
    continue
  elif lifestore_products[num2][0] == 84:
    prod84 = prod84*lifestore_products[num2][2]
    num2 += 1
    continue
  elif lifestore_products[num2][0] == 85:
    prod85 = prod85*lifestore_products[num2][2]
    num2 += 4
    continue
  elif lifestore_products[num2][0] == 89:
    prod89 = prod89*lifestore_products[num2][2]
    num2 += 5
    continue
  elif lifestore_products[num2][0] == 94:
    prod94 = prod94*lifestore_products[num2][2]
    num2 += 1
    continue
    break

print("")
print("Ventas Anuales por Producto en $:")
print("")
print("Producto 1: $" + str(prod1))
print("Producto 2: $" + str(prod2))
print("Producto 3: $" + str(prod3))
print("Producto 4: $" + str(prod4))
print("Producto 5: $" + str(prod5))
print("Producto 6: $" + str(prod6))
print("Producto 7: $" + str(prod7))
print("Producto 8: $" + str(prod8))
print("Producto 10: $" + str(prod10))
print("Producto 11: $" + str(prod11))
print("Producto 12: $" + str(prod12))
print("Producto 13: $" + str(prod13))
print("Producto 17: $" + str(prod17))
print("Producto 18: $" + str(prod18))
print("Producto 21: $" + str(prod21))
print("Producto 22: $" + str(prod22))
print("Producto 25: $" + str(prod25))
print("Producto 28: $" + str(prod28))
print("Producto 29: $" + str(prod29))
print("Producto 31: $" + str(prod31))
print("Producto 33: $" + str(prod33))
print("Producto 40: $" + str(prod40))
print("Producto 42: $" + str(prod42))
print("Producto 44: $" + str(prod44))
print("Producto 45: $" + str(prod45))
print("Producto 46: $" + str(prod46))
print("Producto 47: $" + str(prod47))
print("Producto 48: $" + str(prod48))
print("Producto 49: $" + str(prod49))
print("Producto 50: $" + str(prod50))
print("Producto 51: $" + str(prod51))
print("Producto 52: $" + str(prod52))
print("Producto 54: $" + str(prod54))
print("Producto 57: $" + str(prod57))
print("Producto 60: $" + str(prod60))
print("Producto 66: $" + str(prod66))
print("Producto 67: $" + str(prod67))
print("Producto 74: $" + str(prod74))
print("Producto 84: $" + str(prod84))
print("Producto 85: $" + str(prod85))
print("Producto 89: $" + str(prod89))
print("Producto 94: $" + str(prod94))

Total = prod1 + prod2 + prod3 + prod4 + prod5 + prod6 + prod7 + prod8 + prod10 + prod11 + prod12 + prod13 + prod17 + prod18 + prod21 + prod22 + prod25 + prod28 + prod29 + prod31 + prod33 + prod40 + prod42 + prod44 + prod45 + prod46 + prod47 + prod48 + prod49 + prod50 + prod51 + prod52 + prod54 + prod57 + prod60 + prod66 + prod67 + prod74 + prod74 + prod84 + prod85 + prod89 + prod94

print("")
print("Total Ventas Anuales: $" + str(Total))
Promedio_Mensual = Total/12
print("")
print("Promedio Mensual Anual: $" + str(Promedio_Mensual))

valor1 = 0
valor2 = 0
valor3 = 0
valor4 = 0
valor5 = 0
valor6 = 0
valor7 = 0
valor8 = 0
valor10 = 0
valor11 = 0
valor12 = 0
valor13 = 0
valor17 = 0
valor18 = 0
valor21 = 0
valor22 = 0
valor25 = 0
valor28 = 0
valor29 = 0
valor31 = 0
valor33 = 0
valor40 = 0
valor42 = 0
valor44 = 0
valor45 = 0
valor46 = 0
valor47 = 0
valor48 = 0
valor49 = 0
valor50 = 0
valor51 = 0
valor52 = 0
valor54 = 0
valor57 = 0
valor60 = 0
valor66 = 0
valor67 = 0
valor74 = 0
valor84 = 0
valor85 = 0
valor89 = 0
valor94 = 0

num0 = 0

for precio in lifestore_products:
  if lifestore_products[num0][0] == 1:
    valor1 = lifestore_products[num0][2]
    num0 += 1
    continue
  elif lifestore_products[num0][0] == 2:
    valor2 = lifestore_products[num0][2]
    num0 += 1
    continue
  elif lifestore_products[num0][0] == 3:
    valor3 = lifestore_products[num0][2]
    num0 += 1
    continue
  elif lifestore_products[num0][0] == 4:
    valor4 = lifestore_products[num0][2]
    num0 += 1
    continue
  elif lifestore_products[num0][0] == 5:
    valor5 = lifestore_products[num0][2]
    num0 += 1
    continue
  elif lifestore_products[num0][0] == 6:
    valor6 = lifestore_products[num0][2]
    num0 += 1
    continue
  elif lifestore_products[num0][0] == 7:
    valor7 = lifestore_products[num0][2]
    num0 += 1
    continue
  elif lifestore_products[num0][0] == 8:
    valor8 = lifestore_products[num0][2]
    num0 += 2
    continue
  elif lifestore_products[num0][0] == 10:
    valor10 = lifestore_products[num0][2]
    num0 += 1
    continue
  elif lifestore_products[num0][0] == 11:
    valor11 = lifestore_products[num0][2]
    num0 += 1
    continue
  elif lifestore_products[num0][0] == 12:
    valor12 = lifestore_products[num0][2]
    num0 += 1
    continue
  elif lifestore_products[num0][0] == 13:
    valor13 = lifestore_products[num0][2]
    num0 += 4
    continue
  elif lifestore_products[num0][0] == 17:
    valor17 = lifestore_products[num0][2]
    num0 += 1
    continue
  elif lifestore_products[num0][0] == 18:
    valor18 = lifestore_products[num0][2]
    num0 += 3
    continue
  elif lifestore_products[num0][0] == 21:
    valor21 = lifestore_products[num0][2]
    num0 += 1
    continue
  elif lifestore_products[num0][0] == 22:
    valor22 = lifestore_products[num0][2]
    num0 += 3
    continue
  elif lifestore_products[num0][0] == 25:
    valor25 = lifestore_products[num0][2]
    num0 += 3
    continue
  elif lifestore_products[num0][0] == 28:
    valor28 = lifestore_products[num0][2]
    num0 += 1
    continue
  elif lifestore_products[num0][0] == 29:
    valor29 = lifestore_products[num0][2]
    num0 += 2
    continue
  elif lifestore_products[num0][0] == 31:
    valor31 = lifestore_products[num0][2]
    num0 += 2
    continue
  elif lifestore_products[num0][0] == 33:
    valor33 = lifestore_products[num0][2]
    num0 += 7
    continue
  elif lifestore_products[num0][0] == 40:
    valor40 = lifestore_products[num0][2]
    num0 += 2
    continue
  elif lifestore_products[num0][0] == 42:
    valor42 = lifestore_products[num0][2]
    num0 += 2
    continue
  elif lifestore_products[num0][0] == 44:
    valor44 = lifestore_products[num0][2]
    num0 += 1
    continue
  elif lifestore_products[num0][0] == 45:
    valor45 = lifestore_products[num0][2]
    num0 += 1
    continue
  elif lifestore_products[num0][0] == 46:
    valor46 = lifestore_products[num0][2]
    num0 += 1
    continue
  elif lifestore_products[num0][0] == 47:
    valor47 = lifestore_products[num0][2]
    num0 += 1
    continue
  elif lifestore_products[num0][0] == 48:
    valor48 = lifestore_products[num0][2]
    num0 += 1
    continue
  elif lifestore_products[num0][0] == 49:
    valor49 = lifestore_products[num0][2]
    num0 += 1
    continue
  elif lifestore_products[num0][0] == 50:
    valor50 = lifestore_products[num0][2]
    num0 += 1
    continue
  elif lifestore_products[num0][0] == 51:
    valor51 = lifestore_products[num0][2]
    num0 += 1
    continue
  elif lifestore_products[num0][0] == 52:
    valor52 = lifestore_products[num0][2]
    num0 += 2
    continue
  elif lifestore_products[num0][0] == 54:
    valor54 = lifestore_products[num0][2]
    num0 += 3
    continue
  elif lifestore_products[num0][0] == 57:
    valor57 = lifestore_products[num0][2]
    num0 += 3
    continue
  elif lifestore_products[num0][0] == 60:
    valor60 = lifestore_products[num0][2]
    num0 += 6
    continue
  elif lifestore_products[num0][0] == 66:
    valor66 = lifestore_products[num0][2]
    num0 += 1
    continue
  elif lifestore_products[num0][0] == 67:
    valor67 = lifestore_products[num0][2]
    num0 += 7
    continue
  elif lifestore_products[num0][0] == 74:
    valor74 = lifestore_products[num0][2]
    num0 += 10
    continue
  elif lifestore_products[num0][0] == 84:
    valor84 = lifestore_products[num0][2]
    num0 += 1
    continue
  elif lifestore_products[num0][0] == 85:
    valor85 = lifestore_products[num0][2]
    num0 += 4
    continue
  elif lifestore_products[num0][0] == 89:
    valor89 = lifestore_products[num0][2]
    num0 += 5
    continue
  elif lifestore_products[num0][0] == 94:
    valor94 = lifestore_products[num0][2]
    num0 += 1
    continue
    break

num3 = 0
Enero = 0
Febrero = 0
Marzo = 0
Abril = 0
Mayo = 0
Junio = 0
Julio = 0
Agosto = 0
Septiembre = 0
Octubre = 0
Noviembre= 0
Diciembre = 0

CENE = 0
CFEB = 0
CMAR = 0
CABR = 0
CMAY = 0
CJUN = 0
CJUL = 0
CAGO = 0
CSEP = 0
COCT = 0
CNOV = 0
CDIC = 0

valor = 0

prod = 2
#Agregar el respectivo valor a cada mes
for mes in lifestore_sales:
  if lifestore_sales[num3][3][4] == "1":
    CENE += 1
    if lifestore_sales[num3][1] == 1:
      Enero += valor1
      num3 += 1
      continue
    elif lifestore_sales[num3][1] == 2:
      Enero += valor2
      num3 += 1
      continue
    elif lifestore_sales[num3][1] == 3:
        Enero += valor3
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 4:
        Enero += valor4
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 5:
        Enero += valor5
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 6:
        Enero += valor6
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 7:
        Enero += valor7
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 8:
        Enero += valor8
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 10:
        Enero += valor10
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 11:
        Enero += valor11
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 12:
        Enero += valor12
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 13:
        Enero += valor13
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 17:
        Enero += valor17
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 18:
        Enero += valor18
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 21:
        Enero += valor21
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 22:
        Enero += valor22
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 25:
        Enero += valor25
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 28:
        Enero += valor28
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 29:
        Enero += valor29
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 31:
        Enero += valor31
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 33:
        Enero += valor33
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 40:
        Enero += valor40
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 42:
        Enero += valor42
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 44:
        Enero += valor44
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 45:
        Enero += valor45
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 46:
        Enero += valor46
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 47:
        Enero += valor47
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 48:
        Enero += valor48
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 49:
        Enero += valor49
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 50:
        Enero += valor50
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 51:
        Enero += valor51
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 52:
        Enero += valor52
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 54:
        Enero += valor54
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 57:
        Enero += valor57
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 60:
        Enero += valor60
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 66:
        Enero += valor66
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 67:
        Enero += valor67
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 74:
        Enero += valor74
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 84:
        Enero += valor84
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 85:
        Enero += valor85
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 89:
        Enero += valor89
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 94:
        Enero += valor94
        num3 += 1
        continue
  elif lifestore_sales[num3][3][4] == "2":
    CFEB += 1
    if lifestore_sales[num3][1] == 1:
      Febrero += valor1
      num3 += 1
      continue
    elif lifestore_sales[num3][1] == 2:
      Febrero += valor2
      num3 += 1
      continue
    elif lifestore_sales[num3][1] == 3:
        Febrero += valor3
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 4:
        Febrero += valor4
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 5:
        Febrero += valor5
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 6:
        Febrero += valor6
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 7:
        Febrero += valor7
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 8:
        Febrero += valor8
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 10:
        Febrero += valor10
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 11:
        Febrero += valor11
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 12:
        Febrero += valor12
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 13:
        Febrero += valor13
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 17:
        Febrero += valor17
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 18:
        Febrero += valor18
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 21:
        Febrero += valor21
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 22:
        Febrero += valor22
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 25:
        Febrero += valor25
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 28:
        Febrero += valor28
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 29:
        Febrero += valor29
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 31:
        Febrero += valor31
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 33:
        Febrero += valor33
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 40:
        Febrero += valor40
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 42:
        Febrero += valor42
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 44:
        Febrero += valor44
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 45:
        Febrero += valor45
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 46:
        Febrero += valor46
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 47:
        Febrero += valor47
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 48:
        Febrero += valor48
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 49:
        Febrero += valor49
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 50:
        Febrero += valor50
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 51:
        Febrero += valor51
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 52:
        Febrero += valor52
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 54:
        Febrero += valor54
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 57:
        Febrero += valor57
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 60:
        Febrero += valor60
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 66:
        Febrero += valor66
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 67:
        Febrero += valor67
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 74:
        Febrero += valor74
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 84:
        Febrero += valor84
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 85:
        Febrero += valor85
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 89:
        Febrero += valor89
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 94:
        Febrero += valor94
        num3 += 1
        continue
  elif lifestore_sales[num3][3][4] == "3":
    CMAR += 1
    if lifestore_sales[num3][1] == 1:
      Marzo += valor1
      num3 += 1
      continue
    elif lifestore_sales[num3][1] == 2:
      Marzo += valor2
      num3 += 1
      continue
    elif lifestore_sales[num3][1] == 3:
        Marzo += valor3
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 4:
        Marzo += valor4
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 5:
        Marzo += valor5
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 6:
        Marzo += valor6
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 7:
        Marzo += valor7
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 8:
        Marzo += valor8
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 10:
        Marzo += valor10
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 11:
        Marzo += valor11
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 12:
        Marzo += valor12
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 13:
        Marzo += valor13
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 17:
        Marzo += valor17
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 18:
        Marzo += valor18
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 21:
        Marzo += valor21
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 22:
        Marzo += valor22
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 25:
        Marzo += valor25
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 28:
        Marzo += valor28
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 29:
        Marzo += valor29
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 31:
        Marzo += valor31
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 33:
        Marzo += valor33
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 40:
        Marzo += valor40
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 42:
        Marzo += valor42
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 44:
        Marzo += valor44
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 45:
        Marzo += valor45
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 46:
        Marzo += valor46
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 47:
        Marzo += valor47
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 48:
        Marzo += valor48
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 49:
        Marzo += valor49
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 50:
        Marzo += valor50
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 51:
        Marzo += valor51
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 52:
        Marzo += valor52
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 54:
        Marzo += valor54
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 57:
        Marzo += valor57
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 60:
        Marzo += valor60
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 66:
        Marzo += valor66
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 67:
        Marzo += valor67
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 74:
        Marzo += valor74
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 84:
        Marzo += valor84
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 85:
        Marzo += valor85
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 89:
        Marzo += valor89
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 94:
        Marzo += valor94
        num3 += 1
        continue
  elif lifestore_sales[num3][3][4] == "4":
    CABR += 1
    if lifestore_sales[num3][1] == 1:
      Abril += valor1
      num3 += 1
      continue
    elif lifestore_sales[num3][1] == 2:
      Abril += valor2
      num3 += 1
      continue
    elif lifestore_sales[num3][1] == 3:
        Abril += valor3
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 4:
        Abril += valor4
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 5:
        Abril += valor5
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 6:
        Abril += valor6
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 7:
        Abril += valor7
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 8:
        Abril += valor8
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 10:
        Abril += valor10
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 11:
        Abril += valor11
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 12:
        Abril += valor12
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 13:
        Abril += valor13
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 17:
        Abril += valor17
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 18:
        Abril += valor18
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 21:
        Abril += valor21
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 22:
        Abril += valor22
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 25:
        Abril += valor25
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 28:
        Abril += valor28
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 29:
        Abril += valor29
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 31:
        Abril += valor31
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 33:
        Abril += valor33
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 40:
        Abril += valor40
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 42:
        Abril += valor42
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 44:
        Abril += valor44
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 45:
        Abril += valor45
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 46:
        Abril += valor46
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 47:
        Abril += valor47
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 48:
        Abril += valor48
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 49:
        Abril += valor49
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 50:
        Abril += valor50
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 51:
        Abril += valor51
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 52:
        Abril += valor52
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 54:
        Abril += valor54
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 57:
        Abril += valor57
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 60:
        Abril += valor60
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 66:
        Abril += valor66
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 67:
        Abril += valor67
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 74:
        Abril += valor74
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 84:
        Abril += valor84
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 85:
        Abril += valor85
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 89:
        Abril += valor89
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 94:
        Abril += valor94
        num3 += 1
        continue
  elif lifestore_sales[num3][3][4] == "5":
    CMAY += 1
    if lifestore_sales[num3][1] == 1:
      Mayo += valor1
      num3 += 1
      continue
    elif lifestore_sales[num3][1] == 2:
      Mayo += valor2
      num3 += 1
      continue
    elif lifestore_sales[num3][1] == 3:
        Mayo += valor3
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 4:
        Mayo += valor4
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 5:
        Mayo += valor5
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 6:
        Mayo += valor6
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 7:
        Mayo += valor7
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 8:
        Mayo += valor8
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 10:
        Mayo += valor10
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 11:
        Mayo += valor11
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 12:
        Mayo += valor12
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 13:
        Mayo += valor13
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 17:
        Mayo += valor17
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 18:
        Mayo += valor18
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 21:
        Mayo += valor21
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 22:
        Mayo += valor22
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 25:
        Mayo += valor25
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 28:
        Mayo += valor28
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 29:
        Mayo += valor29
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 31:
        Mayo += valor31
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 33:
        Mayo += valor33
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 40:
        Mayo += valor40
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 42:
        Mayo += valor42
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 44:
        Mayo += valor44
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 45:
        Mayo += valor45
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 46:
        Mayo += valor46
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 47:
        Mayo += valor47
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 48:
        Mayo += valor48
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 49:
        Mayo += valor49
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 50:
        Mayo += valor50
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 51:
        Mayo += valor51
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 52:
        Mayo += valor52
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 54:
        Mayo += valor54
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 57:
        Mayo += valor57
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 60:
        Mayo += valor60
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 66:
        Mayo += valor66
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 67:
        Mayo += valor67
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 74:
        Mayo += valor74
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 84:
        Mayo += valor84
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 85:
        Mayo += valor85
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 89:
        Mayo += valor89
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 94:
        Mayo += valor94
        num3 += 1
        continue  
  elif lifestore_sales[num3][3][4] == "6":
    CJUN += 1
    if lifestore_sales[num3][1] == 1:
      Junio += valor1
      num3 += 1
      continue
    elif lifestore_sales[num3][1] == 2:
      Junio += valor2
      num3 += 1
      continue
    elif lifestore_sales[num3][1] == 3:
        Junio += valor3
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 4:
        Junio += valor4
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 5:
        Junio += valor5
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 6:
        Junio += valor6
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 7:
        Junio += valor7
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 8:
        Junio += valor8
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 10:
        Junio += valor10
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 11:
        Junio += valor11
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 12:
        Junio += valor12
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 13:
        Junio += valor13
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 17:
        Junio += valor17
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 18:
        Junio += valor18
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 21:
        Junio += valor21
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 22:
        Junio += valor22
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 25:
        Junio += valor25
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 28:
        Junio += valor28
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 29:
        Junio += valor29
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 31:
        Junio += valor31
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 33:
        Junio += valor33
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 40:
        Junio += valor40
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 42:
        Junio += valor42
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 44:
        Junio += valor44
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 45:
        Junio += valor45
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 46:
        Junio += valor46
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 47:
        Junio += valor47
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 48:
        Junio += valor48
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 49:
        Junio += valor49
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 50:
        Junio += valor50
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 51:
        Junio += valor51
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 52:
        Junio += valor52
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 54:
        Junio += valor54
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 57:
        Junio += valor57
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 60:
        Junio += valor60
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 66:
        Junio += valor66
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 67:
        Junio += valor67
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 74:
        Junio += valor74
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 84:
        Junio += valor84
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 85:
        Junio += valor85
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 89:
        Junio += valor89
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 94:
        Junio += valor94
        num3 += 1
        continue
  elif lifestore_sales[num3][3][4] == "7":
    CJUL += 1
    if lifestore_sales[num3][1] == 1:
      Julio += valor1
      num3 += 1
      continue
    elif lifestore_sales[num3][1] == 2:
      Julio += valor2
      num3 += 1
      continue
    elif lifestore_sales[num3][1] == 3:
        Julio += valor3
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 4:
        Julio += valor4
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 5:
        Julio += valor5
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 6:
        Julio += valor6
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 7:
        Julio += valor7
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 8:
        Julio += valor8
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 10:
        Julio += valor10
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 11:
        Julio += valor11
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 12:
        Julio += valor12
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 13:
        Julio += valor13
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 17:
        Julio += valor17
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 18:
        Julio += valor18
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 21:
        Julio += valor21
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 22:
        Julio += valor22
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 25:
        Julio += valor25
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 28:
        Julio += valor28
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 29:
        Julio += valor29
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 31:
        Julio += valor31
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 33:
        Julio += valor33
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 40:
        Julio += valor40
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 42:
        Julio += valor42
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 44:
        Julio += valor44
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 45:
        Julio += valor45
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 46:
        Julio += valor46
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 47:
        Julio += valor47
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 48:
        Julio += valor48
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 49:
        Julio += valor49
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 50:
        Julio += valor50
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 51:
        Julio += valor51
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 52:
        Julio += valor52
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 54:
        Julio += valor54
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 57:
        Julio += valor57
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 60:
        Julio += valor60
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 66:
        Julio += valor66
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 67:
        Julio += valor67
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 74:
        Julio += valor74
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 84:
        Julio += valor84
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 85:
        Julio += valor85
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 89:
        Julio += valor89
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 94:
        Julio += valor94
        num3 += 1
        continue
  elif lifestore_sales[num3][3][4] == "8":
    CAGO += 1
    if lifestore_sales[num3][1] == 1:
      Agosto += valor1
      num3 += 1
      continue
    elif lifestore_sales[num3][1] == 2:
      Agosto += valor2
      num3 += 1
      continue
    elif lifestore_sales[num3][1] == 3:
        Agosto += valor3
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 4:
        Agosto += valor4
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 5:
        Agosto += valor5
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 6:
        Agosto += valor6
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 7:
        Agosto += valor7
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 8:
        Agosto += valor8
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 10:
        Agosto += valor10
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 11:
        Agosto += valor11
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 12:
        Agosto += valor12
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 13:
        Agosto += valor13
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 17:
        Agosto += valor17
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 18:
        Agosto += valor18
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 21:
        Agosto += valor21
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 22:
        Agosto += valor22
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 25:
        Agosto += valor25
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 28:
        Agosto += valor28
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 29:
        Agosto += valor29
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 31:
        Agosto += valor31
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 33:
        Agosto += valor33
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 40:
        Agosto += valor40
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 42:
        Agosto += valor42
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 44:
        Agosto += valor44
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 45:
        Agosto += valor45
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 46:
        Agosto += valor46
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 47:
        Agosto += valor47
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 48:
        Agosto += valor48
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 49:
        Agosto += valor49
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 50:
        Agosto += valor50
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 51:
        Agosto += valor51
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 52:
        Agosto += valor52
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 54:
        Agosto += valor54
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 57:
        Agosto += valor57
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 60:
        Agosto += valor60
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 66:
        Agosto += valor66
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 67:
        Agosto += valor67
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 74:
        Agosto += valor74
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 84:
        Agosto += valor84
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 85:
        Agosto += valor85
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 89:
        Agosto += valor89
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 94:
        Agosto += valor94
        num3 += 1
        continue
  elif lifestore_sales[num3][3][4] == "9":
    CSEP += 1
    if lifestore_sales[num3][1] == 1:
      Septiembre += valor1
      num3 += 1
      continue
    elif lifestore_sales[num3][1] == 2:
      Septiembre += valor2
      num3 += 1
      continue
    elif lifestore_sales[num3][1] == 3:
        Septiembre += valor3
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 4:
        Septiembre += valor4
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 5:
        Septiembre += valor5
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 6:
        Septiembre += valor6
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 7:
        Septiembre += valor7
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 8:
        Septiembre += valor8
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 10:
        Septiembre += valor10
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 11:
        Septiembre += valor11
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 12:
        Septiembre += valor12
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 13:
        Septiembre += valor13
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 17:
        Septiembre += valor17
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 18:
        Septiembre += valor18
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 21:
        Septiembre += valor21
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 22:
        Septiembre += valor22
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 25:
        Septiembre += valor25
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 28:
        Septiembre += valor28
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 29:
        Septiembre += valor29
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 31:
        Septiembre += valor31
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 33:
        Septiembre += valor33
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 40:
        Septiembre += valor40
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 42:
        Septiembre += valor42
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 44:
        Septiembre += valor44
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 45:
        Septiembre += valor45
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 46:
        Septiembre += valor46
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 47:
        Septiembre += valor47
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 48:
        Septiembre += valor48
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 49:
        Septiembre += valor49
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 50:
        Septiembre += valor50
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 51:
        Septiembre += valor51
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 52:
        Septiembre += valor52
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 54:
        Septiembre += valor54
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 57:
        Septiembre += valor57
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 60:
        Septiembre += valor60
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 66:
        Septiembre += valor66
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 67:
        Septiembre += valor67
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 74:
        Septiembre += valor74
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 84:
        Septiembre += valor84
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 85:
        Septiembre += valor85
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 89:
        Septiembre += valor89
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 94:
        Septiembre += valor94
        num3 += 1
        continue
  elif lifestore_sales[num3][3][4] == "10":
    COCT += 1
    if lifestore_sales[num3][1] == 1:
      Octubre += valor1
      num3 += 1
      continue
    elif lifestore_sales[num3][1] == 2:
      Octubre += valor2
      num3 += 1
      continue
    elif lifestore_sales[num3][1] == 3:
        Octubre += valor3
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 4:
        Octubre += valor4
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 5:
        Octubre += valor5
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 6:
        Octubre += valor6
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 7:
        Octubre += valor7
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 8:
        Octubre += valor8
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 10:
        Octubre += valor10
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 11:
        Octubre += valor11
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 12:
        Octubre += valor12
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 13:
        Octubre += valor13
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 17:
        Octubre += valor17
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 18:
        Octubre += valor18
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 21:
        Octubre += valor21
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 22:
        Octubre += valor22
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 25:
        Octubre += valor25
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 28:
        Octubre += valor28
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 29:
        Octubre += valor29
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 31:
        Octubre += valor31
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 33:
        Octubre += valor33
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 40:
        Octubre += valor40
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 42:
        Octubre += valor42
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 44:
        Octubre += valor44
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 45:
        Octubre += valor45
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 46:
        Octubre += valor46
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 47:
        Octubre += valor47
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 48:
        Octubre += valor48
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 49:
        Octubre += valor49
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 50:
        Octubre += valor50
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 51:
        Octubre += valor51
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 52:
        Octubre += valor52
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 54:
        Octubre += valor54
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 57:
        Octubre += valor57
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 60:
        Octubre += valor60
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 66:
        Octubre += valor66
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 67:
        Octubre += valor67
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 74:
        Octubre += valor74
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 84:
        Octubre += valor84
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 85:
        Octubre += valor85
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 89:
        Octubre += valor89
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 94:
        Octubre += valor94
        num3 += 1
        continue
  elif lifestore_sales[num3][3][4] == "11":
    CNOV += 1
    if lifestore_sales[num3][1] == 1:
      Noviembre += valor1
      num3 += 1
      continue
    elif lifestore_sales[num3][1] == 2:
      Noviembre += valor2
      num3 += 1
      continue
    elif lifestore_sales[num3][1] == 3:
        Noviembre += valor3
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 4:
        Noviembre += valor4
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 5:
        Noviembre += valor5
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 6:
        Noviembre += valor6
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 7:
        Noviembre += valor7
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 8:
        Noviembre += valor8
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 10:
        Noviembre += valor10
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 11:
        Noviembre += valor11
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 12:
        Noviembre += valor12
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 13:
        Noviembre += valor13
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 17:
        Noviembre += valor17
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 18:
        Noviembre += valor18
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 21:
        Noviembre += valor21
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 22:
        Noviembre += valor22
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 25:
        Noviembre += valor25
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 28:
        Noviembre += valor28
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 29:
        Noviembre += valor29
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 31:
        Noviembre += valor31
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 33:
        Noviembre += valor33
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 40:
        Noviembre += valor40
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 42:
        Noviembre += valor42
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 44:
        Noviembre += valor44
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 45:
        Noviembre += valor45
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 46:
        Noviembre += valor46
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 47:
        Noviembre += valor47
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 48:
        Noviembre += valor48
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 49:
        Noviembre += valor49
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 50:
        Noviembre += valor50
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 51:
        Noviembre += valor51
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 52:
        Noviembre += valor52
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 54:
        Noviembre += valor54
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 57:
        Noviembre += valor57
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 60:
        Noviembre += valor60
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 66:
        Noviembre += valor66
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 67:
        Noviembre += valor67
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 74:
        Noviembre += valor74
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 84:
        Noviembre += valor84
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 85:
        Noviembre += valor85
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 89:
        Noviembre += valor89
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 94:
        Noviembre += valor94
        num3 += 1
        continue
  elif lifestore_sales[num3][3][4] == "12":
    CDIC += 1
    if lifestore_sales[num3][1] == 1:
      Diciembre += valor1
      num3 += 1
      continue
    elif lifestore_sales[num3][1] == 2:
      Diciembre += valor2
      num3 += 1
      continue
    elif lifestore_sales[num3][1] == 3:
        Diciembre += valor3
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 4:
        Diciembre += valor4
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 5:
        Diciembre += valor5
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 6:
        Diciembre += valor6
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 7:
        Diciembre += valor7
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 8:
        Diciembre += valor8
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 10:
        Diciembre += valor10
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 11:
        Diciembre += valor11
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 12:
        Diciembre += valor12
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 13:
        Diciembre += valor13
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 17:
        Diciembre += valor17
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 18:
        Diciembre += valor18
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 21:
        Diciembre += valor21
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 22:
        Diciembre += valor22
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 25:
        Diciembre += valor25
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 28:
        Diciembre += valor28
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 29:
        Diciembre += valor29
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 31:
        Diciembre += valor31
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 33:
        Diciembre += valor33
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 40:
        Diciembre += valor40
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 42:
        Diciembre += valor42
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 44:
        Diciembre += valor44
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 45:
        Diciembre += valor45
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 46:
        Diciembre += valor46
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 47:
        Diciembre += valor47
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 48:
        Diciembre += valor48
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 49:
        Diciembre += valor49
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 50:
        Diciembre += valor50
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 51:
        Diciembre += valor51
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 52:
        Diciembre += valor52
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 54:
        Diciembre += valor54
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 57:
        Diciembre += valor57
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 60:
        Diciembre += valor60
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 66:
        Diciembre += valor66
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 67:
        Diciembre += valor67
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 74:
        Diciembre += valor74
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 84:
        Diciembre += valor84
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 85:
        Diciembre += valor85
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 89:
        Diciembre += valor89
        num3 += 1
        continue
    elif lifestore_sales[num3][1] == 94:
        Diciembre += valor94
        num3 += 1
        continue
  else:
    num3 += 1
    continue
    break

print("")  
print("Ventas Totales por Mes:")
print("")
print("Enero: $" + str(Enero))
print("Febrero: $" + str(Febrero))
print("Marzo: $" + str(Marzo))
print("Abril: $" + str(Abril))
print("Mayo: $" + str(Mayo))
print("Junio: $" + str(Junio))
print("Julio: $" + str(Julio))
print("Agosto: $" + str(Agosto))
print("Septiembre: $" + str(Septiembre))
print("Octubre: $" + str(Octubre))
print("Noviembre: $" + str(Noviembre))
print("Diciembre: $" + str(Diciembre))

print("")  
print("Articulos Vendidos Totales por Mes:")
print("")
print("Enero: " + str(CENE))
print("Febrero: " + str(CFEB))
print("Marzo: " + str(CMAR))
print("Abril: " + str(CABR))
print("Mayo: " + str(CMAY))
print("Junio: " + str(CJUN))
print("Julio: " + str(CJUL))
print("Agosto: " + str(CAGO))
print("Septiembre: " + str(CSEP))
print("Octubre: " + str(COCT))
print("Noviembre: " + str(CNOV))
print("Diciembre: " + str(CDIC))

print("")  
print("Promedio de Venta por Mes:")
print("")
print("Enero: $"+str(Enero/CENE))
print("Febrero: $"+str(Febrero/CFEB))
print("Marzo: $"+str(Marzo/CMAR))
print("Abril: $"+str(Abril/CABR))
print("Mayo: $"+str(Mayo/CMAY))
print("Junio: $"+str(Junio/CJUN))
print("Julio: $"+str(Julio/CJUL))
print("Agosto: $" +str(Agosto/CAGO))
print("Septiembre: $"+str(Septiembre/CSEP))
#print(Octubre)
#print(Noviembre)
#print(Diciembre)
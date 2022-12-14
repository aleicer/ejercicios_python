lista= []
puntosX = [-2.0, 2.0]
puntosY = [3.0]
ubicacionX = []
ubicacionY = []
i= -3.0
while i <= 3.0:
  ejes= {
      "x": i,
      "y": i
  }
  lista.append(ejes)
  i= round(i + 0.001, 3)

for eje in lista:
  if eje["x"] in puntosX:
    ubicacionX.append(f'El punto {puntosX[puntosX.index(eje["x"])]} se encuentra en el index {lista.index(eje)} de la lista en eje x') 
  if eje["y"] in puntosY:
    ubicacionY.append(f'El punto {puntosY[puntosY.index(eje["y"])]} se encuentra en el index {lista.index(eje)} de la lista en eje Y') 

print(f'La lista de indices tiene un tamaño de {len(lista)} datos')
print('\n'.join(ubicacionX), '\n', '\n'.join(ubicacionY))

#=========================================================================================

#constantes
MENU_INICIO='''           -->BIENVENIDOS<--    
        INGRESE TIPO DE USUARIO
    ||  Comprador                          1||
    ||  Administrador                      2||
    ||  Finalizar                          3||\n
  '''
ADMIN= '''           -->ADMIN<--    
        INGRESE SU OPCION
    ||  Modificar precio                   1||
    ||  Modificar cantidad                 2||
    ||  Retornar                           3||\n
  '''

USUARIO= '''           -->BIENVENIDOS<--           
        INGRESE SU OPCION A COMPRAR
    ||  Nintendo                          1||
    ||  Xbox                              2||
    ||  Play                              3||
    ||  Pagar                             4||
    ||  Menu Anterior                     5||\n
  '''

#================================================================================================
def pagar(subtotal, numeroNintendo, numeroXbox, numeroPlay):
    descuento = 0
    cantidadTotal = numeroNintendo + numeroXbox + numeroPlay
    precioBrutoTotal = subtotal

    if cantidadTotal != 1:
        if cantidadTotal == 2:
            descuento = 0.10
        elif cantidadTotal >= 3 and precioBrutoTotal <= 250:
            if numeroNintendo > 0 and numeroXbox > 0 and numeroPlay > 0:
                descuento = 0.10
            else:
                descuento = 0.20
        elif precioBrutoTotal > 250 and precioBrutoTotal <= 2500:
            if (numeroNintendo > 0 and numeroXbox > 0) or (numeroNintendo > 0 and numeroPlay > 0):
                descuento = 0.30
        else:
            descuento = 0.40

    valorDescuento = precioBrutoTotal * descuento
    subtotal = precioBrutoTotal - valorDescuento
    iva = subtotal * 0.19
    total = subtotal + iva
    return f'Pa\' que se dievierta...\nLa cantidad de videojuegos comprados es de {cantidadTotal}\nEl valor de la compra sin descuentos es de ${precioBrutoTotal}\nEl descuento total por su compra es de ${valorDescuento}\nEl total de su compra es de ${total} iva incluido'


def comprador(costos, catidades):
    costoUnidadNintendo = costos['nintendo']
    costoUnidadXbox = costos['xbox']
    costoUnidadPlay = costos['play']
    cantidadNintendo = catidades['nintendo']
    cantidadXbox = catidades['xbox']
    cantidadPlay = catidades['play']
    subtotal = 0
    numeroNintendo = 0
    numeroXbox = 0
    numeroPlay = 0
    while True:
        try:
            print(USUARIO)
            opcionUsuario = int(input('Ingrese su opcion: | '))
        except ValueError:
            print('Debes escribir un numero entre 1 y 4, no letras \n')
            continue

        if type(opcionUsuario) == int and opcionUsuario <= 5 and opcionUsuario > 0:
            if opcionUsuario == 5:
                print('Retornando')
                return False
            if opcionUsuario == 1:
                print('''
              || NINTENDO  ||
              ''')
                nintendo = comprarCantidad(costoUnidadNintendo, cantidadNintendo)
                if nintendo == 0:
                    continue
                subtotal += nintendo["total"]
                numeroNintendo += nintendo["cantidad"]
            if opcionUsuario == 2:
                print('''
              || XBOX  ||
              ''')
                xbox = comprarCantidad(costoUnidadXbox, cantidadXbox)
                if xbox == 0:
                    continue
                subtotal += xbox["total"]
                numeroXbox += xbox["cantidad"]
            if opcionUsuario == 3:
                print('''
              || PLAY  ||
              ''')
                play = comprarCantidad(costoUnidadPlay, cantidadPlay)
                if play == 0:
                    continue
                subtotal += play["total"]
                numeroPlay += play["cantidad"]
            if opcionUsuario == 4:
                print(pagar(subtotal, numeroNintendo, numeroXbox, numeroPlay))
                break
        else:
            print('ingresa un numero valido entre 1 y 5 \n')
            continue


def comprarCantidad(costoUnidad, cantidad):
  cantidadProductos = int(input('Ingrese la cantidad de de juegos a comprar: '))
  if cantidadProductos > cantidad:
    print(f'No hay suficiente stock solo contamos con {cantidad}, vuelve a intentarlo')
    return 0
  total = cantidadProductos * costoUnidad
  return {
    "total": total,
    "cantidad": cantidadProductos
  }

def administrador(costos, cantidades):
    contraseña = input('''
        Ingrese Contraseña
        Recuerde que la contraseña es: 1234:v... 😆
                      ''')
    if contraseña != '1234:v':
      print('Contraseña invalida 😠')
      return False
      
    while True:
        try:
          print(ADMIN)
          opcion= int(input('Ingrese su opcion: | '))
        except ValueError:
          print('Debes escribir un numero entre 1 y 3, no letras \n')
          continue
        if type(opcion) == int and opcion <= 3 and opcion > 0:
          if opcion == 1:
              try:
                costos['nintendo'] = int(input('Ingrese el nuevo precio de Nintendo: '))
                costos['xbox'] = int(input('Ingrese el nuevo precio de Xbox: '))
                costos['play'] = int(input('Ingrese el nuevo precio de Play: '))
                continue
              except ValueError:
                print('Debes darle un valor numerico\n')
                continue
          if opcion == 2:
            try:
              cantidades['nintendo'] = int(input('Ingrese la nueva cantidad de Nintendo: '))
              cantidades['xbox'] = int(input('Ingrese la nueva cantidad de Xbox: '))
              cantidades['play'] = int(input('Ingrese la nueva cantidad de Play: '))
              continue
            except ValueError:
              print('Debes darle un valor numerico\n')
              continue
          
          if opcion == 3:
            print('Retornando')
            return {'costos':costos, 'cantidades':cantidades}
        else:
          print('ingresa un numero valido entre 1 y 5 \n')
          continue

def ciclo_de_seleccion():
  costoUnidadNintendo = 60
  costoUnidadXbox = 60
  costoUnidadPlay = 70
  cantidadNintendo = 250
  cantidadXbox = 103
  cantidadPlay = 300
  while True:
    try:
      print(MENU_INICIO)
      opcion= int(input('Ingrese su opcion: | '))
    except ValueError:
      print('Debes escribir un numero entre 1 y 3, no letras \n')
      continue

    if type(opcion) == int and opcion < 4 and opcion > 0:
      if opcion == 3:
        print('Gracias nos vemos..')
        break
      
      if opcion == 1:
        costos = {'nintendo': costoUnidadNintendo, 'xbox':costoUnidadXbox, 'play': costoUnidadPlay}
        cantidades = {'nintendo': cantidadNintendo, 'xbox':cantidadXbox, 'play': cantidadPlay}
        comprador(costos, cantidades)
        continue
      elif opcion == 2:
        costos = {'nintendo': costoUnidadNintendo, 'xbox':costoUnidadXbox, 'play': costoUnidadPlay}
        cantidades = {'nintendo': cantidadNintendo, 'xbox':cantidadXbox, 'play': cantidadPlay}
        modificaciones = administrador(costos, cantidades)
        if (modificaciones == False):
          continue
        costoUnidadNintendo = modificaciones['costos']['nintendo']
        costoUnidadXbox = modificaciones['costos']['xbox']
        costoUnidadPlay = modificaciones['costos']['play']
        cantidadNintendo = modificaciones['cantidades']['nintendo']
        cantidadXbox = modificaciones['cantidades']['xbox']
        cantidadPlay = modificaciones['cantidades']['play']
        continue
    else:
      print('ingresa un numero valido entre 1 y 3 \n')
      continue
  return 'FINALIZADO'

print(ciclo_de_seleccion())
#================================================================================================

cantidad = int(input('Ingrese la cantidad a contar en HuyPues: '))
if cantidad == 0:
  print('Debe ser mayor a 0')
else:
  for i in range(cantidad):
    if i == 0:
      continue
    if i % 3 == 0:
      print('Huy')
    elif i % 5 == 0:
      print('Pues')
    else:
      print(i)
      
#================================================================================================

cantidadTarea = int(input('Ingrese la cantidad de tareas: '))
listaTareas = []
calificacionFinal = 0
for i in range(cantidadTarea):
    nombreTarea = input(f'Ingrese el nombre de la tarea {i + 1}: ')
    ponderacionTarea = int(input(f'Ingrese la ponderacion de la tarea {i + 1} en porcentaje (%): '))
    calificacionTarea = int(input(f'Ingrese la calificacion de la tarea {i + 1} de 1 a 100: '))
    ponderado = float(f'0.{ponderacionTarea}')
    objeto = {
        'nombre': nombreTarea,
        'ponderado': ponderacionTarea,
        'calificacion': calificacionTarea,
        'equivalencia': calificacionTarea * ponderado
    }
    listaTareas.append(objeto)


for objeto in listaTareas:
    print(f"En la tarea {objeto['nombre']} con calificacion {objeto['calificacion']} tiene un ponderado de {objeto['ponderado']}%")
    calificacionFinal += objeto['equivalencia']
    
print(f'La calificacion final es de {calificacionFinal}')
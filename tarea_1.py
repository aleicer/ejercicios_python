def kilometro_a_metro():
  valor = float(input('Ingrese la cantidad de kilometros a convertir: '))
  conversion = valor * 1000
  return 'El resultado de convertir {} kilometros a metros es: {} metros'.format(valor, conversion)

def centimetro_a_metro():
  valor= float(input('Ingrese la cantidad de centimetros a convertir: '))
  conversion = valor * 0.01
  return 'El resultado de convertir {} centimetros a metro es: {} metros'.format(valor, conversion)

def kilometro_a_milla():
  valor = float(input('Ingrese la cantidad de kilometros: '))
  conversion = valor * 0.62
  return 'El resultado de convertir {} kilometros a millas es: {} millas'.format(valor, conversion)

def nota_educatic_a_canvas():
  valor = float(input('Ingrese la nota de educatic: '))
  if valor > 5 or valor <= 0:
    return 'El valor ingresado supera las 5 decimas permitidas o es negativo'
  conversion = valor * 20
  return 'El resultado de convertir {} nota educatic a canvas es: {} nota canvas'.format(valor, conversion)

def nota_canvas_a_educatic():
  valor = float(input('Ingrese la nota de canvas: '))
  if valor > 100 or valor <= 0:
    return 'El valor ingresado supera las 100 decimas permitidas o es negativo'
  conversion = valor * 0.05
  return 'El resultado de convertir {} nota canvas a educatic es: {} nota educatic'.format(valor, conversion)

def mililitri_a_centimetroCubico():
  valor = float(input('Ingrese los mililitris: '))
  return 'El resultado de {} militros son {} centimetros cubicos XD'.format(valor, valor)

def dolar_a_peso_colombiano():
  valor = float(input('Ingrese la cantidad de dolares: $'))
  if valor < 0:
    return 'Los valores negativos no estan permitidos'
  conversion = valor * 5068
  return 'El resultado de convertir {} dolares a pesos colombianos es: ${:,.2f} pesos'.format(valor, conversion)

def peso_colombiano_a_dolar():
  valor = float(input('Ingrese la cantidad de pesos colombianos: $'))
  if valor < 0:
    return 'Los valores negativos no estan permitidos'
  conversion = valor * 0.00020
  return 'El resultado de convertir {} pesos colombianos a dolares es: ${:,.2f} dolares'.format(valor, conversion)

def libra_a_kilogramo():
  valor = float(input('Ingrese la cantidad de libras: '))
  conversion = valor * 0.45
  return 'El resultado de convertir {} libras a kilogramos es: {} kilos'.format(valor, conversion)

def minuto_luz_a_kilometro():
  valor = float(input('Ingrese la cantidad de minutos luz: '))
  if valor < 0:
    return 'No se admiten valores negativos'
  conversion = valor * 17987539.67
  return 'El resultado de convertir {} minutos luz a kilometros es: {:,.2f} kilometros'.format(valor, conversion)

def menu():
  print('      -->BIENVENIDOS<--    ')
  print('  INGRESE LA OPCION QUE DESEA USAR')
  print('''
    Kilómetro a metro ==>                     0
    Centímetro a metro ==>                    1
    Kilómetro por hora a millas por hora ==>  2 
    Nota en Educatic a nota en Canvas ==>     3
    Nota en Canvas a nota en Educatic ==>     4
    Mililitro a centímetro cúbico ==>         5
    Dólar (USA) a peso colombiano ==>         6
    Peso colombiano a dólar (USA) ==>         7
    Libra a kilogramo ==>                     8
    Minuto luz a kilómetro ==>                9
    Finalizar ejecucion ==>                  10\n
  ''')

def ciclo_de_seleccion():
  while True:
    try:
      menu()
      option= int(input('Ingrese su opcion: | '))
    except ValueError:
      print('Debes escribir un numero entre 0 y 10, no letras \n')
      continue

    if type(option) == int and option < 11 and option >= 0:
      if option == 10:
        print('Gracias nos vemos..')
        break
      cases= {
        0: kilometro_a_metro,
        1: centimetro_a_metro,
        2: kilometro_a_milla,
        3: nota_educatic_a_canvas,
        4: nota_canvas_a_educatic,
        5: mililitri_a_centimetroCubico,
        6: dolar_a_peso_colombiano,
        7: peso_colombiano_a_dolar,
        8: libra_a_kilogramo,
        9: minuto_luz_a_kilometro,
      }
      try:
        solution = cases[option]()
        print(solution)
        print('''
                *
               ***
              *****
        ''')
        continue
      except ValueError:
        print('Al parecer ingresaste un valor erroneo, vamos de nuevo \n')
        continue
    else:
      print('ingresa un numero valido entre 0 y 10 \n')
      continue
  return 'FINALIZADO'

print(ciclo_de_seleccion())
#=========================================================================================
# Desarrolle su ejercicio aquí.
from math import sqrt

def distanceBetweenPoints():
  print('Ingrese los 2 valores del punto 1: ')
  x1= float(input())
  y1= float(input())

  print('Ingrese los 2 valores del punto 2: ')
  x2= float(input())
  y2= float(input())

  distancia= sqrt((x2-x1)**2 + (y2-y1)**2)
  print('La distancia entre los dos puntos es: {:,.2f}'.format(distancia))

print(distanceBetweenPoints())

#=========================================================================================
# Desarrolle su ejercicio aquí
def planetsTime():
  SPEED_OF_LIGHT=300000
  planets = [
    {'planet': 'Mercurio', 'distance': 57910000},
    {'planet': 'Venus', 'distance': 108200000}, 
    {'planet': 'Tierra', 'distance': 149600000}, 
    {'planet': 'Marte', 'distance': 227910000}, 
    {'planet': 'Júpiter', 'distance': 778330000}, 
    {'planet': 'Saturno', 'distance': 1429400000},
    {'planet': 'Urano', 'distance':	2870990000}, 
    {'planet': 'Neptuno', 'distance':	4504300000}]

  for planet in planets:
    timeInSeconds= planet['distance'] / SPEED_OF_LIGHT
    timeInMinutes= int(timeInSeconds / 60)
    print('El tiempo que tarda la luz en llegar a {} es de {:,.2f} segundos, es decir, alrededor de {} minutos'.format(planet['planet'], timeInSeconds, timeInMinutes))

print(planetsTime())


#=========================================================================================
#@title Texto de título predeterminado
tarea1 = 0 #@param {type:"number"}
tarea2 = 0 #@param {type:"number"}
tarea3 = 0 #@param {type:"number"}
tarea4 = 100 #@param {type:"number"}
# Desarrolle su ejercicio aquí.

def calcularPonderado(tarea1, tarea2, tarea3, tarea4):
  validador = tarea1 + tarea2 + tarea3 + tarea4
  if validador > 400 or validador < 0:
    return print('Debe ingresar valores de 0 a 100') 
  porcentaje1= 0.25 #25%
  porcentaje2= 0.25 #25%
  porcentaje3= 0.30 #30%
  porcentaje4= 0.20 #20%

  equivalencia1= tarea1 * porcentaje1
  equivalencia2= tarea2 * porcentaje2
  equivalencia3= tarea3 * porcentaje3
  equivalencia4= tarea4 * porcentaje4

  ponderado= equivalencia1 + equivalencia2 + equivalencia3 + equivalencia4
  return print('El ponderado de las 4 notas es: ', ponderado)

print(calcularPonderado(tarea1, tarea2, tarea3, tarea4))
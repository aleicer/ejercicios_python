def imprimir_valores_dinamicos (opcion: int, valor: int, conversion: int):
  imprimible= {
    0: 'El resultado de convertir {} kilometros a metros es: {} metros'.format(valor, conversion),
    1: 'El resultado de convertir {} centimetros a metro es: {} metros'.format(valor, conversion),
    2: 'El resultado de convertir {} kilometros a millas es: {} millas'.format(valor, conversion),
    3: 'El resultado de convertir {} nota educatic a canvas es: {} nota canvas'.format(valor, conversion),
    4: 'El resultado de convertir {} nota canvas a educatic es: {} nota educatic'.format(valor, conversion),
    5: 'El resultado de {} militros son {} centimetros cubicos XD'.format(valor, valor),
    6: 'El resultado de convertir {} dolares a pesos colombianos es: ${:,.2f} pesos'.format(valor, conversion),
    7: 'El resultado de convertir {} pesos colombianos a dolares es: ${:,.2f} dolares'.format(valor, conversion),
    8: 'El resultado de convertir {} libras a kilogramos es: {} kilos'.format(valor, conversion),
    9: 'El resultado de convertir {} minutos luz a kilometros es: {:,.2f} kilometros'.format(valor, conversion),
  }
  return imprimible[opcion]

def menu():
  print('      -->BIENVENIDOS<--    ')
  print('  INGRESE LA OPCION QUE DESEA USAR')
  print('''
    ||  Kilómetro a metro ==>                            0  ||
    ||  Centímetro a metro ==>                           1  ||
    ||  Kilómetro por hora a millas por hora ==>         2  ||
    ||  Nota en Educatic a nota en Canvas ==>            3  ||
    ||  Nota en Canvas a nota en Educatic ==>            4  ||
    ||  Mililitro a centímetro cúbico ==>                5  ||
    ||  Dólar (USA) a peso colombiano ==>                6  ||
    ||  Peso colombiano a dólar (USA) ==>                7  ||
    ||  Libra a kilogramo ==>                            8  ||
    ||  Minuto luz a kilómetro ==>                       9  ||
    ||  Finalizar ejecucion ==>                         10  ||\n
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
      listParameters= [1000, 0.01, 0.62, 20, 0.05, 1, 4811, 0.00020, 0.45, 17987539.67]
      input
      try:
        valor = float(input('Ingrese el valor a convertir: '))
        conversion = listParameters[option]
        solucion = valor * conversion
        print(imprimir_valores_dinamicos(option, valor, solucion))
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
#@title Mero Gamer
cantidad_nintendo = 31 #@param {type:"slider", min:0, max:100, step:1}
cantidad_xbox = 2 #@param {type:"slider", min:0, max:100, step:1}
cantidad_play = 0 #@param {type:"slider", min:0, max:100, step:1}

#constantes
NINTENDO = 60
XBOX = 60
PLAY = 70

#variables
descuento = 0
cantidadTotal = cantidad_nintendo + cantidad_xbox + cantidad_play

#precios sin descuento
precioNintendo = NINTENDO * cantidad_nintendo
precioXbox = XBOX * cantidad_xbox
precioPlay = PLAY * cantidad_play
precioBrutoTotal = precioNintendo + precioXbox + precioPlay

if cantidadTotal != 1:
  if cantidadTotal == 2: 
    descuento = 0.10
  elif cantidadTotal >= 3 and precioBrutoTotal <= 250:
    if cantidad_nintendo > 0 and cantidad_play > 0 and cantidad_xbox > 0:
      descuento = 0.10
    else:
      descuento = 0.20
  elif precioBrutoTotal > 250 and precioBrutoTotal <= 2500:
    if (cantidad_nintendo > 0 and cantidad_xbox > 0) or (cantidad_nintendo > 0 and cantidad_play > 0):
      descuento = 0.30
  else:
    descuento = 0.40

valorDescuento = precioBrutoTotal * descuento
subtotal = precioBrutoTotal - valorDescuento
iva = subtotal * 0.19
total = subtotal + iva
print(f'Pa\' que se dievierta...\nLa cantidad de videojuegos comprados es de {cantidadTotal}\nEl valor de la compra sin descuentos es de ${precioBrutoTotal}\nEl descuento total por su compra es de ${valorDescuento}\nEl total de su compra es de ${total} iva incluido')


#=========================================================================================

lado1 = input('Ingrese el lado 1 del triangulo: ')
lado2 = input('Ingrese el lado 2 del triangulo: ')
lado3 = input('Ingrese el lado 3 del triangulo: ')
angulo1 = input('Ahora ingrese el angulo 1: ')
angulo2 = input('Ahora el 2do angulo: ')
angulo3 = input('y por ultimo el angulo 3: ')

validador1 = lado1 + lado2
validador2 = lado1 + lado3
sumaAngulos = angulo1 + angulo2 + angulo3
respuestaLados = ''
respuestaAngulos = 'el triangulo cumple con los angulos'

if validador1 > lado3 or validador2 > lado2:
  respuestaLados = 'estan correctos'
else: 
  respuestaLados = 'no corresponden a un triangulo'

if sumaAngulos != 180:
  respuestaAngulos = 'no cumple con los angulos'

print(f'El triangulo con los valores que plantea:\n Los lados {respuestaLados}\n En cuanto a los angulos {respuestaAngulos}')

#=========================================================================================

#@title Ponderado de notas
nombre_nota_1 = "ejercicio 1" #@param {type:"string"}
nota_1 = 71 #@param {type:"slider", min:0, max:100, step:1}
nombre_nota_2 = "tarea 2" #@param {type:"string"}
nota_2 = 91 #@param {type:"slider", min:0, max:100, step:1}
nombre_nota_3 = "evaluacion 3" #@param {type:"string"}
nota_3 = 68 #@param {type:"slider", min:0, max:100, step:1}
nombre_nota_4 = "examen 4" #@param {type:"string"}
nota_4 = 74 #@param {type:"slider", min:0, max:100, step:1}

diccionarioNotas = {
    'nota1': {
        'nombre': nombre_nota_1,
        'nota': nota_1
    },
    'nota2': {
        'nombre': nombre_nota_2,
        'nota': nota_2
    },
    'nota3': {
        'nombre': nombre_nota_3,
        'nota': nota_3
    },
    'nota4': {
        'nombre': nombre_nota_4,
        'nota': nota_4
    },
}
totalNotas = 0
for objecto in diccionarioNotas:
  totalNotas = totalNotas + diccionarioNotas[objecto]['nota']

ponderadoNotas = totalNotas / len(diccionarioNotas)
print(f'''El ponderado de las notas de los ejercicios:
{diccionarioNotas['nota1']['nombre']} con nota {diccionarioNotas['nota1']['nota']}
{diccionarioNotas['nota2']['nombre']} con nota {diccionarioNotas['nota2']['nota']}
{diccionarioNotas['nota3']['nombre']} con nota {diccionarioNotas['nota3']['nota']}
{diccionarioNotas['nota4']['nombre']} con nota {diccionarioNotas['nota4']['nota']}
tiene un ponderado de nota de: {ponderadoNotas} nota final
      ''')
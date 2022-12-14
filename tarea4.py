import random as rnd

BIENVENIDA= '''
    BIENVENIDOS A LAS VOTACIONES
'''
MENU= '''
    Escoja una opcion
    ||  Votacion manual por jugador          1||
    ||  Votacion automatica                  2||
    ||  Finalizar programa                   3||
'''
listadoJugadores = [
    'Lionel Messi',
    'Cristiano Ronaldo',
    'Kylian Mbappé',
    'Neymar',
    'Kevin De Bruyne',
    'Joshua Kimmich',
    'Dušan Vlahović',
    'Robert Lewandowski',
    'Harry Kane',
    'Luis Suárez',
]

listaJueces = [
  'Guillem Balague',
  'Julio Maldonado',
  'Antonio Romero',
  'Pedro Martín',
  'Fernando Evangelio',
  'Diego Armando Maradona',
  'Michel Platini',
  'Franz Beckenbauer',
  'Ronaldinho Gaúcho',
  'Zinedine Zidane',
]

def seleccionadorJugadores(lista:list)-> list:
    jugadoresSeleccionados = []
    for i in lista:
        if len(jugadoresSeleccionados) == 3:
            break
        seleccionado = rnd.choice(lista)
        if seleccionado in jugadoresSeleccionados:
            continue
        jugadoresSeleccionados.append(seleccionado)
    return jugadoresSeleccionados

def votacionManual(seleccionados: list, jueces: list)-> dict:
    # Crear diccionario de votos a llenar
    votos = {
      'jugador1': {
        'nombre': '',
        'votos': [],
        'puntaje': 0
      },
      'jugador2': {
        'nombre': '',
        'votos': [],
        'puntaje': 0
      },
      'jugador3': {
        'nombre': '',
        'votos': [],
        'puntaje': 0
      }
    }
    # iteracion de jugadores seleccionados
    for jugador in seleccionados:
      print('\n==>Recuerde que los votos deben ingresarse entre 0 y 10<==\n')
      print(f'Votaciones para jugador {jugador}')
      votos[f'jugador{seleccionados.index(jugador) + 1}']['nombre'] = jugador
      # Iteracion de cada juez para votacion
      for juez in jueces:
        while True:
          try:
            voto = int(input(f'Ingrese el voto del juez {juez}: | '))
          except ValueError:
            print('Debes escribir un numero entre 1 y 4, no letras \n')
            continue
          if type(voto) == int and voto < 11 and voto >= 0:
            puntaje= votos[f'jugador{seleccionados.index(jugador) + 1}']['puntaje']
            # Agregamos otro diccionario a la lista de votos dentro de diccionario principal
            votos[f'jugador{seleccionados.index(jugador) + 1}']['votos'].append({'juez': juez, 'voto': voto})
            votos[f'jugador{seleccionados.index(jugador) + 1}']['puntaje'] = puntaje + voto # Sumamos cada voto al puntaje
            break
          else:
            print('Ingresa el voto entre 0 y 10 \n')
            continue
        # Ordenamos los votos de menor a mayor
        votos[f'jugador{seleccionados.index(jugador) + 1}']['votos']= sorted(votos[f'jugador{seleccionados.index(jugador) + 1}']['votos'] , key=lambda i: i['voto'], reverse=False)
    return votos

def votacionAutomatica(seleccionados: list, jueces: list)-> dict:
    # Crear diccionario de votos a llenar
    votos = {
      'jugador1': {
        'nombre': '',
        'votos': [],
        'puntaje': 0
      },
      'jugador2': {
        'nombre': '',
        'votos': [],
        'puntaje': 0
      },
      'jugador3': {
        'nombre': '',
        'votos': [],
        'puntaje': 0
      }
    }
    # iteracion de jugadores seleccionados
    for jugador in seleccionados:
      votos[f'jugador{seleccionados.index(jugador) + 1}']['nombre'] = jugador
      # Iteracion de cada juez para votacion
      for juez in jueces:
        voto = rnd.choice(range(0, 11))
        puntaje= votos[f'jugador{seleccionados.index(jugador) + 1}']['puntaje']
        # Agregamos otro diccionario a la lista de votos dentro de diccionario principal
        votos[f'jugador{seleccionados.index(jugador) + 1}']['votos'].append({'juez': juez, 'voto': voto})
        votos[f'jugador{seleccionados.index(jugador) + 1}']['puntaje'] = puntaje + voto # Sumamos cada voto al puntaje
      # Ordenamos los votos de menor a mayor
      votos[f'jugador{seleccionados.index(jugador) + 1}']['votos']= sorted(votos[f'jugador{seleccionados.index(jugador) + 1}']['votos'] , key=lambda i: i['voto'], reverse=False)
    return votos

def definirResultados(votos: dict) -> dict:
  categoria = 'Bajo'
  votosCrudos = [0,0,0,0,0,0,0,0,0,0,0]
  for jugador in votos:
    votaciones = votos[jugador]['votos']
    for voto in votaciones:
      votosCrudos[voto['voto']] += 1
  votoMasUsado = max(votosCrudos)
  votoMayorVotacion = votosCrudos.index(votoMasUsado)
  if votoMayorVotacion == 10 or votoMayorVotacion == 9:
    categoria = 'Alto'
  elif votoMayorVotacion < 9 and votoMayorVotacion >= 6:
    categoria = 'Medio'
  mayorPuntaje = max(votos.keys(), key = lambda k: votos[k]['puntaje'])
  jugadorMayorPuntaje = votos[mayorPuntaje]
  return f'''
        Promediando las votaciones, los jueces votaron {votoMasUsado} veces el numero {votoMayorVotacion} es decir la categoria mas botada fue {categoria}\n
        Damos nuestras felicitaciones al jugador {jugadorMayorPuntaje['nombre'].upper()} por su gran desempeño con un puntaje de {jugadorMayorPuntaje['puntaje']} puntos\n
        Para verificaciones las votaciones del jugador {jugadorMayorPuntaje['nombre']} fueron las siguientes: {jugadorMayorPuntaje['votos']}
        '''

def ejecutar():
    votos = {}
    #selecciona 3 jugadores al azar de la lista de jugadores
    jugadoresSeleccionados = seleccionadorJugadores(listadoJugadores)
    print(f'''\nLos jugadores seleccionados de este partido son: 
          --->  {jugadoresSeleccionados[0].upper()}, 
          --->  {jugadoresSeleccionados[1].upper()}, 
          --->  {jugadoresSeleccionados[2].upper()}
          ''')
    
    while True:
        try:
            print(BIENVENIDA)
            print(MENU)
            opcionUsuario = int(input('Ingrese su opcion: | '))
        except ValueError:
            print('Debes escribir un numero entre 1 y 4, no letras \n')
            continue

        if type(opcionUsuario) == int and opcionUsuario <= 3 and opcionUsuario > 0:
            if opcionUsuario == 1:
                votos = votacionManual(jugadoresSeleccionados, listaJueces)
                return definirResultados(votos)
            elif opcionUsuario == 2:
                votos = votacionAutomatica(jugadoresSeleccionados, listaJueces)
                return definirResultados(votos)
            else:
              return 'Gracias por usar el programa'
        else:
            print('ingresa un numero valido entre 1 y 5 \n')
            continue
    return votos         

print(ejecutar())


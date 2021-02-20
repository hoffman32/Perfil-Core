import itertools



###################Partida de ping pong#############################

def ping_pong():
  """
  Funcionalidad que resuelve ambos puntos de la partida de PING PONG
  Parametros internos:
  - pj: Partidas jugadas
  - pjp: Partidas jugadas pares
  - pji: Partidas jugadas impares
  Return:
  - jsn: Json con las partidas jugadas por Juan
  """
  ana = 17
  jose = 15
  juan = 10
  print('Ana ', 17, 'Jose', 15, 'Juan', 10)
  #Si las sumamos estamos contando 2 veces la misma partida
  pj= (ana + jose + juan)/2

  print('Se jugaron en total: ', int(pj), ' partidas')

  #Cuando una persona pierde todas las partidas
  #sale ,significa que esta intermitente en los partidos jugados al ser solo 3 personas las que juegan
  pjp=0
  pji=0
  jsn = {}
  for i in range(1, int(pj+1)):
    if i%2 == 0:
      #print('par', i)
      jsn[i] = 'Perdio'
      pjp+=1
    else:
      #print('impar', i)
      jsn[i] = 'No jugo'
      pji+=1
  
  print('Partidas jugadas pares :', pjp)
  print('Partidas jugadas impares :', pji)

  #Juan que jugo 10 partidas es igual la cantidad de partidas pares que jugaria la persona que pierde
  #todas las partidas

  print('Juan es la persona que pierde {} partidas de las {} partidas jugadas'.format(pjp, int(pj)))
  print('Json con las partidas de Juan')
  return jsn

ping_pong()

##################Resultados #1 #############
"""
Ana  17 Jose 15 Juan 10
Se jugaron en total:  21  partidas
Partidas jugadas pares : 10
Partidas jugadas impares : 11
Juan es la persona que pierde 10 partidas de las 21 partidas jugadas
Json con las partidas de Juan
{1: 'No jugo',
 2: 'Perdio',
 3: 'No jugo',
 4: 'Perdio',
 5: 'No jugo',
 6: 'Perdio',
 7: 'No jugo',
 8: 'Perdio',
 9: 'No jugo',
 10: 'Perdio',
 11: 'No jugo',
 12: 'Perdio',
 13: 'No jugo',
 14: 'Perdio',
 15: 'No jugo',
 16: 'Perdio',
 17: 'No jugo',
 18: 'Perdio',
 19: 'No jugo',
 20: 'Perdio',
 21: 'No jugo'}
"""



#################Serie de fibonacci########################################


def pandigital(numero):
  """
  Funcionalidad para buscar el numero pandigital
  Parametros:
  - numero : Valor entero al cual se le verificara si es pandigital o no.
  Returns:
  - Booleano : True o False para aplicar condiciones en iteracion.
  """
  n=str(numero)
  if len(n) < 9:
      return False
  else:
      lista=["1","2","3","4","5","6","7","8","9"]
      for x in n:
          if x in lista:
              lista.remove(x)
      if len(lista) == 0:
          return True
      else:
          return False

def fibonacci(n):
  """
  Calculador del numero actual y siguiente de serie fibonacci dependiendo de el grado de fibonacci.
  Parametros:
  - n : Grado de fibonacci
  Returns:
  - (c, d) ò (d, c+d) : Tuplas de actual y siguiente de la serie de fibonacci.
  """
  if n == 0:
      return (0, 1)
  else:
      a, b = fibonacci(n // 2)
      c = a * (b * 2 - a)
      d = a * a + b * b
      if n % 2 == 0:
          return (c, d)
      else:
          return (d, c + d)

def buscador():
  """
  Buscador de la serie de fibonacci iterativo con secciones pandigital al inicio y fin.
  Returns:
  - Grado de la serie de fibonacci que tiene pandigital al inicio y final.
  """
  k2 = 10**9
  x1 = 0
  x2 = 1
  for i in itertools.count():
    if pandigital(str(x1)[-9:]):  
      f = fibonacci(i)[0]
      if pandigital(str(f)[:9]):  
        return str(i)
    x1, x2 = x2, (x1 + x2) % k2
  return str(ans)

print('El grado de la serie de fibonacci con pandigital al inicio y final es : ', buscador())


########################Resultados #2 ###########################
"""
El grado de la serie de fibonacci con pandigital al inicio y final es :  329468
"""



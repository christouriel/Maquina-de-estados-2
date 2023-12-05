#automata_finito.py
class Estado:
  Q0, Q1, Q2, Q3, NO_RECONOCIDO = range(5)

def validar_contrasena(input_string):
  pos = 0
  actual = Estado.Q0
  cadena_rechazada = False

  while not cadena_rechazada and pos < len(input_string):
      simbolo = input_string[pos]

      if actual == Estado.Q0:
          if simbolo.isalnum():
              actual = Estado.Q1
          else:
              cadena_rechazada = True

      elif actual == Estado.Q1:
          if simbolo.isalnum():
              actual = Estado.Q1
          elif simbolo in ['@', '#', '$', '&']:
              actual = Estado.Q2
          else:
              cadena_rechazada = True

      elif actual == Estado.Q2:
          if simbolo.isalnum() or simbolo in ['!', '%']:
              actual = Estado.Q3
          else:
              cadena_rechazada = True

      elif actual == Estado.Q3:
          if simbolo.isalnum() or simbolo in ['!', '%']:
              actual = Estado.Q3
          else:
              cadena_rechazada = True

      pos += 1

  if cadena_rechazada:
      return Estado.NO_RECONOCIDO

  return actual


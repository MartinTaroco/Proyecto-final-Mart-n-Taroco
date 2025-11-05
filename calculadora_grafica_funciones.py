import math
import csv  #Permite trabajar con csv
import os  #Permite interactuar con el Sistema operativo

def calculadora_raices(a,b,c):
  
  if abs(b) ** 2 - 4*a*c >= 0:
    discriminante = abs(b) ** 2 - 4*a*c
    x1 = (-b + math.sqrt(discriminante)) / (2*a)
    x2 = (-b - math.sqrt(discriminante)) / (2*a)
    return x1, x2
  else:
     return "Error"


def calculadora_vertice(a,b,c):
  xv = -b/(2*a)
  yv = a* (xv ** 2) + b * xv + c
  return xv, yv

def agregar_a_csv(a, b, c):
    # Construye la ruta completa al archivo dentro de la carpeta data
    ruta = os.path.join("data", "coeficientes_funciones.csv")

    # Abre el archivo en modo append
    with open(ruta, mode="a", newline="") as f:
        writer = csv.writer(f)  #Creamos el objeto pars escribir
        writer.writerow([a, b, c])   #agregamos filas

def concavidad(a):
  if a > 0:
    return "Positiva"
  else:
    return "Negativa"
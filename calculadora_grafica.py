import tkinter
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from calculadora_grafica_funciones import calculadora_raices, calculadora_vertice, agregar_a_csv, concavidad

#Creamos la Ventana donde será nuestra interfaz
ventana = tkinter.Tk()
ventana.geometry("2000x2000")  #Tamaño de ventana


#Creamos la etiqueta que será el titulo de nuestro programa
etiqueta = tkinter.Label(ventana, text= "INGRESA LOS COEFICIENTES a, b y c DE TU FUNCIÓN DE SEGUNDO GRADO", 
    font=("cursive", 12, "bold"),     # fuente, tamaño y estilo
    fg="blue",                      # color del texto (foreground)
    bg="lightyellow",               # color de fondo
    padx=10,                        # relleno horizontal interno
    pady=10                         # relleno vertical interno)
)
etiqueta.pack(pady=2)   #La agregamos a la ventana



#Caja y boton donde se ingresará el coeficiente a
cajaA = tkinter.Entry(ventana)
cajaA.pack(pady=5)

botonA = tkinter.Button(ventana, text= "Escribe el coeficiente a") 
botonA.pack(pady=5)

#-----------------------------------------------------------------------------------------#
#Caja y boton donde se ingresará el coeficiente b
cajaB = tkinter.Entry(ventana)
cajaB.pack(pady=5)


botonB = tkinter.Button(ventana, text= "Escribe el coeficiente b") 
botonB.pack(pady=5)
#-------------------------------------------------------------------------------------------#
#Caja y boton donde se ingresará el coeficiente c

cajaC = tkinter.Entry(ventana)
cajaC.pack(pady=5)


botonC = tkinter.Button(ventana, text= "Escribe el coeficiente c")
botonC.pack(pady=5)
#----------------------------------------------------------------------------------------------- 

 #Dimensiones de la gráfica
fig = Figure(figsize=(2, 2), dpi=100)  #Creamos al figura y sus dimensiones
ax = fig.add_subplot(111)                   #Le ponemos ejes a la figura
canvas = FigureCanvasTkAgg(fig, master=ventana)   #Al canvas en blanco le metemos la figura
canvas.get_tk_widget().pack(pady=20)              #Llevamos al canvas a tkinter

#Mensajes que aparecerán y tendran su texto modificado cuando se confirmen los coeficientes.
mensaje_validacion = tkinter.Label(ventana, text="", fg="blue", font=("Arial", 12))
mensaje_validacion.pack(pady=2)
mensaje1 = tkinter.Label(ventana, text="", fg="blue", font=("Arial", 12))
mensaje1.pack(pady=2)
mensaje2 = tkinter.Label(ventana, text="", fg="blue", font=("Arial", 12))
mensaje2.pack(pady=2)
mensaje3 = tkinter.Label(ventana, text="", fg="blue", font=("Arial", 12))
mensaje3.pack(pady=2)
mensaje4 = tkinter.Label(ventana, text="", fg="blue", font=("Arial", 12))
mensaje4.pack(pady=2)


#La función se llama cuando le damos al boton confirmar
def graficar():
  #Toma los coeficientes de las cajas de texto, los convertimos en float
  parametroA = float(cajaA.get())    
  parametroB = float(cajaB.get())
  parametroC = float(cajaC.get())
 
  agregar_a_csv(parametroA,parametroB,parametroC)
 
 #Tenemos en cuenta los diferentes casos, con mensaje personalizados, no queremos mostrar un error, sino señalar que obtendría en cada caso.
  if parametroA == 0 and parametroB != 0:
    mensaje_validacion.config(text="Obtienes una función de primer grado!! trata con a diferente de 0", fg="red")
  
  elif parametroA == 0 and parametroB ==0 and parametroC ==0 or parametroA ==0 and parametroB == 0:
    mensaje_validacion.config(text="Obtienes una función constante!! trata con a diferente de 0", fg="red")
  else:
    mensaje_validacion.config(text="", fg="red")
    
 # Limpiar gráfico anterior
  ax.clear()

#Damos los valores de x y sus imagenes
  x = np.linspace(-10, 10, 200)  #Creamos 200 valores entre -10 y 10, (pre-imagenes)
  y = parametroA*x**2 + parametroB*x + parametroC   #imagenes



  #Graficamos
  ax.plot(x, y, color="blue")  
 
  # Poner las líneas de los ejes en el origen (x=0, y=0)
  ax.axhline(0, color="black", linewidth=1)   # eje X en y=0
  ax.axvline(0, color="black", linewidth=1)   # eje Y en x=0

  # titulo de la gráfica
  ax.set_title(f"y = {parametroA}x² + {parametroB}x + {parametroC}")
  ax.grid(True)

    
  #Mostrar en Tkinter
  canvas.draw()
  
  #Confioguramos los mensajes que proporiconan Raices, ordenada en el origen y vértice
  
  #Raices
  raices = calculadora_raices(parametroA, parametroB, parametroC)
  if raices == "Error":
    mensaje1.config(text=f"No existen raices reales!", fg="red")
  else:
    mensaje1.config(text=f"Raíz X1 = {raices[0]} y Raiz X2 = {raices[1]}", fg="red")
  
  #Ordenada en el origen
  mensaje2.config(text=f"La ordenada en el origen es y = {parametroC}", fg="green")
  
  #Coordenadas del vértice
  vertice = calculadora_vertice(parametroA,parametroB,parametroC)
  
  mensaje3.config(text=f"El vértice tiene coordenadas ( {vertice[0]} , {vertice[1]})  ", fg="green")
  
  concavidad_funcion =concavidad(parametroA)
  mensaje4.config(text=f"Su concavidad es: {concavidad_funcion}", fg="green")
  
  
#Funcion encargada de limpiar los valores y la grafica  
def limpiar():
  
    #Limpiamos las cajas
    cajaA.delete(0, tkinter.END)
    cajaB.delete(0, tkinter.END)
    cajaC.delete(0, tkinter.END)
    #Dejamos en blanco los mensajes
    mensaje_validacion.config(text="", fg="red")
    mensaje1.config(text="", fg="red")
    mensaje2.config(text="", fg="red")
    mensaje3.config(text="", fg="red")
    mensaje4.config(text="", fg="red")
    #borramos la grafica y dibujamos de nuevo el canvas vacio
    ax.clear()
    canvas.draw()
    
    
    
#Boton que llama a la función graficas
confirmar =tkinter.Button(ventana, text= "CONFIRMAR VALORES", command=graficar)
confirmar.pack(pady=2)
 
#Boton que limpia las cajas de texto y la grafica 
limpiar =tkinter.Button(ventana, text= "LIMPIAR VALORES", command=limpiar)
limpiar.pack(pady=2)
  


#inicializamos la función
ventana.mainloop()

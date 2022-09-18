#Paso inicial
import random
import time

#Colores
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

#Introducción
print("¡Hola! Bienvenid@ a la pequeña prueba sobre Geología")
time.sleep(1)
print("Específicamente, hoy pondremos a prueba si tienes conocimientos sobre los minerales\n")
print('¿Cuál es tu nombre?')
nombre= input()
time.sleep(1)
puntaje = random.randint(4,10)
trivia = True
intento=0
print("\nComenzarás con", puntaje, "puntos,",nombre,"\n")
time.sleep(1)

while trivia == True:
  intento += 1
  #Saludo
  print("Así que, responde las siguientes 4 preguntas:\n")
  print("Intento número: ", intento)
  time.sleep(1)

  #Primera Pregunta
  print("1.¿Qué es un mineral?")
  print("a. Es una sustancia natural con estructura interna ordenada y composición química definida")
  time.sleep(2)
  print("b. Es una sustancia inorgánica natural con estructura interna ordenada")
  time.sleep(2)
  print("c. Es un sólido inórganico natural que tiene una estructura interna ordenada y una composición química definida")
  time.sleep(2)
  print("d. Es un sólido inórganico que tiene una estructura interna ordenada y una composición química definida")
  time.sleep(2)
  respuesta=input("\nTu respuesta es: \n")
  while respuesta not in ("a","b",'c','d',"x"):
    respuesta=input('Debes responder a, b, c o d. Por favor, vuelve a ingresar tu respuesta: \n')
  if respuesta == "x":
    puntaje +=random.randint(1,3)
    print(GREEN+"\n¡Ajá!", nombre, ",", "veo que tienes mucha curiosidad, pero esta no es la respuesta correcta, tan solo una respuesta secreta. Vas teniendo", puntaje, "puntos\n"+RESET)
    time.sleep(2)
  elif respuesta == "a": 
    puntaje -=1
    print (RED+"\n¡INCORRECTO!",nombre, ",",  "recuerda que un mineral debe ser inórganico. Vas teniendo", puntaje, "puntos\n"+RESET) 
    time.sleep(2)
  elif respuesta == "b": 
    puntaje = puntaje/2
    print (RED+"\n¡INCORRECTO!",nombre, "," , "recuerda que un mineral debe tener una composición química definida. Vas teniendo", puntaje, "puntos\n"+RESET)
    time.sleep(2)
  elif respuesta == "c":
    puntaje +=1
    print (BLUE+"\n¡CORRECTO!",nombre,",", "vas avanzando bien. Vas teniendo", puntaje, "puntos\n"+RESET)
    time.sleep(2)
  else:
    puntaje -=3
    print (RED+"\n¡INCORRECTO!",nombre,",", "no olvides que un mineral debe ser natural. Vas teniendo", puntaje, "puntos\n"+RESET)
    time.sleep(2)

  #Segunda Pregunta
  print("2.¿Cuál es un mineral?")
  print("a. Pirita")
  time.sleep(1)
  print("b. Hielo de la refrigeradora")
  time.sleep(1)
  print("c. Ópalo")
  time.sleep(1)
  print("d. Ámbar")
  time.sleep(1)
  respuesta1=input("\nTu respuesta es: \n")
  while respuesta1 not in ("a","b",'c','d',"x"):
    respuesta1=input('Debes responder a, b, c o d. Por favor, vuelve a ingresar tu respuesta: \n')
  if respuesta1 == "x":
    puntaje +=random.randint(1,5)
    print(GREEN+"\nObservo que hay mucha insistencia en respuestas secretas.", nombre, ",", "estás cerca de encontrar algo novedoso. Sigue así, crack. Vas teniendo", puntaje, "puntos\n"+RESET)
    time.sleep(2)
  elif respuesta1 == "a":
    puntaje =puntaje*2
    print (BLUE+"\n¡CORRECTO!",nombre, ",",  "vas entendiendo el concepto. Vas teniendo", puntaje, "puntos\n"+RESET) 
    time.sleep(2)
  elif respuesta1 == "b": 
    puntaje -=1.5
    print (RED+"\n¡INCORRECTO!",nombre, "," , "el hielo de la refrigeradora no es natural. Vas teniendo", puntaje, "puntos\n"+RESET)
    time.sleep(2)
  elif respuesta1 == "c":
    puntaje -=0.5
    print (RED+"\n¡INCORRECTO!",nombre,",", "porque el ópalo es amorfo, es decir, no tiene una estructura interna definida. Vas teniendo", puntaje, "puntos\n"+RESET)
    time.sleep(2)
  else:
    puntaje -=2.5
    print (RED+"\n¡INCORRECTO!",nombre,",", "el ámbar no es mineral porque proviene de una fuente órganica. Recuerda que el ámbar es resina fosilizada proveniente de árboles. Vas teniendo", puntaje, "puntos\n"+RESET)
    time.sleep(2)

  #Tercera Pregunta
  print("3.¿Qué mineral es pesado?")
  print("a. Halita")
  time.sleep(1)
  print("b. Calcita")
  time.sleep(1)
  print("c. Cuarzo")
  time.sleep(1)
  print("d. Cinabrio")
  time.sleep(1)
  respuesta2=input("\nTu respuesta es: \n")
  while respuesta2 not in ("a","b",'c','d',"x"):
    respuesta2=input('Debes responder a, b, c o d. Por favor, vuelve a ingresar tu respuesta: \n')
  if respuesta2 == "x":
    puntaje +=random.randint(1,7)
    print(GREEN+"\nTienes hambre de puntos. Vas teniendo ", puntaje, "puntos\n"+RESET)
    time.sleep(2)
  elif respuesta2 == "a":
    puntaje = puntaje -1
    print (RED+"\n¡INCORRECTO!", nombre, ",",  "ese mineral tiene bajo peso específico. Vas teniendo ", puntaje, "puntos\n" +RESET)
    time.sleep(2)
  elif respuesta2 == "b": 
    puntaje = puntaje - 3
    print (RED+"\n¡INCORRECTO!",nombre, "," , "la calcita pesa poquísimo. Vas teniendo", puntaje, "puntos\n"+RESET)
    time.sleep(2)
  elif respuesta2 == "c":
    puntaje = puntaje - 2
    print (RED+"\n¡INCORRECTO!",nombre,",", "el cuarzo tiene 2.67 g/cm3 aproximadamente. Vas teniendo", puntaje, "puntos\n"+RESET)
    time.sleep(2)
  else:
    puntaje = puntaje + 1
    print (BLUE+"\n¡CORRECTO!",nombre,",", "el cinabrio tiene más peso específico que la galena. Recuerda no es tóxico a pesar de tener mercurio. Vas teniendo", puntaje, "puntos\n"+RESET)
    time.sleep(2)

#Cuarta Pregunta
  print("4.¿Qué mineral tiene clivaje perfecto?")
  print("a. Calcopirita")
  time.sleep(1)
  print("b. Clorita")
  time.sleep(1)
  print("c. Marcasita")
  time.sleep(1)
  print("d. Arsenopirita")
  time.sleep(1)
  respuesta3=input("\nTu respuesta es: \n")
  while respuesta3 not in ("a","b",'c','d',"x"):
    respuesta3=input('Debes responder a, b, c o d. Por favor, vuelve a ingresar tu respuesta: \n')
  if respuesta3 == "x":
    puntaje +=random.randint(1,9)
    print(GREEN+"\nCálmate, que te llevarás todo XD. Vas teniendo ", puntaje, "puntos\n"+RESET)
    time.sleep(2)
  elif respuesta3 == "a":
    puntaje -= 0.25
    print (RED+"\n¡INCORRECTO!",nombre, ",",  "el clivaje de la calcopirita es pobre. Vas teniendo ", puntaje, "puntos\n"+RESET) 
    time.sleep(2)
  elif respuesta3 == "b": 
    puntaje += 1
    print (BLUE+"\n¡CORRECTO!",nombre, "," , "el clivaje de la clorita es perfecto en una dirección. Vas teniendo", puntaje, "puntos\n"+RESET)
    time.sleep(2)
  elif respuesta3 == "c":
    puntaje -= 1.25
    print (RED+"\n¡INCORRECTO!",nombre,",", "su clivaje clivaje no es imperfecto como la pirita, que es su polimorfo, pero tampoco es perfecto. Vas teniendo", puntaje, "puntos\n"+RESET)
    time.sleep(2)
  else:
    puntaje -=0.75
    print (RED+"\n¡INCORRECTO!",nombre,",", "su clivaje puede llegar a ser bueno, mas no perfecto, de este mineral que tiene color blanco de estaño. Vas teniendo", puntaje, "puntos\n"+RESET)
    time.sleep(2)
    
  #Valor aleatorio
  numero_ale=int(input("Escribe un número: "))
  time.sleep(1)
  
  #Comentario Final
  print(MAGENTA+"\nGracias", nombre, ",","por haber respondido estas preguntas. Lo anterior te restará puntos jejeje. Así, obtuviste",puntaje - numero_ale,"puntos"+RESET)
  time.sleep(1)


  print("\n¿Deseas volver a hacer la prueba?")
  repetir_trivia=input("Ingresa 'Sí' para repetir o digita cualquier tecla para culminar la prueba: ").lower()

if repetir_trivia != "Sí":
  print("\nEspero que hayas disfrutado bastante este pequeño test")
  trivia=False 
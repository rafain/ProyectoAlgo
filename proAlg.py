from __future__ import division
from __future__ import print_function
from tabulate import tabulate
from prettytable import PrettyTable
from texttable import Texttable
from random import randint
from math import log10
import time
aleatoria = 0

#TERMINADO NO TOCAR
def quickSort(lis, first, last):
  comp = 0
  inter = 0
  despl = 0

  comp += 1
  if first<last:
    comp2, inter2, despl2, split = quickSortH(lis, first, last)

    comp3, inter3, despl3 = quickSort(lis, first, split-1)
    comp4, inter4, despl4 = quickSort(lis, split+1, last)

    comp += comp2 + comp3 + comp4
    inter += inter2 + inter3 + inter4
    despl += despl2 + despl3 + despl4
  
  if (aleatoria == 1):
    print(lis)

  return (comp, inter, despl)

def quickSortH(lis, first, last):
  comp = 0
  inter = 0
  despl = 0

  pivot = lis[first]
  left = first +1
  right = last
  Done = False

  while not Done:
    comp += 1
    while (left <= right and lis[left] <= pivot):
      comp += 1
      left += 1
    while (left <= right and lis[right] >= pivot):
      comp += 1
      right -= 1
    comp += 1
    if (left > right):
      Done = True
    else:
      inter += 1
      temp = lis[right]
      lis[right] = lis[left]
      lis[left] = temp
  
  inter += 1
  lis[first] = lis[right]
  lis[right] = pivot
  if(aleatoria == 1):
    print(lis)
  return (comp, inter, despl, right)
#Aqui termina QuickSort


#TERMINADO NO TOCAR
def selectionSort(lis):
  comp = 0
  inter = 0
  despl = 0

  for j in range(len(lis)-1,0,-1):
    max = 0
    for i in range(1,j+1):
      comp += 1
      if(lis[i] > lis[max]):
        max = i
    
    inter += 1
    prob = lis[max]
    lis[max] = lis[j]
    lis[j] = prob
    if (aleatoria == 1):
      print(lis) 

  return (comp, inter, despl)
#Aqui termina selectionSort


#TERMINADO NO TOCAR
def heapify(lis, n, parent): 
    comp = 0
    swaps = 0
    swapping = parent
    rightchild = 2 * parent +2
    leftchild = 2 * parent +1
    
    if leftchild < n and lis[parent] < lis[leftchild]: 
        swapping = leftchild 
        comp += 1
        
    if rightchild < n and lis[swapping] < lis[rightchild]: 
        swapping = rightchild 
        comp += 1
        
    if swapping != parent: 
        lis[parent],lis[swapping] = lis[swapping],lis[parent] 
        heapify(lis, n, swapping)
        swaps += 1
        
    return (comp, swaps)
  
def heapSort(lis): 
    n = len(lis) 
    comp = 0
    swaps = 0
    inter = 0

    for i in range(n, -1, -1): 
        comp2, swaps2 = (heapify(lis, n, i)) 
        comp += comp2
        swaps += swaps2

    for i in range(n-1, 0, -1): 
        lis[i], lis[0] = lis[0], lis[i]
        comp3, swaps3 = (heapify(lis, i, 0))
        comp += comp3
        swaps += swaps3
        if aleatoria == 1:
            print(lis)
    return(lis, comp, swaps, inter)
#Aquí termina HEAP SORT


#TERMINADO NO TOCAR
def mergeSort(lis):
  comp = 0
  inter = 0
  despl = 0

  if len(lis) <= 1:
    if (aleatoria == 1):
      print(lis)
    return (lis, comp, inter, despl)
  else:
    split = len(lis)//2
    lis2, comp2, inter2, despl2 = mergeSort(lis[:split])
    lis3 , comp3, inter3, despl3 = mergeSort(lis[split:len(lis)])
    lis, comp4, inter4, despl4 = merge(lis2, lis3)
    comp += comp2 + comp3 + comp4
    inter += inter2 + inter3 + inter4
    despl += despl2 + despl3 + despl4

    if (aleatoria == 1):
      print(lis)
    return (lis, comp, inter, despl)

def merge(lis, lis2):
  comp = 0
  inter = 0
  despl = 0

  res = []
  while(len(lis) > 0 and len(lis2) > 0):

    comp += 1
    if (lis[0] < lis2[0]):
      res.append(lis.pop(0))
    else:
      res.append(lis2.pop(0))

  comp += 1
  if(len(lis) > 0):
    res += lis
  else:
    res += lis2
  
  return (res, comp, inter, despl)
#Aqui termina Merge Sort



#TERMINADO NO TOCAR
def bubbleSort(lis):
  comp = 0
  inter = 0
  despl = 0

  n = len(lis)
  for i in range(n-1):
    for j in range(n-i-1):
      comp += 1
      if (lis[j] > lis[j+1]):
        inter += 1
        prob = lis[j+1]
        lis[j+1] = lis[j]
        lis[j] = prob
    if (aleatoria == 1):
      print(lis)
  return (comp, inter, despl)
#Aquí termina bubbleSort


#TERMINADO NO TOCAR
def insertionSort(lis):
  comp = 0
  inter = 0
  despl = 0

  for j in range(1, len(lis)):
    val = lis[j]
    pos = j
    comp += 2
    while(pos > 0 and val < lis[pos-1]):
      comp += 2
      lis[pos] = lis[pos-1]
      despl += 1
      pos = pos-1
    
    lis[pos] = val
    if (aleatoria == 1):
      print(lis)
    
  return(comp,inter,despl)
#Aquí termina insertionSort


def llenarLista():
  arr = []
  x = int(input("¿Cuántos números deseas agregar?\n"))
  for i in range(x):
    try:
      y = int(input("Escribe el número: "))
      arr.append(y)
    except Exception:
      print("Introduce un valor correcto. Vuelve a iniciar")
      arr = llenarLista()
      break
  return arr

def numerosAleatorios():
  arr = []
  print("Se generaran un millón de números aleatorios. Por favor espere\n")
  for i in range(10000): #100000
    arr.append(randint(0,1000000)) 
  return arr

def main():
  global aleatoria
  lista = []
  print("\n*****************************************\n")
  print("Bienvenido. En este proyecto podrás comparar los diferentes algoritmos de ordenamiento. Por favor seleccion una opción:\n")

  print("1. Introducir los números.")
  print("2. Generar los números de manera aleatoria")
  print("3. Salir\n")

  print("*****************************************\n")

  try:
    aleatoria = int(input("Elije tu opción[1 2 3]: "))
  except Exception:
    print("Introduzca una opción válida")
    aleatoria = 0

  while(True):
    if(aleatoria == 1):
      lista = llenarLista()
      break; 
    elif(aleatoria == 2):
      lista = numerosAleatorios()
      print("Gracias por esperar. Tu números han sido generados\n")
      break
    elif(aleatoria == 3):
      break
    else:
      print("El valor dado es incorrecto. Por favor otorgue una opción válida")
      try:
        aleatoria = int(input("Elije tu opción[1 2 3]: "))
      except Exception:
        print("Introduzca una opción válida")
        aleatoria = 0

  n = len(lista)

  #Corrida para Bubble Sort
  table = PrettyTable(["", 'Comparaciones', 'Intercambios','Desplazamientos', 'Tiempo'])
  

  if(aleatoria == 1):
    print("\n**********************************************************\n")
    print("\nBubble Sort: \n")

  lisBS = list(lista)
  start = time.time()
  compBS, interBS, desplBS = bubbleSort(lisBS)
  end = time.time()

  if (aleatoria == 1):
    print("\n")
    tableCM = Texttable()
    tableCM.add_row(["",'Comparaciones','Intercambios','Desplazamientos']) 
    tableCM.add_row(['Notacion 0',['O(n^2) = ', n**2], [0, n**2],0])      
    tableCM.add_row(['Realizadas',str(compBS),str(interBS),str(desplBS)])
    print(tableCM.draw())
    
    print("Tiempo de ejecución: " + str(end-start)+"\n")
    print(lisBS)
    print("\n**********************************************************\n")
  elif(aleatoria == 2):

    print("               |       Comparaciones       |       Intercambios        |     Desplazamiento        |       Tiempo")
    print("BubbleSort     |             "+ str(compBS)+"        |              "+ str(interBS) +"       |             "+str(desplBS)+"             |            "+ str(end-start))
  

  #Corrida para Selection Sort
  if (aleatoria == 1):
    print("\n**********************************************************\n")
    print("Selection Sort: \n")
  lisSS = list(lista)
  start = time.time()
  compSS, interSS, desplSS = selectionSort(lisSS)
  end = time.time()

  if (aleatoria == 1):
    print("\n")
    tableCM = Texttable()
    tableCM.add_row(["",'Comparaciones','Intercambios','Desplazamientos'])
    tableCM.add_row(['Notacion 0',['O(n^2) = ', n**2], [n, n],0])          
    tableCM.add_row(['Realizadas',str(compSS),str(interSS),str(desplSS)])
    print(tableCM.draw())
    
    print("Tiempo de ejecución: " + str(end-start)+"\n")
    print(lisSS)
    print("\n**********************************************************\n")
  elif(aleatoria == 2):
    print("SelectionSort  |             "+ str(compSS)+"        |              "+ str(interSS) +"       |             "+str(desplSS)+"             |            "+ str(end-start))


  #Corrida Insertion Sort
  if (aleatoria == 1):
    print("\n**********************************************************\n")
    print("Insertion Sort: \n")
  lisIS = list(lista)
  start = time.time()
  compIS, interIS, desplIS = insertionSort(lisIS)
  end = time.time()

  if (aleatoria == 1):
    print("\n")
    tableCM = Texttable()
    tableCM.add_row(["",'Comparaciones','Intercambios','Desplazamientos'])
    tableCM.add_row(['Notacion 0',['O(n^2) = ', n**2], 0 ,[1, n**2]])      
    tableCM.add_row(['Realizadas',str(compIS),str(interIS),str(desplIS)])
    print(tableCM.draw())
    
    print("Tiempo de ejecución: " + str(end-start)+"\n")
    print(lisIS)
    print("\n**********************************************************\n")
  elif(aleatoria == 2):
    print("InsertionSort  |             "+ str(compIS)+"        |              "+ str(interIS) +"       |             "+str(desplIS)+"             |            "+ str(end-start))

  #Corrida para Merge Sort
  if (aleatoria == 1):
    print("\n**********************************************************\n")
    print("Merge Sort: \n")
  lisMS = list(lista)    
  start = time.time()
  lisMSord, compMS, interMS, desplMS = mergeSort(lisMS)
  end = time.time()

  if (aleatoria == 1):
    print("\n")
    tableCM = Texttable()
    tableCM.add_row(["",'Comparaciones','Intercambios','Desplazamientos'])
    tableCM.add_row(['Notacion 0',['O(nlogn) = ', n * log10(n)], [n * log10(n) , n * log10(n)],0])               
    tableCM.add_row(['Realizadas',str(compMS),str(interMS),str(desplMS)])
    print(tableCM.draw())
    
    print("Tiempo de ejecución: " + str(end-start)+"\n")
    print(lisMSord)
    print("\n**********************************************************\n")
  elif(aleatoria == 2):
    print("MergeSort      |             "+ str(compMS)+"        |              "+ str(interMS) +"       |             "+str(desplMS)+"             |            "+ str(end-start))


  #Corrida para HeapSort
  if (aleatoria == 1):
    print("\n**********************************************************\n")
    print("Heap Sort: \n")
  lisHS = list(lista)
  start = time.time()
  liaHS, compHS, interHS, desplHS = heapSort(lisHS)
  end = time.time()

  if (aleatoria == 1):
    print("\n")
    tableCM = Texttable()
    tableCM.add_row(["",'Comparaciones','Intercambios','Desplazamientos'])
    tableCM.add_row(['Notacion 0',['O(nlogn) = ', n * log10(n)], [n * log10(n) , n * log10(n)],0])            
    tableCM.add_row(['Realizadas',str(compHS),str(interHS),str(desplHS)])
    print(tableCM.draw())

    print("Tiempo de ejecución: " + str(end-start)+"\n")
    print(lisHS)
    print("\n**********************************************************\n")
  elif(aleatoria == 2):
    print("HeapSort      |             "+ str(compHS)+"        |              "+ str(interHS) +"       |             "+str(desplHS)+"             |            "+ str(end-start))


  #Corrida para Quick Sort
  if (aleatoria == 1):
    print("\n**********************************************************\n")
    print("Quick Sort: \n")
  lisQS = list(lista)
  start = time.time()
  compQS, interQS, desplQS = quickSort(lisQS, 0, len(lisQS)-1)
  end = time.time()

  if (aleatoria == 1):
    print("\n")
    tableCM = Texttable()
    tableCM.add_row(["",'Comparaciones','Intercambios','Desplazamientos'])
    tableCM.add_row(['Notacion 0',['O(n^2) = ', n**2], [n * log10(n), n**2] ,0]) 
    tableCM.add_row(['Realizadas',str(compQS),str(interQS),str(desplQS)])
    print(tableCM.draw())

    print("Tiempo de ejecución: " + str(end-start)+"\n")
    print(lisQS)
    print("\n**********************************************************\n")
  elif(aleatoria == 2):
    print("QuickSort      |             "+ str(compQS)+"        |              "+ str(interQS) +"       |             "+str(desplQS)+"             |            "+ str(end-start))

main()

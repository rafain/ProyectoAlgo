# Proyecto de comparación de algoritmos de ordenamiento.
# Realizado por:
#   Jesús Perea
#   Samuel Sánchez
#   Juan Manuel Gómez
#   Rafaín Rodríguez
#
# 13-nov-2018

def quickSort(lis):
    comp = 0
    inter = 0
    despl = 0

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

  return(comp,inter)


def heapSort(lis):
    comp = 0
    inter = 0
    despl = 0

def mergeSort(lis):
    comp = 0
    inter = 0
    despl = 0

def bubbleSort(lis):
      comp = 0
  inter = 0
  despl = 0

  n = len(lis)
  for i in range(n-1):
    for i in range(n-1):
      comp += 1
      if (lis[i] > lis[i+1]):
        inter += 1
        prob = lis[i+1]
        lis[i+1] = lis[i]
        lis[i] = prob
  return(comp,inter)


def insertionSort(lis):
    comp = 0
    inter = 0
    despl = 0


def main():
    

main()

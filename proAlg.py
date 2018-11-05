# Proyecto de comparación de algoritmos de ordenamiento.
# Realizado por:
#   Jesús Perea
#   Samuel Sánchez
#   Juan Manuel Gómez
#   Rafaín Rodríguez
#
# 13-nov-2018

#Hello Everybody. This is a git test
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
      comp += 2
      left += 1
    while (left <= right and lis[right] >= pivot):
      comp += 2
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

  return (comp, inter, despl, right)



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

  return (comp, inter, despl)



def heapSort(lis):
    comp = 0
    inter = 0
    despl = 0

    
    
def mergeSort(lis):
  comp = 0
  inter = 0
  despl = 0

  comp += 1
  if len(lis) <= 1:
    return (lis, comp, inter, despl)
  else:
    split = len(lis)//2
    lis2, comp2, inter2, despl2 = mergeSort(lis[:split])
    lis3 , comp3, inter3, despl3 = mergeSort(lis[split:len(lis)])
    lis, comp4, inter4, despl4 = merge(lis2, lis3)
    comp += comp2 + comp3 + comp4
    inter += inter2 + inter3 + inter4
    despl += despl2 + despl3 + despl4

    return (lis, comp, inter, despl)

def merge(lis, lis2):
  comp = 0
  inter = 0
  despl = 0

  res = []
  while(len(lis) > 0 and len(lis2) > 0):
    comp += 2

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
  return (comp, inter, despl)




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
    
  return(comp,inter,despl)


def main():
    

main()

import random
import math
import sys
import time

def ISEQUAL(array, SL, SR):
    for k in range(SL+1, SR-1):
        if array[k] != array[SL]:
            SWAP(array, k, SL)
            return k
    return -1

def INSRIGHT(array, CurrItem, SR, right):
    j = SR
    while j <= right and CurrItem > array[j]:
        array[j - 1] = array[j]
        j = j + 1
    array[j-1] = CurrItem

def INSLEFT(array, CurrItem, SL, left):
    j = SL
    while j >= left and CurrItem < array[j]:
        array[j + 1] = array[j]
        j = j - 1
    array[j+1] = CurrItem


def SWAP(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

def BCIS(array, left, right):
    SL = left
    SR = right

    while SL < SR:
        SWAP(array, SR, SL+((SR-SL)//2))

        if array[SL] == array[SR]:
            if ISEQUAL(array, SL, SR) == -1:
                return

        if array[SL] > array[SR]:
            SWAP(array, SL, SR)

        if (SR - SL) >= 100:
            for i in range(SL+1, math.floor((SR-SL)**0.5)):
                if array[SR] < array[i]:
                    SWAP(array, SR, i)
                elif array[SL] > array[i]:
                    SWAP(array, SL, i)
        
        i = SL+1
        
        LC = array[SL]
        RC = array[SR]

        while i < SR:
            CurrItem = array[i]
            if CurrItem >= RC:
                array[i] = array[SR - 1]
                INSRIGHT(array, CurrItem, SR, right)
                SR = SR - 1
            elif CurrItem <= LC:
                array[i] =  array[SL + 1]
                INSLEFT(array, CurrItem, SL, left)
                SL = SL + 1
                i = i + 1
            else:
                i = i + 1
        SL = SL + 1
        SR = SR - 1

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key


# Python program for implementation of MergeSort
def mergeSort(arr):
    if len(arr) > 1:
  
         # Finding the mid of the array
        mid = len(arr)//2
  
        # Dividing the array elements
        L = arr[:mid]
  
        # into 2 halves
        R = arr[mid:]
  
        # Sorting the first half
        mergeSort(L)
  
        # Sorting the second half
        mergeSort(R)
  
        i = j = k = 0
  
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
  
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
  
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def beginrandomSort(length):
    list_a = []

    len_a = length

    print("-"*20)
    print(f"Sorting random array with {len_a} elements")
    print("-"*20)
    print()

    for i in range(len_a):
        list_a.append(random.randint(0, 100000))

    list_a_is = list_a.copy()
    list_a_bcis = list_a.copy()
    list_a_mergesort = list_a.copy()

    print('Begin Sorting with BCIS')
    start_time = time.time()
    BCIS(list_a_bcis, 0, len_a-1)
    print(f"--- {time.time() - start_time} seconds ---\n")

    print('Begin Sorting with Insertion Sort')
    start_time = time.time()
    insertionSort(list_a_is)
    print(f"--- {time.time() - start_time} seconds ---\n")

    print('Begin Sorting with Merge Sort')
    start_time = time.time()
    mergeSort(list_a_mergesort)
    print(f"--- {time.time() - start_time} seconds ---\n\n")

def beginascSort(length):
    list_a = []

    len_a = length

    print("-"*20)
    print(f"Sorting sorted ascending array with {len_a} elements")
    print("-"*20)
    print()

    for i in range(len_a):
        list_a.append(i)

    list_a_is = list_a.copy()
    list_a_bcis = list_a.copy()
    list_a_mergesort = list_a.copy()

    print('Begin Sorting with BCIS')
    start_time = time.time()
    BCIS(list_a_bcis, 0, len_a-1)
    print(f"--- {time.time() - start_time} seconds ---\n")

    print('Begin Sorting with Insertion Sort')
    start_time = time.time()
    insertionSort(list_a_is)
    print(f"--- {time.time() - start_time} seconds ---\n")

    print('Begin Sorting with Merge Sort')
    start_time = time.time()
    mergeSort(list_a_mergesort)
    print(f"--- {time.time() - start_time} seconds ---\n\n")

def begindescSort(length):
    list_a = []

    len_a = length

    print("-"*20)
    print(f"Sorting sorted descending array with {len_a} elements")
    print("-"*20)
    print()
    
    for i in range(len_a, 0, -1):
        list_a.append(i)

    list_a_is = list_a.copy()
    list_a_bcis = list_a.copy()
    list_a_mergesort = list_a.copy()

    print('Begin Sorting with BCIS')
    start_time = time.time()
    BCIS(list_a_bcis, 0, len(list_a_bcis)-1)
    print(f"--- {time.time() - start_time} seconds ---\n")

    print('Begin Sorting with Insertion Sort')
    start_time = time.time()
    insertionSort(list_a_is)
    print(f"--- {time.time() - start_time} seconds ---\n")

    print('Begin Sorting with Merge Sort')
    start_time = time.time()
    mergeSort(list_a_mergesort)
    print(f"--- {time.time() - start_time} seconds ---\n\n")


num_element = [32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536]

for ijk in num_element:
    beginascSort(ijk)

for ijk in num_element:
    begindescSort(ijk)

for ijk in num_element:
    beginrandomSort(ijk)
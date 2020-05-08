import time 
import sys

import gen


def heapify(arr, n, i):
    largest = i 
    l = 2 * i + 1     
    r = 2 * i + 2     
  
    if l < n and arr[i] < arr[l]: 
        largest = l 

    if r < n and arr[largest] < arr[r]: 
        largest = r 
  
    if largest != i: 
        arr[i], arr[largest] = arr[largest], arr[i] 
  
        heapify(arr, n, largest) 


def heap_sort(arr):
    n = len(arr) 
  
    for i in range(n//2 - 1, -1, -1): 
        heapify(arr, n, i) 
  
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] 
        heapify(arr, i, 0) 


def merge(arr, l, m, r): 
    len1, len2 =  m - l + 1, r - m  
    left, right = [], []  
    for i in range(0, len1):  
        left.append(arr[l + i])  
    for i in range(0, len2):  
        right.append(arr[m + 1 + i])  
    
    i, j, k = 0, 0, l 

    while i < len1 and j < len2:  
       
        if left[i] <= right[j]:  
            arr[k] = left[i]  
            i += 1 
           
        else: 
            arr[k] = right[j]  
            j += 1 
           
        k += 1
       
    while i < len1:  
       
        arr[k] = left[i]  
        k += 1 
        i += 1
    
    while j < len2:  
        arr[k] = right[j]  
        k += 1
        j += 1


def merge_sort(arr):
    if len(arr) >1: 
        mid = len(arr)//2 #Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
  
        merge_sort(L) # Sorting the first half 
        merge_sort(R) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1


def partition(arr, low, high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than the pivot 
        if   arr[j] < pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 


def quick_sort(arr, low, high):
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr, low, high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quick_sort(arr, low, pi-1) 
        quick_sort(arr, pi+1, high) 


def insertion_sort(arr, left, right):  
    for i in range(left + 1, right+1):  
       
        temp = arr[i]  
        j = i - 1 
        while j >= left and arr[j] > temp :  
            arr[j+1] = arr[j]  
            j -= 1
           
        arr[j+1] = temp  



def tim_sort(arr, n):
    for i in range(0, n, 32):  
        insertion_sort(arr, i, min((i+31), (n-1)))  
    
    size = 32
    while size < n:  
        for left in range(0, n, 2*size):  

            mid = min((left + size - 1), (n-1))
            right = min((left + 2*size - 1), (n-1))  
    
            merge(arr, left, mid, right)  
          
        size = 2*size 


def print_commands():
    print('Commands: ')
    print('random n             Generates a list of random numbers.')
    print('mostly_sorted n      Generates a list of mostly sorted numbers.')
    print('sin_pattern n        Generates a list of values ranging from -10000 to 10000 in a sin pattern.');
    print('half_half n          Generates a list of numbers where the first half of the elements belong in the second half of the list and vice versa.')
    print('Were \'n\' is the number of elements you want to generate')


def main(argc, argv):
    # The number of tests to run
    tests_count = 1
    if (argc == 4):
        tests_count = int(argv[3])

    # The times for each algorigthm
    heap_sort_times = []
    merge_sort_times = []
    quick_sort_times = []
    tim_sort_times = []

    for i in range(0, tests_count):
        # The list of numbers to be sorted
        list_to_sort = list()

        # Generate the input data to be sorted 
        if argv[1] == 'random':
            gen.random(int(argv[2]))
        elif argv[1] == 'mostly_sorted':
            gen.mostly_sorted(int(argv[2]))
        elif argv[1] == 'sin_pattern':
            gen.sin_pattern(int(argv[2]))
        elif argv[1] == 'half_half':
            gen.half_half(int(argv[2]))
        elif argv[1] == 'help':
            print_commands()
        else:
            print('Invalid command. Type help to get a list of commands.')
            return

        
        # Read the elements to be sorted
        with open('list.txt', 'r') as f:
            content = f.read().split(' ')
            for n in content:
                if n != '':
                    list_to_sort.append(int(n))

        # Sort the numbers and time each sorting method
        # Heap sort
        start_time = time.time()
        heap_sort(list_to_sort[:])
        elapsed_time = time.time() - start_time
        heap_sort_times.append(elapsed_time)

        # Merge sort
        start_time = time.time()
        merge_sort(list_to_sort[:])
        elapsed_time = time.time() - start_time
        merge_sort_times.append(elapsed_time)

        # Quick sort
        n = len(list_to_sort) - 1
        start_time = time.time()
        quick_sort(list_to_sort[:], 0, n)
        elapsed_time = time.time() - start_time
        quick_sort_times.append(elapsed_time)

        # Timsort
        n = len(list_to_sort) - 1
        start_time = time.time()
        tim_sort(list_to_sort, n)
        elapsed_time = time.time() - start_time
        tim_sort_times.append(elapsed_time)

        print('Test', i + 1)

    print('Heapsort average:', sum(heap_sort_times) / tests_count, 'seconds')
    print('Mergesort average:', sum(merge_sort_times) / tests_count, 'seconds')
    print('Quicksort average:', sum(quick_sort_times) / tests_count, 'seconds')
    print('Timsortsort average:', sum(tim_sort_times) / tests_count, 'seconds')


if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
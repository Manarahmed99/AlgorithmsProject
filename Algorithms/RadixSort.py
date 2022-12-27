# Radix sort 

# Using counting sort to sort the elements in the basis of significant places
def countingSort(array, place):
    #length of data 
    #O(1)
    size = len(array)
    
    #auxiliary array for assigning sorted data 
    #O(1)
    output = [0] * size
    
    #This array is used for storing the count of the elements in the array. 
    #O(1)
    count = [0] * 10

    # Calculate count of elements
    # digit position: ones / tens /hundred and so on
    #O(max)
    for i in range(0, size):
        index = array[i] // place   
        count[index % 10] += 1  

    # Calculate cumulative count
    #O(size)
    for i in range(1, 10):
        count[i] += count[i - 1]

    
    # Find the index of each element of the original array in count array
    # place the elements in output array
    
    #O(max)
    i = size - 1 #placing integers to it correcponding place in array in backward
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1 #decrease count by 1
        i -= 1 #deacrement by 1


    #filling original array with sorted data
     #O(size)
    for i in range(0, size):
        array[i] = output[i]
 

# Main function to implement radix sort
def radixSort(array):
        
    # Get maximum element in data
    ##O(1)
    max_element = max(array)

    # Apply counting sort to sort elements based on place value.
    #O(maxDigit)
    place = 1
    while max_element // place > 0:
        countingSort(array, place)
        place *= 10 #increasse the place by 10 each loop

# PSEUDO-CODE:
#
# for j = 2 to A.length
#     key=A[j]
#     ****insert key to sorted portion of the array,namely A[1,j-1]****
#     i=j-1
#     while i>0 and A[i]>key:
#         A[i+1]=A[i]
#         i=i-1
#     ***this loop switches element on i-th place one to the right and then we insert key to the openning position***
#     A[i+1] = key
#

def insertion_sort (array):
    for j in range(len(array)):
        key = array[j]
        i=j-1
        while i > 0 and array[i] > key :
            array[i+1] = array[i]
            i -= 1
        array[i+1 ] = key
    return array
array = [1,5,2,3,4]
insertion_sort(array)
print(array)

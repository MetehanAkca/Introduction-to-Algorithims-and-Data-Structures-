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


# exercise 1:demonstrate insertion sort of increasing order for array [31,41,59,26,41,58


def insertion_sort (array):
    for j in range(len(array)):
        key = array[j]
        i=j-1
        while i >= 0 and array[i] > key :
            array[i+1] = array[i]
            i -= 1
        array[i+1 ] = key
    return array
array = [31,41,59,26,41]
insertion_sort(array)
print(array)

# exercise 2:modify the algorithm to sort for decreasing order and demonstrate funcionality.
def insertion_sort_decreasing (array):
    for j in range(len(array)):
        key = array[j]
        i=j-1
        while i >= 0 and array[i] < key :
            array[i+1] = array[i]
            i -= 1
        array[i+1] =key
    return array

print(insertion_sort_decreasing(array))


# Consider the searching problem:
#     Input: a sequence of n numbers and a value ven
#     Output:an index i such than v=A[i] or NIL if such a number doesnt exist in sequence.
#   write the pseudo code for linear search.Proove corectness using loop invariant
"""
for i = 1 to A.len
    while A[i]<= v
       if A[i] ==v:
           return i
           break
    return NIL  
    
    PROOF:
    Consider two sub-arrays A[1..i] and A[i+1 .. n]
    Initiation: since array is a sequence all of it's elements are ordered hence so is the A[1..i] and A[i+1..n]
    Mainttanance: throughout the loop as i increases the next element of the sequence is transferred from sub-array A[i+1..n] to A[1..i]
    This step will not insert anything new thus not mess with the ordering.
    Termination:As the loop ends integrity of the initial sequence was not disrupted via any sort of replacement or insertion.As a result,
    loop invariance was satisified in all three steps.
     
"""


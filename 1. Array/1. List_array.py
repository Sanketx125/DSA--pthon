

# Array:
'''
    * Array is special type of data structure is can store more than 1 homogeneous values in single variable.
    * array has two types:  1. Static Array | 2. Dynamic array |

                1. Static array:
                                - array with fixed size
                                -
                2. Dynamic Array:
                                - array which can change there size as per requirement.
                                - every new insertion time array increase there size double.
                                - the pythons list is example of Dynamic array.
                

cons:
    * Fixed size
    * lack of Flexibility (only can store homogeneous values.)
    * 
'''
# python array module:
import array as ar


# creating integer array:
arr = ar.array('i', [1, 2, 3])

# float array:
arr2 = ar.array('f', [1.0, 2.0, 3.1, 4.5, 5.5])

# unicode value array:
arr3 = ar.array('u', [ 'a', 'b', 'c', 'd'])

print(arr)
print('lenth of array : ', len(arr))

# accessing elements in array:
for i in range(len(arr)):
    print( arr[i], end=" ")

print('\n----------------------------------------------')

# insert element in array:

arr.append(25)    # insert element last/end of the array
arr.insert( 0, 100)  # insert element in specified index here 100 value in insertig in index '0'

for i in range(len(arr)):
    print( arr[i], end=" ")

print('\n----------------------------------------------')

# deleting element in array:

arr.pop()  # delete last element in array we can also pass the index no. of element which we want to delete
for i in range(len(arr)):
    print( arr[i], end=" ")


print('\n----------------------------------------------')
# searching in array
l = [1, 2, 3, 4, 5, 6, 7]

myarr = ar.array('i', l)
# print array:
for i in range(len(myarr)):
    print( myarr[i], end="  ")

key = int(input("\nEnter value : "))

found = False
for i in range( len(myarr)):
    if (key == myarr[i]):
        print('index: ',i)
        found = True
        break

# If key is not found
if not found:
    print("value not present in array")


# sorting ascending order
print('\n----------------------------------------------')

def ascending(arr):

    sort_arr = arr.tolist()
    sort_arr.sort()
    display(sort_arr)

def display(arr):

    for i in range( len(arr)):
        print(arr[i], end=" ") 


ar1 = ar.array('i', [6,7,5,8,9,2,4,1,0])
ascending(ar1)

print('\n----------------------------------------------')

# sorting Descending order

def descending(arr):
    sort_list = arr.tolist()
    sort_list.sort(reverse = True)

    display(arr) # display function call

descending(ar1)


print('\n',type(ar1))
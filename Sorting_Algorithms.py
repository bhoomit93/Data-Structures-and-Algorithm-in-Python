"""
@author : Bhoomit Patel

"""
#Implementation of Selection Sort
def selection_sort(arr):

    #Traverse through all elements
    for i in range(len(arr)):
        min_idx = i

        #finding index of minimum element
        for j in range(i+1,len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx=j

        #Swapping the elements
        arr[i],arr[min_idx]=arr[min_idx],arr[i]
        print(i,"th iteration : ",arr)

#Driver Program

A=[50,11,48,95,32,75]

#Selection Sort Implementation
print("Selection Sort:")
selection_sort(A)
"""
sample output:
Selection Sort:
0 th iteration :  [11, 50, 48, 95, 32, 75]
1 th iteration :  [11, 32, 48, 95, 50, 75]
2 th iteration :  [11, 32, 48, 95, 50, 75]
3 th iteration :  [11, 32, 48, 50, 95, 75]
4 th iteration :  [11, 32, 48, 50, 75, 95]
5 th iteration :  [11, 32, 48, 50, 75, 95]
"""
# -*- coding: utf-8 -*-
# from __future__ import unicode_literals, division
'''
Sort by "shaker" method

5 4 3 2 1  (b=0 e=4)
1-st pass
4 5 3 2 1  
= =
4 3 5 2 1    
  = =
4 3 2 5 1
    = =
4 3 2 1 5  (b=0 e=3)
      = =
2-nd pass
4 3 1 2 5 
    = = 
4 1 3 2 5 
  = =  
1 4 3 2 5  (b=1 e=3)
= =   
'''

def shake_sorter(arr):
    # setting 1-st pass range
    left = 0
    right = len(arr) - 1
    pass_cnt = 0
    sorted_flag = True
    while not (left >= right):
        # ->
        i = left
        while i < right:
            pass_cnt += 1
            if arr[i] > arr[i+1]:
                sorted_flag = False
                _ = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = _
            i += 1
        if sorted_flag:
            break
        right -= 1
        # <-
        i = right
        while i > left:
            pass_cnt += 1            
            if arr[i] < arr[i-1]:
                sorted_flag = False
                _ = arr[i]
                arr[i] = arr[i-1]
                arr[i-1] = _
            i -= 1
        if sorted_flag:
            break
        left += 1
    print('Passes {}'.format(pass_cnt))
    return arr

if __name__ == '__main__':
    arr1 = [5,2,3,4,1]
    print(arr1)
    print(shake_sorter(arr1))
    arr2 = [5,2,2,4,1]
    print(arr2)
    print(shake_sorter(arr2))
    arr3 = [4,3,2,1]
    print(arr3)
    print(shake_sorter(arr3))
    arr4 = [1,2,3,4]
    print(arr4)
    print(shake_sorter(arr4))
    arr5 = [1,1,1,1,1]
    print(arr5)
    print(shake_sorter(arr5))



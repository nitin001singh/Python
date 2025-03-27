# '''
# * * * * 
# * * * * 
# * * * * 
# * * * *

# '''
# for x in range(4):
#     for y in range(4):
#         print('*', end=" ")
#     print()
    

# '''
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# '''

# for x in range(6):
#     for y in range(x):
#         print('*', end=" ")
#     print()
    


# '''
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 

# '''

# for x in range(1,6):
#     for y in range(1, x+1):
#         print(y, end=" ")
#     print()
    
    
# '''
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5 
# '''
# for x in range(1,6):
#     for y in range(1, x+1):
#         print(x, end=" ")
#     print()
# n = 5  

# '''
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 
# '''
# for x in range(5,0,-1):
#     for y in range(1, x+1):
#         print('*', end=" ")
#     print()
    
# n = 6
# for x in range(1,n):
#     for y in range(1, n-x+1):
#         print('*', end=" ")
#     print()


# '''
#     *    
#    ***   
#   *****  
#  ******* 
# *********

# '''

# n = 5
# for x in range(1,n+1):
#     for y in range(1, n+1-x):
#         print(" ", end="")
        
#     for z in range(1, 2*x):
#         print("*", end="")
        
#     for m in range(1, n+1-x):
#         print(" ", end="")
#     print()


'''
***************
 ************* 
  ***********  
   *********   
    *******    
     *****     
      ***      
       *  

'''


# n = 9
# for x in range(1,n+1):
#     for y in range(1, x):
#         print(" ", end="")
        
#     for z in range(1, 2*n - 2*x):
#         print("*", end="")
        
#     for m in range(1, x):
#         print(" ", end="")
#     print()


'''
    *    
   ***   
  *****  
 ******* 
*********
 ******* 
  *****  
   ***   
    * 

'''


# n = 5

# for x in range(1,n+1):
#     for y in range(1, n+1-x):
#         print(" ", end="")
        
#     for z in range(1, 2*x):
#         print("*", end="")
        
#     for m in range(1, n+1-x):
#         print(" ", end="")
#     print()
    
    
# for k in range(1,n+1):
#     for y in range(k):
#         print(" ", end="")
        
#     for z in range(1, 2*n - 2*k):
#         print("*", end="")
        
#     for m in range(k):
#         print(" ", end="")
#     print()


# '''
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

# '''

# n = 5
# for x in range(1,n+1):
#     for y in range(x):
#         print('*', end="")
#     print()
    
# for x in range(n-1, 0, -1):
#     for y in range(x):
#         print('*', end="")
#     print()


# n = 5
# for x in range(1,2*n):
#     for y in range(2*n - x if x > n else x):
#         print('*', end="")
#     print()




# '''
# 0
# 10
# 010
# 1010
# 01010

# '''

# n = 5
# for x in range(1,n+1):
#     start = 1 if x%2 == 0 else 0
#     for y in range(x):
#         print(start, end="")
#         start = 1-start
#     print()


# '''
# 1        1
# 12      21
# 123    321
# 1234  4321
# 1234554321

# '''
# n = 5
# for x in range(1,n+1):
#     for y in range(1,x+1):
#         print(y, end="")
    
#     for k in range(2*n - 2*x):
#         print(' ', end="")
    
    
#     for z in range(1,x+1):
#         print(x+1-z, end="")
#     print()

# '''
# 1
# 23
# 456
# 78910
# 1112131415
# '''
# n = 5
# num = 1
# for x in range(1, n+1):
#     for y in range(x):
#         print(num, end="")
#         num += 1
#     print()


# '''
# A
# AB
# ABC
# ABCD
# ABCDE

# '''

# n = 5
# for x in range(1, n+1):
#     num = ord('A')
#     for y in range(x):
#         print(chr(num), end="")
#         num += 1
#     print()

# n = 5
# for x in range(1, n+1):
#     for y in range(ord('A'), ord('A') + x):
#         print(chr(y), end="")
#     print()


# '''
# ABCDEF
# ABCDE
# ABCD
# ABC
# AB
# A
# '''

# n = 5
# for x in range(n+1 , 0 , -1):
#     num = ord('A')
#     for y in range(x):
#         print(chr(num), end="")
#         num += 1
#     print()

# n = 5
# for x in range(n+1, 0, -1):
#     for y in range(ord('A'), ord('A') + x):
#         print(chr(y), end="")
#     print()


# '''
# A
# BB
# CCC
# DDDD
# EEEEE

# '''

# n = 5
# num = ord('A')
# for x in range(1, n+1):
#     for y in range(x):
#         print(chr(num), end="")
        
#     num += 1
#     print()



# n = 5
# for i in range(0, n):
#     letter = chr(ord('A') + i)
#     print(letter * (i+1))
    
    
    
# '''

#         A         
#       A B A       
#     A B C B A     
#   A B C D C B A   
# A B C D E D C B A

# '''
    
# n = 5

# for x in range(1,n+1):
#     for y in range(1, n+1-x):
#         print(" ", end=" ")
        
#     num = ord('A')
#     for z in range(1, 2*x):
#         print(chr(num), end=" ") 
#         if (2*x / 2) > z:
#             num += 1
#         else:
#             num -= 1
        
#     for m in range(1, n+1-x):
#         print(" ", end=" ")
#     print()


# '''
# H 
# G H 
# F G H 
# E F G H 
# D E F G H 
# C D E F G H 
# B C D E F G H 
# A B C D E F G H

# '''


# n = 8
# num = ord('A') + n
# for x in range(1,n+1):
#     for y in range(num - x, num):
#         print(chr(y), end=" ")
#     print()

'''
* * * * * * * * * * 
* * * *     * * * * 
* * *         * * * 
* *             * * 
*                 * 
*                 * 
* *             * * 
* * *         * * * 
* * * *     * * * * 
* * * * * * * * * * 

'''

# n = 5
# for x in range(n):
#     for y in range(n-x, 0, -1):
#         print('*', end=" ")
        
#     for y in range(2*x):
#         print(' ', end=" ")
        
#     for y in range(n-x, 0, -1):
#         print('*', end=" ")
#     print()
    
# for x in range(1,n+1):
#     for y in range(x):
#         print('*', end=" ")
        
#     for y in range(2*n - 2*x):
#         print(' ', end=" ")
        
#     for y in range(x):
#         print('*', end=" ")
#     print()


# '''
# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *


# '''

# n = 5
# for x in range(1,n+1):
#     for y in range(x):
#         print('*', end="")
        
#     for y in range(2*n-2*x):
#         print(' ', end="")
        
#     for y in range(x):
#         print('*', end="")
#     print()
    
# for x in range(1,n+1):
#     for y in range(n-x):
#         print('*', end="")
        
#     for y in range(2*x):
#         print(' ', end="")
        
#     for y in range(n-x):
#         print('*', end="")
#     print()


# '''
# ******
# *    *
# *    *
# *    *
# *    *
# ******

# '''
# n = 6
# for x in range(n):
#     for y in range(n):
#         # print(x, y)
#         if (x==0 or x == n-1)  or  ( y==0 or y==n-1 ):
#             print('*', end="")
#         else:
#             print(' ', end="")
#     print()


'''
4 4 4 4 4 4 4 
4 3 3 3 3 3 4 
4 3 2 2 2 3 4 
4 3 2 1 2 3 4 
4 3 2 2 2 3 4 
4 3 3 3 3 3 4 
4 4 4 4 4 4 4 

'''

# n = 4
# for x in range(2*n-1):
#     for y in range(2*n-1):
#         top = x
#         left = y
#         right = 2*n-2 - y
#         down = 2*n - 2 - x    
        
#         print( n - min( min(top, down) , min(right, left)  ) , end=" ")
#     print()
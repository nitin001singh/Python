
import math
n = int(math.log10(1852852) + 1 )
print(n)

import unittest

def sum(a, b):
    return a+b
def sub(a, b):
    return a-b
def mul(a, b):
    return a*b
def divi(a, b):
    return a/b

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.a = 10
        self.b = 20

    def tearDown(self):
        self.a = 0
        self.b = 0
        print("Test Case completed")

    def testSum(self):
        result = sum(self.a, self.b)
        self.assertEqual(result, self.a + self.b)

    def testSub(self):
        result = sub(self.a, self.b)
        self.assertEqual(result, self.a - self.b)

    def testMul(self):
        result = mul(self.a, self.b)
        self.assertEqual(result, self.a * self.b)

    def testDiv(self):
        result = divi(self.a, self.b)
        self.assertEqual(result, self.a / self.b)


if __name__ == "__main__":
    unittest.main()





# import threading
# import time
#
# condition = threading.Condition()
# turn = "odd"  # To track whose turn it is
#
# def showOdd():
#     global turn
#     for x in range(1, 11, 2):  # Odd numbers from 1 to 9
#         with condition:
#             while turn != "odd":  # Wait if it's not the odd number's turn
#                 condition.wait()
#             print(f"Odd number is {x}")
#             time.sleep(1)
#             turn = "even"  # Switch to even
#             condition.notify()  # Notify the even number thread
#
# def showEven():
#     global turn
#     for x in range(2, 11, 2):  # Even numbers from 2 to 10
#         with condition:
#             while turn != "even":  # Wait if it's not the even number's turn
#                 condition.wait()
#             print(f"Even number is {x}")
#             time.sleep(1)
#             turn = "odd"  # Switch to odd
#             condition.notify()  # Notify the odd number thread
#
# t1 = threading.Thread(target=showOdd)
# t2 = threading.Thread(target=showEven)
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()
#
# print('Thread success')



# import threading
# import time
#
# lock = threading.Lock()
#
# def showEven(lock):
#     with lock:
#         for x in range(11):
#             time.sleep(1)
#             if x % 2 == 0:
#                 print("Even number is " + str(x))
#
# def showOdd(lock):
#     with lock:
#         for x in range(11):
#             time.sleep(1)
#             if x % 2 != 0:
#                 print("Odd number is " + str(x))
#
# t1 = threading.Thread(target=showOdd, args=(lock,))
# t2 = threading.Thread(target=showEven, args=(lock,))
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()
#
# print('Thread success')




# from threading import Thread
# import time
#
# class MyThread(Thread):
#     def __init__(self, name, args):
#         super().__init__(name=name, args=args)
#         print(args)
#         print(name)
#
#     def run(self):
#         print("Thread is running", end="\n")
#         time.sleep(5)
#         for x in range(11):
#             print(x)
#         print("Thread is exiting", end="\n")
#
#
# t1 = MyThread( name = "Nitin Thread", args=("Nitin",34))
# t1.start()
# t1.is_alive()
# print(t1.name, end="\n")
#
# print(t1.ident, end="\n")
# t1.join()
#
# print("Thread success")
# print(t1.ident, end="\n")

# import multiprocessing
#
#
# def showNumber():
#     for x in range(11):
#         print(x)
#
#
# p1 = multiprocessing.Process(target=showNumber)
# p1.start()
# p1.join()
# p1.terminate()
# p1.close()
# print('Process success')

#
# import threading
# import time
# lock = threading.Lock()
#
# def showEven(lock):
#     lock.acquire()
#
#     for x in range(11):
#         time.sleep(1)
#         if x % 2 == 0:
#             print("Even number is " + str(x))
#     lock.release()
#
#
# def showOdd(lock):
#     lock.acquire()
#
#     for x in range(11):
#         time.sleep(1)
#         if x % 2 != 0:
#             print("Odd number is " + str(x))
#     lock.release()
#
#
#
# t1 = threading.Thread(target=showOdd, args=(lock, ))
# print(threading.active_count())
# t2 = threading.Thread(target=showEven, args=(lock, ))
# print(threading.active_count())
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()
#
# print('Thread success')




# feed = input().split(' ')
# data = []
# for x in range(len(feed) + 1):
#     data.append((input().split(' ')))
#
# max_val = 0
# for m in data:
#     max_val += max(list( map(int, m))) ** 2
#
# print(max_val % int(feed[1]))
# n = 6
# for x in range(n):
#     for y in range(x):
#         print('*', end="")
#     print()
# for m in range(n, 0, -1):
#     for n in range(0, m):
#         print('*', end="")
#     print()

#
# test_cases = int(input(""))
# data = []
# for x in range(test_cases):
#     val = input("")
#     data.append( ( val.split(' ') ) )
#
# try:
#     for y in data:
#         print( int(y[0]) / int(y[1])  , end="\n")
#
# except ZeroDivisionError as ze:
#     print(ze)


# c = 32
# f = c * (9/5)+32
# print(f)


#
# n = 1203045
# rev = 0
# while n > 0:
#     remainder = n % 10
#     rev = rev * 10 + remainder
#     n = n // 10
#
# print(rev)






# l = [10,2,52,15,98,75,150,27,0,65,48]
# max = l[0]
# for x in l:
#     if x >= max:
#         max = x
#
# print(max)




# def power(a,b):
#     if b == 0:
#         return 1
#     else :
#         return  (a * power( a , b-1))
#
# res = power(2,3)
# print(res)


# def print_rangoli(size):
#     # your code goes here
#     for i in range(size):
#         s = "-".join(chr(ord('a')+size-j-1) for j in range(i+1))
#         # print(s+s[::-1][1:].center(4*size-3, "-"))
#         print((s+s[::-1][1:]).center(4*size-3, "-"))
#     for i in range(size-1):
#         s = "-".join(chr(ord('a')+size-j-1) for j in range(size-i-1))
#         print((s+s[::-1][1:]).center(4*size-3, "-"))
#
# if __name__ == '__main__':
#     n = int(input())
#     print_rangoli(n)
#



# import math
# class Points(object):
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def __sub__(self, no):
#         return Points(self.x - no.x,
#                       self.y - no.y,
#                       self.z - no.z)
#
#     def dot(self, no):
#         return self.x * no.x + self.y * no.y + self.z * no.z
#
#     def cross(self, no):
#         return Points(self.y * no.z - self.z * no.y,
#                       self.z * no.x - self.x * no.z,
#                       self.x * no.y - self.y * no.x)
#
#     def absolute(self):
#         return math.sqrt((self.x ** 2 + self.y ** 2 + self.z ** 2))
#
# if __name__ == '__main__':
#     points = list()
#     for i in range(4):
#         a = list(map(float, input().split()))
#         points.append(a)
#
#     a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
#     x = (b - a).cross(c - b)
#     y = (c - b).cross(d - c)
#     angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))
#
#     print("%.2f" % math.degrees(angle))

# print(*[1,2,3])

# dict1 = {"a": 1, "b": 2}
# dict2 = {"c": 3, "d": 4}
# merged = {**dict1, **dict2}
# print(merged)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}


# import math
#
#
# class Complex(object):
#     def __init__(self, real, imaginary):
#         self.real, self.imaginary = real, imaginary
#
#     def __add__(self, no):
#         real = self.real + no.real
#         imag = self.imaginary + no.imaginary
#         return __class__(real, imag)
#
#     def __sub__(self, no):
#         real = self.real - no.real
#         imag = self.imaginary - no.imaginary
#         return __class__(real, imag)
#
#     def __mul__(self, no):
#         real = self.real * no.real - self.imaginary * no.imaginary
#         imag = self.real * no.imaginary + no.real * self.imaginary
#         return __class__(real, imag)
#
#     def __truediv__(self, no):
#         real = self.real * no.real + self.imaginary * no.imaginary
#         real /= pow(no.real, 2) + pow(no.imaginary, 2)
#         imag = self.imaginary * no.real - self.real * no.imaginary
#         imag /= pow(no.real, 2) + pow(no.imaginary, 2)
#         return __class__(real, imag)
#
#     def mod(self):
#         real = math.sqrt(pow(self.real, 2) + pow(self.imaginary, 2))
#         imag = 0.00
#         return __class__(real, imag)
#
#     def __str__(self):
#         if self.imaginary == 0:
#             result = "%.2f+0.00i" % (self.real)
#         elif self.real == 0:
#             if self.imaginary >= 0:
#                 result = "0.00+%.2fi" % (self.imaginary)
#             else:
#                 result = "0.00-%.2fi" % (abs(self.imaginary))
#         elif self.imaginary > 0:
#             result = "%.2f+%.2fi" % (self.real, self.imaginary)
#         else:
#             result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
#         return result
#
#
# if __name__ == '__main__':
#     c = map(float, input().split())
#     d = map(float, input().split())
#     x = Complex(*c)
#     y = Complex(*d)
#     print(*map(str, [x + y, x - y, x * y, x / y, x.mod(), y.mod()]), sep='\n')
#








#
# from collections import Counter
#
#
# N = int(input())
# count = Counter(map(int, input().split()))
# # print(count)
# print(next(k for k, v in count.items() if v != N))


# grp_size = 5
# rooms_no =  [1, 2, 3, 6, 5, 4, 4, 2, 5, 3, 6, 1, 6, 5, 3, 2, 4, 1, 2, 5, 1, 4, 3, 6, 8, 4, 3, 1, 5, 6, 2]
#
# d = {}
# for x in rooms_no:
#     if x in d:
#         d[x] += 1
#     else:
#         d[x] = 1

# print( "".join( [ str(room) for room, x in d.items() if x != grp_size ] ))

# captain_room = 0
# for room, grp_size in d.items():
#     if grp_size == 1:
#         print("Captain Room number is ", room)
#         break


#
#
# from itertools import combinations as cm
# n = int(input())
# s = list(input().split(" "))
# k = int(input())
# l=["".join(word) for word in list(cm(s,k))]
# print(l)
# x,y=0,len(l)
# for word in l:
#     x+=1 if 'a' in word else 0
# print(x/y)



# def print_rangoli(size):
#     # your code goes here
#     for i in range(size):
#         s = "-".join(chr(ord('a')+size-j-1) for j in range(i+1))
#         # print(s+s[::-1][1:].center(4*size-3, "-"))
#         print((s+s[::-1][1:]).center(4*size-3, "-"))
#     for i in range(size-1):
#         s = "-".join(chr(ord('a')+size-j-1) for j in range(size-i-1))
#         print((s+s[::-1][1:]).center(4*size-3, "-"))
#
# if __name__ == '__main__':
#     n = int(input())
#     print_rangoli(n)



# val = """4
# bcdef
# abcdefg
# bcde
# bcdef"""
#
# print(val.split("\n"))
# uw = []
# d = {}
# input_arr = val.split("\n")
# for x in input_arr:
#     if x.isalpha():
#         uw.append(x)
#         if x in d:
#             d[x] += 1
#         else:
#             d[x] = 1
# print(len(set(uw)))
# print(" ".join(list(map(str, d.values()))))



# s = "1122233334555"
# d = {}
# t = []
# for x in s:
#     if x in t:
#         d[x] += 1
#     else:
#         d[x] = 1
#         t.append(x)
#
# res = " ". join(list(map(str, list(d.items()))))
# print(res)
# # print(t)






# l1 = [2, 7, 5, 64, 14]
# even = [ x for x in l1 if x % 2 == 0]
#
# print("Even ", len(even))
# print("Odds ", len(l1) - len(even))
# from datetime import datetime
# import pytz
# UTC = pytz.utc
# IST = pytz.timezone('Asia/Kolkata')
# print("UTC in Default Format : ", datetime.now(UTC))
# print("IST in Default Format : ", datetime.now(IST))
#
# datetime_utc = datetime.now(UTC)
# print("Date & Time in UTC : ", datetime_utc.strftime('%Y:%m:%d %H:%M:%S %Z %z'))
# datetime_ist = datetime.now(IST)
# print("Date & Time in IST : ", datetime_ist.strftime('%Y:%m:%d %H:%M:%S %Z %z'))

# class Student:
#
#     def __init__(self, name, roll_no, m1, m2):
#         self.__name = name
#         self.__roll_no = roll_no
#         self.__m1 = m1
#         self.__m2 = m2
#
#     def accept(self , name, roll_no, m1, m2):
#         obj = Student(name, roll_no, m1, m2)
#         ls.append(obj)
#
#     @staticmethod
#     def display():
#         print("List of Students \n")
#         for x in ls:
#             print("Name is {}".format(x.__name))
#             print("Roll Number is {}".format(x.__roll_no))
#             print("Marks 1 is {}".format(x.__m1))
#             print("Marks 2 is {}".format(x.__m2))
#             print('-'*30)
#         else:
#             print("No record found")
#
#     def search(self, roll_no):
#         print("Searching.... \n")
#         for x in ls:
#             if int(roll_no) == int(x.__roll_no):
#                 print("Name is {}".format(x.__name))
#                 print("Roll Number is {}".format(x.__roll_no))
#                 print("Marks 1 is {}".format(x.__m1))
#                 print("Marks 2 is {}".format(x.__m2))
#                 break
#         else:
#             print("No Record found")
#
#     def delete(self, roll_no):
#         for index, x in enumerate(ls):
#             if int(roll_no) == int(x.__roll_no):
#                 del ls[index]
#                 break
#         print("Student has been deleted \n")
#
#     def update(self, old_roll_no, new_roll_no):
#         for index, x in enumerate(ls):
#             if int(old_roll_no) == int(x.__roll_no):
#                 ls[index].__roll_no = new_roll_no
#                 break
#         print("Student roll number has been updated \n")
#
#
# ls = []
# obj1 = Student("",0,0,0)
# obj1.accept("Nitin","1234",80,90)
# obj1.accept("Ankit","4521",90,70)
# # Student.display()
# obj1.update(4521,100)
# # obj1.search(1234)
# obj1.delete(100)
# Student.display()
# obj1.search(1234)

# print(ls)
# def breakingRecords(n,score):
#
#     max = score[0]
#     min = score[0]
#     min_counter = 0
#     max_counter = 0
#     for x in range(n):
#         if score[x] > max:
#             max_counter += 1
#             max = score[x]
#             # print(max_counter, max)
#
#         if score[x] < min:
#             min_counter += 1
#             min = score[x]
#
#         # print(score[x], max)
#
#     return list(map(str, [max_counter , min_counter]))
#
#
# res = breakingRecords(9, [10,5,20,20,4,6,2,25,1])
# print(" ".join(res))



# import Demo.app as da
# res= da.mul(2,5)
# print(res)
#


# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def display(self):
#         return self.name
#
# # obj1 = Person("Nitin")
# # print(obj1.display())
#
# import pickle
# # with open("demo.pkl", "wb") as f2:
# #     pickle.dump(Person, f2)
#
# with open("demo.pkl", "rb") as f2:
#     response = pickle.load(f2)('Anil')
#     print("Pickle loading..")
#     print(response.display())
#




# import json
# with open("demo.json", "w") as f:
#     json.dump([1,2,3],f)
#
#
# with open("demo.json", "r") as f1:
#     res = json.load(f1)
#     print(res, type(res))

#
# def double(func):
#     def wrapper(*args, **kw):
#         return sum(args) * 2
#     return wrapper
#
#
# @double
# def add1(a,b):
#     return a+b
#
# def add2(a,b):
#     return a+b
#
# a = add1
# b = add2
# print(a(2,3))
# print(b(2,3))
#
# assert a(2,3) == b(2,3)*2, "Values are matching"
# print("Values are matching")
# print(res)
# def double(func):
#     def wrapper(*args, **kw):
#         return [func(*args, **kw), func(*args, **kw)]
#     return wrapper
#
#
# @double
# def hello(string):
#     print(string)

# on calling after specified decorator is inplaced
# hello('hello')
#
# def printer(func):
#     def wrapper():
#         res = func()
#         if res:
#             return func()
#         else:
#             pass
#     return wrapper
#
#
#
# def hi():
#     print("Hello")
# abc = printer(hi)
# print(abc())
# def make_bold(func):
#     def wrapper():
#         return "<b>"+func()+"</b>"
#     return wrapper
#
# def make_italic(func):
#     def wrapper():
#         return "<i>"+func()+"</i>"
#     return wrapper
#
# def make_underline(func):
#     def wrapper():
#         return "<u>"+func()+"</u>"
#     return wrapper
#
# def hello():
#     return "hello world"
#
# bold= make_bold(hello)
# print(bold())
# italic= make_italic(hello)
# print(italic())
# underline= make_underline(hello)
# print(underline())
#
# print('---'*30)
# @make_bold
# @make_italic
# @make_underline
# def hello_new():
#     return "hello world Program"
#
# b = hello_new
# print(b())


# import time
# def elapsed_since(data):
#     last_time = time.perf_counter()
#     for item in data:
#         current_time = time.perf_counter()
#         delta = current_time - last_time
#         last_time = current_time
#         yield (delta, item)
#
# for t in elapsed_since('abcd'):
#     print(t)
#     time.sleep(2)
#
# import time
# def counter_Table(data):
#     for x in range(1,11):
#         yield(data*x)
#
# for t in counter_Table(2):
#     print(t)
#     time.sleep(2)



# class Circle:
#     def __init__(self, data, number):
#         self.data = data
#         self.number = number
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index >= self.number:
#             raise StopIteration
#         print(self.index , len(self.data), (self.index % len(self.data)))
#         value = self.data[self.index % len(self.data)]
#         self.index += 1
#         return value
#
#
# c = Circle('abc', 5)
# d = Circle('abc', 7)
# print(list(c))
# print(list(d))


# class MyEnumerate:
#     def __init__(self, data):
#         self.data = data
#         self.index = 0
#
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.index == len(self.data):
#             raise StopIteration
#         value = (self.index, self.data[self.index])
#         self.index += 1
#         return value
#
# for i,x in MyEnumerate("nitin"):
#     print(i,":",x)


# counter = 0
# def gcd(a,b):
#     global counter
#     counter += 1
#     if a == b:
#         return a
#     elif a > b:
#         return gcd(a-b, b)
#     else:
#         return gcd(b-a, a)
#
# res = gcd(5,10)
# print(res, counter)

# class Person:
#     def __init__(self, name ,state,city, age):
#         self.name = name
#         self.state = state
#         self.__city = city
#         self.__age = age
#
#     def address(self):
#         return "{}, {}, {}".format(self.name, self.__city, self.state)
#
#
# obj1 = Person("Nitin", "Jaipur", "Rajasthan",33)
# print(obj1.address())
# print(Person.__dict__)
# print(obj1.__dict__)
# class StopIteration(Exception):
#     def __init__(self, msg):
#         self.__msg = msg
#         self.display()
#
#     def display(self):
#         return self.__msg
#
# i = 1
# while True:
#     try:
#         if i > 20:
#             raise StopIteration(" Max number limit has reached")
#         print(i, end=" ")
#         i += 1
#     except StopIteration as si :
#         print(si)
#         break


# class InvalidAge(Exception):
#     def __init__(self, msg):
#         self.__msg = msg
#         self.display()
#
#     def display(self):
#         return self.__msg
#
# class InvalidName(Exception):
#     def __init__(self, msg):
#         self.__msg = msg
#         self.display()
#
#     def display(self):
#         return self.__msg
#
# try:
#     name = input("Enter name ")
#     age = int(input("Enter age "))
#     if age < 18:
#         raise InvalidAge("Invalid age")
#     elif len(name.split(" "))  < 2:
#         raise InvalidName("Invalid Name")
# except InvalidAge as ia:
#     print(ia)
# except InvalidName as ina:
#     print(ina)
#
# else:
#     print("Vote done")




# class GuessError(Exception):
#     def __init__(self, msg):
#         self.__msg = msg
#         self.display()
#
#     def display(self):
#         return self.__msg
#
# class ValueTooLarge(Exception):
#     def __init__(self, msg):
#         self.__msg = msg
#         self.display()
#
#     def display(self):
#         return self.__msg
#
# class ValueTooSmall(Exception):
#     def __init__(self, msg):
#         self.__msg = msg
#         self.display()
#
#     def display(self):
#         return self.__msg
# guess = 10
# while True:
#     try:
#         value = int(input("Enter a number "))
#         if value == guess:
#             print("Correct answer !!!")
#             break
#         elif value < 1:
#             raise GuessError("Value can not be negative")
#         elif value > guess:
#             raise ValueTooLarge("Value is greater than the guessed number")
#         elif value < guess:
#             raise ValueTooSmall("Value is smaller than the guessed number")
#
#     except ValueTooSmall as e:
#         print(str(e))
#
#     except ValueTooLarge as e:
#         print(str(e))
#
#     except GuessError as e:
#         print(str(e))
# try:
#     with open("demo.txt", "w") as f:
#         f.write("Hello, Good Morning !!!")
#
# except IOError as io:
#     print(str(io))
# except Exception as e:
#     print(str(e))
# else :
#     print("File has successfully written")
#


# try :
#     l = [{0:2},2,3,4,'5', {5:10}, "15", {10:50}]
#     # For calculating sum of above list
#     s=0
#     for i in range(len(l)):
#         #You can Edit code from here
#         s += l[i].get(i)
#         s += l[i]
#         s += int(l[i])
#
# except TypeError as te:
#     print(str(te))
# except Exception as e:
#     print(str(e))
# finally:
#     print(s)
#
# def function(l: list, s, **args):
#     try:
#         last_element = l[-1]
#
#         l[int(s)]=10
#         any_element = l[int(s)+10]
#         l[s]=10
#
#         res = sum(l)
#
#         p = args['p']
#         # print(p)
#         return res/last_element * p + any_element
#
#     except IndexError as ie:
#         return str(ie)
#
#     except ValueError as ve:
#         return ve
#
#     except TypeError as te:
#         return te
#     except KeyError as ke:
#         return "Unknown key " + str(ke)
#
#     except ZeroDivisionError as ze:
#         return str(ze)
#
#     else:
#         print("Result is ", res)
#     finally:
#         print("End program")
#
# # res = function([1,2,1], 12)
# # res = function([1,2,1]*9, '1-2')
# # res = function([1,'2',1]*9, 12)
# # res = function([1,'2',1]*9, 12)
# # res = function([1,2,0]*9, 12  )
# res = function([1,2,1]*9, 12, p=None)
# # res = function([1,2,0]*9, 12, p=10)
#
# print(res)




# def get_final_line(filename):
#     lastline = ""
#     for f in open(filename,"r"):
#         lastline = f
#     return lastline
#
# response = get_final_line("demo.txt")
# print(response)

# vowels = ['a','e','i','o','u']
# v_dict = {i:0 for i in vowels}
# for line in open("demo.txt", "r"):
#     for x in line:
#         if x in v_dict:
#             v_dict[x] += 1
#
# print(v_dict)


# with open("demo.txt", "w") as f:
#     for x in range(1,20,2):
#         data = str(x) + '\t\t' + str(x+1) + "\n"
#         f.writelines(data)
#
# opt = ""
# total_sum = 0
# for i in  open("demo.txt", "r") :
#     line = i.strip().split("\t\t")
#     opt += line[0] +  '\t\t' + line[1] + '\t\t' + str(int(line[0]) * int(line[1] )) + "\n"
#     total_sum += int(line[0]) * int(line[1] )
#     # print(opt)
# opt += "Total" + "\t\t\t" + str(total_sum)
# print(opt)


# def generateFile(infile, outfile):
#     data = []
#     with open(infile, "r") as f:
#         data = f.read().split("\n")
#
#     with open(outfile, "w") as f1:
#         for x in data:
#             f1.write(x[::-1] + "\n")
#
# resp = generateFile("demo.txt", "opt.txt")


# word_list = ['alice', 'wonder', 'natural',"her"]
# countdict = {x:0 for x in word_list }
# # print(countdict)
# with open("demo.txt", "r") as f:
#     while True:
#         line = f.readline()
#         if not line :
#             break
#
#         line = line.replace("\n","").replace("'","").replace(".","").replace("?","").replace("(","").replace(")","").replace(",","").replace(";","").split(" ")
#         print(line)
#         for x in line :
#             if x.lower() in countdict:
#                 print(x.lower())
#                 countdict[x.lower()] += 1
#
# print("Countdict", countdict)

# val = "abcd323"
#
# def recursion(arg):
#     if arg == "":
#         return 0
#     else:
#         return 1 + recursion(arg[1:])

# res = recursion(val)
# print(res)






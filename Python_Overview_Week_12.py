#%%

name = 'dude'

#f string

print(f'hey, {name}')

#format()

print('hey, {}'.format(name))

print('hey, {a}'.format(a=name))

#print('hey, {1}'.format(1=name))


# %%
'''
escape characters

\\ backslash
\' single quote
\" double quote
\n new line
\t tab
'''

print("ssup? \n \"dude\" \\ \t dudette")


# %%
'''
import methods

import math (everything)

from math import * (entire contents of math library)

from math import pi
(only variable from math library)

import calendar as cal
(import the library and is accessed as cal)

from calendar import month as m
(import only month from calendar and accessed as m)
'''
# %%
'''
Conditionals

if

if-elif

if-elif-else

same can be written in a single line as shown below:
print('a is greater than b' if a>b else 'a is less than b' if a<b else 'a and b are equal')

'''

# %%
'''
Loops

While using some conditional

for using either range or without using range and over some iterable item

Nested loop, all these three kinds of loops can be used inside
one another, and this structure is referred to as nested loops/iterations

Loop control statements: break, continue and pass

range(start, stop, step):
start: it is optional and default value is 0
end: position to stop (non-inclusive) and mandatory
step: steps to take

'''
# %%
'''

In-built functions:

print() - prints arguments on the console
input() - takes input from the console as a string
type() - returns the type of an object
len() - returns the length of an object
max() - return the largest value in the iterable
min() - reuturn the smallest value in the iterable
sum() - sums the elements in an iterator
sorted() - returns the sorted list
iter() - returns an iterator object
next() - returns the next element in the iterator object
enumerate() - enumerates by adding counter to an iterable
zip() -  returns an iterator after coupling two or more iterator
map() - returns the iterator after applying specific function on each element in it
filter() - returns an iterator after applying specific filtering function

'''

print('z'>'Z') #alphabetical order holds and lower case> upper

print(sum({1,2,2,2,2,3})) #only non repeated considered in the set

s = iter('abcdef') #creating iter object

for item in s:
    print(item)

#can also be accessed as next(s) each element

t = iter('ab')

print(next(t))
print(next(t))
try:
    print(next(t)) # throws error because only two possible
except StopIteration: #exception is handled here
    print('next exceeds the iter object length')

a = enumerate('abc')
#print(list(a))
#print(set(a))#can be converted to set of tuples
print(dict(a))#can be converted to dict with keys
b = enumerate (['abc','bcd','cde'],1) #second argument gives the starting index
#print(list(b))
print(set(b))


#zip, no of elements of zip will be same as len of smallest iterable
A = [1,2,3]
B = ['a','b','c','d']
C = ['A','B','C']
D = 'hey'
E = {4,5,6,7,8} #even a set can be part, items added in sequence
F = {'lol':'laugh?','naa':'no no','oops':'akward much?'} #keys are taken from a dictionary not values
G = zip(A,B,C,D,E,F) #no.of elements in zip is the len of smallest iterable

#print(G[0]), zip object cannot be indexed directly
#print(len(G)), len() is not applicable for zip function
print(list(G))

#map

I = list(map(lambda x,y,z=3: x*y*z, A, A))
#here funciton is x*y*z with a default vaule of 3 for z, so minimum two ro max three arguments can be taken
#same as zip, len of smallest 
print(I)

#filter, filters an iter based on certain funtion

J = [25,36,-81,-100,4]

print(list(map(lambda x: x**0.5,J))) #negative numbers will result in complex answers, square root form math library won't take negatives

print(list(map(lambda x: x**0.5, filter(lambda x: x>0,J))))
#this will filter only the positive numbers

# %%

'''
User defined funcitons

- Positional arguments: sequence of definition
- keyword arguments: parameter given explicity, sequence won't matter
- Default arguments: some default value is given to certain paramentes and considered if no parameter is provided for that argument

'''

def mapping(x,y,z):
    return x-y-z
result = mapping (10,20,30) #positionally considered for x,y,z

def mapping (z,x,y):
    return x-y-z
result = mapping(x=10,y=20,z=30)
#both reults will be same, arguments and parameters are defined accordingly

def mapping (z, y=20, x =10): #default values in the end, non-default cannot follow a default value
    return x-y-z
result = mapping(30)
#now min of one and max of three parameters can be defined here
# %%

'''
Collections in python

List, Tuple, Dictionary, Set

(note that Dictionaries have been modified to maintain insertion order with the release of Python 3.7, so they are now ordered collection of data values.)

in the sequence shown above
Notation: [],(),{'key':'value'},{}
creation: list(), tuple(), dict(),set()
mutability: only tuple is immutable, i.e. cannot be modified once assigned
types of elements: Any, Any, keys: Hashable values: any, Hashable
order: expect set all are ordered in python 3.7 and above
duplicate: duplicate keys not allowed in dictionary, duplicates not allowed in set
operations: list: add/update/delete, tuples: no operations, dict; keys: add/del ; values: add/update/del, sets: add/del
Operations: list: index/slice/iterate, tuple: index/slice/iterate, dict: iteration, set: iteration
sorting: not possible in tuples and sets


NOTE on Hashable:
(keys can’t be repeated and must be immutable and hashable,
mapping in dictionaries is based on key lookup

An object is hashable if it has a hash value which never changes during its lifetime
object.__hash__() can be used to access hash values

list not hashable, but tuples are if each element within the tuple is hashable, hashable tuple can be used as a dictionary key

{(1,2,3): [10,20,30]} valid, {(1,[2]): [10,20,30]} invalid)
'''
# %%

'''
recursive function: A function which calls itself
important to have a well defined base case
'''
def fact(n):
    if n==1: #base case
        return 1
    else:
        return n*fact(n-1) #recursion
print(fact(5))
# %%

'''
lambda function
An anonymous funciton which can be assigned to a variable and called
single expression and simple functions only
'''
z = lambda a,b,c,d=4: a*b*c-d #can have any number of arguments and both default and notdefault values

print(z(1,2,3)) #defalut value of d is taken here as the fourth parameter
# %%

'''
List comprehension, optimized way to create lists in a single line
'''
example = [x**2 for x in range(1,11,2)] #squares of odd numbers between 1 to 10 
print(example)

testcase = [1,2,3,-4,-3,-10]
example = [x for x in testcase if x>0] #conditional and looping, taking out positive numbers into a list
print(example)

example = [x*x for x in testcase] #simple looping and creation of list
print(example)
# %%

'''
exception handling:
--> different from sytax errors, while writing a program
--> try-except blocks can be used to handl exceptions
'''

#comment out and try different inputs for a & b

a,b = 10,2 #valid input

#a,b = 10,0 #ZeroDivisionError

#a,b = 'a',5 #TypeError

#a,b = [1,2,3],5 #TypeError

#a,b = 0,['a'] #TypeError

try:
    print(a/b)
    print(n) #this is a ValueError, n not defined, which goes to general exception
except ZeroDivisionError:
    print('b cannot be zero')
except TypeError:
    print('inputs should be numerical')
except: #general exception
    print('something went wrong')
finally:
    print('this if from finally') #always executes wheather a program runs successfully or stops due to exception
#allocation and stopping of certain system resources can be done through this finally block

'''
raise exception is an user defined exception
'''

a = int(input()) #take an interger

if a%2 != 0:
    raise Exception('NotEvenNumber')
#if an odd number is given as input the custom exception will be raised
# %%
'''
File handling

f = open(filename,mode)

example: s = open('crazy.txt','r')

modes:
Create 'x' - creates the file, returns error if file exists
Read 'r' - opens for reading, error if file does not exist
Append 'a' - opens a file for appending, Creates if it does not exist
Write 'w' - opens for writing, creates if it does not exist
Text 't' - default value, Text mode
Binary 'b' - Binary mode (eg images)

examples:


>>> f = open('C:\myfile.txt','a') #appending
>>> f.write(" World!")
7
>>> f.close()

# reading file
>>> f = open('C:\myfile.txt','r') 
>>> f.read()
'Hello World!'
>>> f.close()


writing of multiple lines
>>> lines=["Good bye, World!.\n", "Welcome to the Apocalipse.\n"]
>>> f=open("D:\myfile.txt", "w")
>>> f.writelines(lines)
>>> f.close()

'''

'''
Reading a file:

f.read(): #or whatever vairalbe you assigned the file to
reads the specified no.of bytes from the file, defalut value -1 which means entire file

f.readline():
reads file one line at a time, each exectuion goes to the next line, end will be a blank string ''

f.readlines: 
reads entire file as list of strings representing individual lines

Writing to a file:

f.write():
file must be opened in 'w' or 'a' mode in order to write

f.close():
important to close the file after necessary operations, can be included in the finally block as a good programming practice
'''
# %%
'''
OOB - Object Oriented Programming

Python is an OOB, i.e. each and every entity in Python is an object with associated attributes

Creating a class:
class myClass: #basic structure with no attributes
    def __init__(self):
        pass

Creating an object:

obj = myClass() #object of class defined above with no attributes
'''

#example class from lecture with attribures, methods etc
class Student(): #initiation of class Student
    count = 0 #class variable
    def __init__(self, roll_no, name, total): #attibutes
        self.roll_no = roll_no #object variable
        self.name = name
        self.total = total
    
    def display(self): #methods of the class
        print(self.roll_no, self.name, self.total) #simple print

    def result(self): #conditional method giving result
        if self.total >120:
            print('Pass')
        else:
            print('Fail')

s0 = Student(0,'Bhuvanesh', 100) #an object of class student
Student.count += 1 #accessing of class vriable
s0.display() #class method on object
s0.result() #conditional class method on object

s1 = Student(1, 'Lolz', 150)
Student.count +=1
s1.display()
s1.result()


print(Student.count)

'''
Ineritence:
to inherit attributes or methods from a parent class

Types:
Simple inheritance - one parent one child
Hierarchical inheritance - one parent multiple children
Multiple inheritance - multiple parents one child
Multilevel inheritance Parent -> Intermediate (acts as child for parent and parent for child) -> Child 
(or Grandparent -> Parent -> Child)
Hybrid inheritance any combos of above four

Note: adding two underscores before a variable/attribute makes it private and can only be accessed within that class/method

Method Overloading (python doesn't support overloading):
->More than one method of a class sharing same method name with different attributes
->Used to add more to the behavior of mehtods
->Python doesn't support overloading and uses the last defined method by default
->example of Compile time polymorphism

Method Overriding:
-> example of Run time polymorphism
-> specific implementation of a method that is already defined in the parent class
-> used to change behavoir of existing methods
-> inheritance is a must for overriding since it is done between Parent (super class) and child (child class) methods

'''
#exmple of Hierarchical inheritance shown below

class Person: #Parent class or base calss, with or without paranthesis is ok
    def __init__(self, name, age):
        self.name = name
        self.age = age
        #self.__age = age #, adding underscores makes it a private variable and children cannot access
    
    def display(self):
        print(self.name, self.age, end = ' ')

class Student(Person): #child or derived or sub class
    def __init__(self, name, age, marks):
        super().__init__(name, age) #inheritance
        self.marks = marks
    
    def display(self):
        super().display() #inheritence from parent
        print(self.marks)

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name,age)  #inheritance from parent class
        self.salary = salary
    
    def display(self):
        #super().display() 
        print(self.name, self.age, self.salary) #method over riding

s = Student('lol',20,120) #student object

e = Employee('haha', 28, 70000) #employee object

s.display() #no overriding and uses super calss mehtod and adds on it

e.display() #Overriding, refer to method definition
# %%
'''

END OF THE SUMMARY VIDEO

ALL THE BEST AND HAPPY CODING !!!


'''

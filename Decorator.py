#A decorator takes in a function, adds some functionality and returns it.

# A simple Example :

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 13:29:02 2021

@author: giri
"""
class Test:
  
  class_var = 100
  
  def __init__(self):
    self.object_var = 10
    
  def show(self):
    #object variables can be accessed by self keyword
    print("Object Variable : ",self.object_var)

    print("Class Variable : ",self.class_var)
    
  def inc(self):
    self.class_var = self.class_var+10
    print("class variable increment : ",self.class_var)
    #class variables can be accessed by self/instance keyword or class name 
    #when ever we calls a function to print a class variable with help of object/instance , so that time mro(method resoultion order) comes into picture
    #first searches varible in instance itself 
    #second on calss variables it will search
    #third it will checks in builtin functions.
    
t = Test()
print("Class variable beofre inc() method calls : ",Test.class_var)
t.inc()
print("Class variable After inc() method calls : ",Test.class_var)

###################################################################################################

#To overcome from above problem , that when ever we do increment the instance variable of (class_var) , why its not showing its updated value.
#we can achieve this by 2 resolutions :

#Method 1 
# in inc() method we can have the statement like below :
       # Test.class_var = Test.class_var + 10
 
#Method 2
#using decorator(@classmethod) for that inc() method
#@classmethod
#  def inc(self):
#    self.object_var = self.object_var+10
#    print("Object variable increment : ",self.object_var)
    
#    self.class_var = self.class_var+10
#    print("class variable increment : ",self.class_var)

###################################################################################################


class Test:
  
  class_var = 100
  
  def __init__(self):
    self.object_var = 10
    
  def show(self):
    #object variables can be accessed by self keyword
    print("Object Variable : ",self.object_var)

    print("Class Variable : ",self.class_var)
  
  @classmethod
  def inc(self):
    self.class_var = self.class_var+10
    print("class variable increment : ",self.class_var)

t = Test()
print("Class variable beofre inc() method calls : ",Test.class_var)
t.inc()
print("Class variable After inc() method calls : ",Test.class_var)

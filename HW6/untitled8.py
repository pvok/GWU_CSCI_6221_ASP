# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 14:26:47 2023

@author: sagar
"""

import math;

class InvalidInput(Exception):
    pass

class shape:
    def __init__(self, base,height=1):
        self.base=base
        self.height=height
    def area(self):
        pass

class qualilateral(shape):    
    def area(self):
        return self.base*self.height

class triangle(shape):   
    def area(self): 
        return 0.5*self.base*self.height

class circle(shape):  
    def area(self): 
        return math.pi*self.base*self.base

def check_menu(dtype):
    if dtype!='triangle' and dtype!='rectangle' and dtype!='square' and dtype!='circle' and dtype!='parallelogram' and dtype!='Exit':
        return 1
    else:
        return 0


dtype = input('Enter one of the below options\na. triangle\nb. rectangle\nc. square\nd. circle\ne. parallelogram\nf. Exit\n')
dtype.strip()    

while check_menu(dtype):
    dtype=input('Invalid Input type. Enter one of the below options\na. triangle\nb. rectangle\nc. square\nd. circle\ne. parallelogram\nf. Exit\n')
    dtype.strip()

control_flow=0
while dtype!='Exit':
    if dtype=='rectangle' or dtype=='square' or dtype=='parallelogram':
        if dtype=='rectangle':
            try:
                l=float(input('Enter lenght and width of rectangle seperated by newline\n'))
                w=float(input())
                if l<=0:
                    print('Invalid Input for Length')
                    raise InvalidInput
                if l<=0:
                    print('Invalid Input for Width')
                    raise InvalidInput    
                print('Area of Rectangle is')
                q=qualilateral(l, w)
                print(q.area())
                control_flow=1
            except InvalidInput:
                print("Inout Value not accepted, Value can not be Less than or equal to 0.\nValue has to be a real positive number")
            except ValueError:
                print("Input Value can not be a string.\nValue has to be a real positive number")
                
        elif dtype=='parallelogram':
            try:
                l=float(input('Enter Base and Height of rectangle seperated by newline\n'))
                w=float(input())
                if l<=0:
                    print('Invalid Input for Base')
                    raise InvalidInput
                if w<=0:
                    print('Invalid Input for Height')
                    raise InvalidInput    
                print('Area of Parallelogram is')
                q=qualilateral(l, w)
                print(q.area())
                control_flow=1
            except InvalidInput:
                print("Inout Value not accepted, Value can not be Less than or equal to 0.\nValue has to be a real positive number")
            except ValueError:
                print("Input Value can not be a string.\nValue has to be a real positive number")

        elif dtype=='square':
            try:
                l=float(input('Enter side of Square\n'))
                if l<=0:
                    print('Invalid Input for Side')
                    raise InvalidInput

                print('Area of Square is')
                q=qualilateral(l, l)
                print(q.area())
                control_flow=1
            except InvalidInput:
                print("Inout Value not accepted, Value can not be Less than or equal to 0.\nValue has to be a real positive number")
            except ValueError:
                print("Input Value can not be a string.\nValue has to be a real positive number")
    
    if dtype=='triangle':
        try:
            l=float(input('Enter Base and Height of triangle seperated by newline\n'))
            w=float(input())
            if l<=0:
                print('Invalid Input for Base')
                raise InvalidInput
            if w<=0:
                print('Invalid Input for Height')
                raise InvalidInput    

            print('Area of Triangle is')
            t=triangle(l, w)
            print(t.area())
            control_flow=1
        except InvalidInput:
            print("Inout Value not accepted, Value can not be Less than or equal to 0.\nValue has to be a real positive number")
        except ValueError:
            print("Input Value can not be a string.\nValue has to be a real positive number")

    elif dtype=='circle':
        try:
            l=float(input('Enter radius of Circle\n'))
            if l<=0:
                print('Invalid Input for Radius')
                raise InvalidInput

            print('Area of Circle is')
            c=circle(l)
            print(c.area())
            control_flow=1
        except InvalidInput:
            print("Inout Value not accepted, Value can not be Less than or equal to 0.\nValue has to be a real positive number")
        except ValueError:
            print("Input Value can not be a string.\nValue has to be a real positive number")

                
    if control_flow!=0:
        dtype=input('Enter one of the below options\na. triangle\nb. rectangle\nc. square\nd. circle\ne. parallelogram\nf. Exit\n')
        control_flow=0
        while check_menu(dtype):
            dtype=input('Invalid Input type. Enter one of the below options\na. triangle\nb. rectangle\nc. square\nd. circle\ne. parallelogram\nf. Exit\n')
            dtype.strip()                           
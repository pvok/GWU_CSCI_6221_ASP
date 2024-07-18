# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 16:25:06 2023

@author: sagar
"""

import random

def fib(n):
    x=[]
    for i in range(n+1):
        if i==0:
            x.append(0)
        elif i==1:
            x.append(1)
        else:
            if len(x)==n:
                return x
            x.append(x[i-1]+x[i-2])
    return x

def lgc_loop_guarded_command(a, b, c):

    expressions=[]
    # create a list of Boolean expressions based on the range of integers
    for i in range(a,b+1):
        expressions.append([c % i == 0,fib(i)])
        
    # evaluate each Boolean expression for the value of c
    true_expressions = []
    for exp in expressions:
        if exp[0]:
            true_expressions.append(exp)
    
    # randomly select one of the true expressions and print the corresponding Fibonacci sequence
    random_exp=random.choice(true_expressions)
    if random_exp[0]==1:
        print(random_exp[1])
        
lgc_loop_guarded_command(3,6,12)
         
        


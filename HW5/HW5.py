# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 00:27:58 2023

@author: sagar
"""

# define Python user-defined exceptions
class InvalidString(Exception):
    pass


dtype = input('Data Type of Queue\nInteger or String\n')
print(dtype)
dtype.strip()



while dtype!='Integer' and dtype!='String':
    dtype=input('Invalid Data Type for Queue\nKindly enter either Integer or String\n')
    dtype.strip()

optype=''
q=[]

while optype!='end':
    optype = input('What operation to execute\n a. push \n b. pop \n c. count \n d. end\n')
    
    try:
        
        if optype=='push':
            inpt=input()
            
            
            
            if dtype=='Integer':
                inpt=int(inpt)
            else:
            #checking if string input is valid or not    
                if inpt[0]=='\'' and inpt[-1]=='\'':
                    inpt=inpt.replace('\'','')
                elif inpt.isdigit():
                    raise InvalidString
                    
            q.append(inpt)
        
        if optype=='pop':
            print(q[0])
            q.pop(0)

        if optype=='count':
            print(len(q))
            
            
    except ValueError:
        print("\nwrong data type is entered")
    except IndexError:
        print("\nQueue is empty, list can not be popped \n")
    except InvalidString:
        print("\nString Value not accepted. Enter number string enclosed in single quotes")
        print("\'9\'")
        
        
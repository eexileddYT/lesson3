#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 16:23:09 2021

@author: 蔡侑廷
"""


import random
a = random.randint(1,20) 

n = 5
t = 0

x = input('Please guess a random number from 1-20 and you have 5 tries  ')
x = int(x)


while n > 0:
    
    n = n - 1 
    t = t + 1

    if x > a and n != 0:
        print('Too large')
        x = int(input('Please try again '))   
      
        
    elif x < a and n != 0:
        print('Too little') 
        x = int(input('Please try again '))  

        
    
    elif x == a:
        print('Correct!')
        print('You played ',t,'times')
        n = 0
    
    

   
if n == 0 and a != x: 
        print('No more tries, you lose')
        
 
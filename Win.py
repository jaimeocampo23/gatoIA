#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 08:57:43 2020

@author: jaimecalderonocampo
"""

def VWIM(gato):
    WIN = 0
    W = (gato == 1)
    if (W[0, 0] == 1 and W[0, 1] == 1 and W[0, 2] == 1 or 
        W[0, 3] == 1 and W[0, 4] == 1 and W[0, 5] == 1 or
        W[0, 6] == 1 and W[0, 7] == 1 and W[0, 8] == 1 or
        W[0, 0] == 1 and W[0, 3] == 1 and W[0, 6] == 1 or
        W[0, 1] == 1 and W[0, 4] == 1 and W[0, 7] == 1 or
        W[0, 2] == 1 and W[0, 5] == 1 and W[0, 5] == 1 or
        W[0, 0] == 1 and W[0, 4] == 1 and W[0, 8] == 1 or
        W[0, 2] == 1 and W[0, 4] == 1 and W[0, 6] == 1):
            WIN = 1
    else:
        W = (gato == 2)
        if (W[0, 0] == 1 and W[0, 1] == 1 and W[0, 2] == 1 or 
        W[0, 3] == 1 and W[0, 4] == 1 and W[0, 5] == 1 or
        W[0, 6] == 1 and W[0, 7] == 1 and W[0, 8] == 1 or
        W[0, 0] == 1 and W[0, 3] == 1 and W[0, 6] == 1 or
        W[0, 1] == 1 and W[0, 4] == 1 and W[0, 7] == 1 or
        W[0, 2] == 1 and W[0, 5] == 1 and W[0, 5] == 1 or
        W[0, 0] == 1 and W[0, 4] == 1 and W[0, 8] == 1 or
        W[0, 2] == 1 and W[0, 4] == 1 and W[0, 6] == 1):
            WIN = 2
        
    return WIN
                
        
                
                
                
                
                
                
                
                
         
         
         
         
    
    
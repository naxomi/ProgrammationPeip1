#!/usr/bin/env python
#-*- coding: utf-8 -*- 

##########################################################################

''' ----- Exercice 2 ----- '''

def Affine(a,b,x):
    return a*x+b

print(Affine(Affine(1,1,1),1,1))
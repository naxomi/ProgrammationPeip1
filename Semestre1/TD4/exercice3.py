#!/usr/bin/env python
#-*- coding: utf-8 -*- 

##########################################################################

''' ----- Exercice 3 ----- '''

def Affine(a,b,x):
    return a*x+b

def FahrenheitToCelsius(temperature):
    return Affine(temperature-32, b=0, x=1/1.8)

def CelsiusToFahrenheit(temperature):
    return Affine(temperature, b=32, x=1.8)

temperature = int(input("Quelle température ? : "))
unite = int(input("Quelle unité ? (°Celsius -> 0 et °Fahrenheit -> 1) : "))

if unite == 0:
    print(f"{temperature}° Celsius vaut {CelsiusToFahrenheit(temperature)}° Fahrenheit.")
elif unite == 1:
    print(f"{temperature}° Fahrenheit vaut {FahrenheitToCelsius(temperature)}° Celsius.")
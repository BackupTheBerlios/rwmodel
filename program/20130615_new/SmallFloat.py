from __future__ import division
#-*- coding: utf-8 -*-
#! python
#name: SmallFloat
#author: Erik Lux
#date: 15.06.2013
#purpose: calculate with probabilities, values smaller than 0, working with very small numbers
#supports: addition and multiplication
#input: float number
#input is normalized right after input
#number is stored in form: mantisa in [-1,1], exponent in [-1, maxBigFloat) 
#meaning mantisa*10^(-exponent)
# if the result of operation ovverflows or invalid input, python raises Exception
from bigfloat import *
import math

class Small:
  def normalize(self,n):
    if n >1:
      raise Exception("invalid input -  number greater than 1")
    if n < -1:
      raise Exception("invalid input -  number smaller than -1")
    if n ==0:
      return (int(0), bigfloat(0))
      return 0
    else:
      return (-int(math.log10((n)))+1,n*(10**Small.e))
      

  def __init__(self,number):
    Small.x = number
    pair =  Small.normalize(self, Small.x)
    Small.e = pair[0]
    Small.m = pair[1]


  def add(self, x):
  def multiply(self, x):
    




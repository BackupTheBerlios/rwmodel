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
#number is stored in form: mantisa in (-10,10), exponent in [-1, maxBigFloat) 
#meaning mantisa*10^(-exponent)
# if the result of operation ovverflows or invalid input, python raises Exception
from bigfloat import *
import math
num_base = 10
class Small:
  #normalize probability
  def normalize(self,n):
    if n >1:
      raise Exception("invalid input -  number greater than 1")
    if n <-1:
      raise Exception("invalid input -  number smaller than -1")
    if n ==0:
      return (float(0), BigFloat(0))
    else:
      e = -int(math.log10(abs(n)))
      return (BigFloat(e),n*(10**(e)))
      
  #normalize number greater than 0
  def normalize_num(self, n):
    e = int(math.log10(abs(n)))
    if e > 0:
      return (BigFloat(e), n/(10**(e)))
    else:
      return (BigFloat(e), n*(10**(e)))

  def __init__(self,number):
    self.x = number
    pair =  Small.normalize(self, self.x)
    self.e = pair[0]
    self.m = pair[1]
  
  def init(self, mantisa, exponent):
    self.m = mantisa
    self.e = exponent

  #x is Small small object
  #neither is zero
  def add(self,number):
    number_gt = 0
    mm = int(0)
    ee = BigFloat(0)
    #print number.e, self.e
    if number.e < self.e:
      number_gt = 1
    if number.e == self.e and number.m > self.m:
      number_gt = 1
    #swap if the number is greater
    if number_gt == 1:
      mm = number.m
      ee = number.e
      number.m = self.m
      number.e = self.e
      self.m = mm
      self.e = ee
    #greater is in Small
    ediff = number.e - self.e
    #print 'num_gt:', number_gt
    #print 'ediff:', ediff
    
    mm = number.m
    ee = self.e
    if ediff != 0:
      mm /=(num_base**ediff)
    #print mm, ee
    #even expo
    self.m += mm
    if self.m >= num_base or self.m <=-num_base:
      self.m /=num_base
      self.e -=1
    
  
  def multiply(self, num):
    #multiply by number that is not probability// greater than 1
    #multiplication is allowed if and only if number the result will not overflow
    if not(isinstance(num, Small)) and num > 0:
      pair = self.normalize_num(num)
      e = pair[0]
      m = pair[1]
      multiplicant = Small(0)
      multiplicant.init(float(m), BigFloat(-e))
      if e < self.e:
        self.multiply(multiplicant)
        return
      else:
        raise Exception('invalid input - result overflows')
    if not(isinstance(num, Small)) and num <=0:
      raise Exception('invalid input - negative value')
                  
    self.m *= num.m
    self.e += num.e
    if self.m >= num_base or self.m <= -num_base:
      self.m /= num_base
      self.e -= 1

  def p(self):
    print 'mantisa: ', self.m
    print 'exponent: ', -self.e


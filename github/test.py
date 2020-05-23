class figure:
  from decimal import Decimal
  import math
  def __init__(self,a=None,b=None,area=None,c=None):
    self.a=a
    self.b=b
    self.area=area
    self.c=c
  def area(self):
    self.a=self.Decimal(self.a)
    self.b=self.Decimal(self.b)
    self.area=self.a*self.b
    print(self.area)
    return self.area

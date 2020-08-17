#!/usr/bin/env python
# coding: utf-8

# In[35]:


class Car():   #class
    def __init__(self,modelname,yearn,price):  #constructor
        self.modelname=modelname
        self.yearn=yearn
        self.price=price

    def price_inc(self):
        self.price=int(self.price*1.18)


#honda.modelname= 'City'    # modelname,yearn and price are variables associated with each object/instances
#honda.yearn=2017
#honda.price= 10000

#tata.modelname= 'Bolt'
#tata.yearn=2018
#tata.price= 30000

#print(honda.price)
#print(tata.price)

class SuperCar(Car):  #car is the parent of supercar
    pass
honda= SuperCar('city',2017,10000)            #honda is object belonging to car class
tata= Car('Bolt',2018,30000)

honda.cc=1500
print(honda.yearn)  #yearn defined in parent class, not child class
#print(help(honda))
honda.price_inc()
print(honda.price)
#print(honda.__dict__)
#print(honda.price)
#honda.price_inc()
#print(honda.price)


# In[ ]:





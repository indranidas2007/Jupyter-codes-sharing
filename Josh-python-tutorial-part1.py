#!/usr/bin/env python
# coding: utf-8

# In[2]:


name=input("What is your name?")
Fav= input("What is your favourite color?")
print(name)
print(Fav)
print(name + " likes " + Fav)


# In[4]:


year= input("Birth year")
age= 2020- int(year)  #string needs to be converted to int
print(age)


# In[8]:


first="John"
last="cena"
message= first + '[' + last + '] is a coder'
msg= f'{first} [{last}] is a coder'
print(message)
print(msg)


# In[10]:


print(10/3)
print(10%3)


# In[11]:


x=10 + 3*2
x


# In[13]:


y=2*3
z=2**3
x= 10+ 3*2**2
print(x)
print(y)
print(z)


# In[14]:


x=2.9
print(round(x))
print(abs(-2.9))


# In[17]:


import math
math.ceil(2.9)
math.floor(2.9)


# In[21]:


is_hot= False
is_cold= True
if is_hot:
    print("drink")
elif is_cold:
    print("Get blanket")
else:
    print("Sleep")
print("Enjoy your Day")


# In[23]:


has_high_income=True
has_good_credit=True
if has_high_income and has_good_credit:
    print("Eligible for Loan")
else:
    print("Not eligible")


# In[28]:


temparature=input("Today's Temp:")
temp=int(temparature)
if temp>30:
    print("HOt Day")
elif(temp==30):
    print("Moderate")
else:
    print("Not Hot Day")


# In[ ]:


weight=int(input("What's your weight:"))
unit=input("(L)bs or (K)g:")
if unit.upper()=='L':
    converted= weight*0.45
    print(f"You are {converted} kilos")
else:
    connverted= weighted/0.45
    print(f" You are {converted} kilos")
          


# In[ ]:


i=1
while i<=5:
    print('*'*i)
    i=i+1
print("Done")
    


# In[ ]:


secret_no=9
i=0
limit=3
while i<limit:
    guess=int(input('Guess:'))
    i +=1
    if guess == secret_no:
        print("You Won")
        break
else:
    print("You Failed.")


# In[ ]:


command=""
started= False
while True:
    command= input(">").lower()
    if command=="start":
        if started:
            print("Car is already started")
        else:
            started= True
            print("Car Started...")
    elif command=="stop":
        if not started:
            print("Car has already stopped!")
        else:
            started= False
            print("Car is stopped")
    elif command=="help":
        print("""start= to start the car
                stop= to stop the car
                quit- to quit""")
    elif command== "quit":
         break
    else:
        print("Sorry i dont understand")


# In[ ]:





# In[ ]:





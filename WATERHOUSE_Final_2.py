#!/usr/bin/env python
# coding: utf-8

# In[4]:


import math
from sympy.ntheory import factorint
while True:
    q=int(input("Give me the prime power number q of the finite field F: q= ")) 
    fact=factorint(q)        #We factor the number q=p_1^{n_1}*p_2^{n_2}*...
    p_1=list(fact.keys())    #We create a list with keys to be the the numbers p_1,p_2,...
    n_1=list(fact.values())  #We create a list with values to be the the numbers n_1,n_2,...
    p=int(p_1[0])            #We define p=p_{1}
    n=int(n_1[0])            #We define n=n_{1}
    dict_N={}                 #We define an empty dictionary for the number N.
    if q==p**n:              #Check if the number q=p_{1}[0]**n_{1}[0]=p**n.
        print("The number "+str(q)+" is a prime power")
        print("The prime number p="+str(p))
        print("The natural number n="+str(n))
        upper_bound=int(2*math.sqrt(q))
        print("The integer upper bound of the rational integers is |a|<="+str(upper_bound)+".")
        list_of_integers=[]
        for i in range(upper_bound+1): #Creating a list with all the integers : |a|<=2*q^{1/2}.
            list_of_integers.append(i)
            list_of_integers.append(-i)
        list_of_integers.remove(0)    
        print("The possible values of the integers a are :"+str(list_of_integers)+".")
        list_of_isogeny_classes=[]
        for a in list_of_integers:  #Checking CASE 1 gcd(a,p)=1
            if math.gcd(a,p)==1:   #Creating a list of isogeny classes for the corresponding integer a.
                list_of_isogeny_classes.append(a)
        for a in list_of_isogeny_classes:   #We print the number N=#E(F_{q}) of elements of the elliptic curve E in the isogeny class for every integer a. 
            dict_N[q+1-a]=a
            print("There exists an elliptic curve for a="+str(a)+" with N="+str(q+1-a)+" element(s).")
        total=len(list_of_isogeny_classes)
        s_1,s_2 = 0,0
        if n%2==1: #Checking CASE 2 when the natural number n is odd
            for a in list_of_integers:
                if a==0:
                    s_1=1
                    dict_N[q+1-a]=a
                    print("There exists a supersingular elliptic curve for a="+str(a)+" with N="+str(q+1-a)+" element(s).")
                if (a==math.sqrt(p*q) or a==math.sqrt(p*q)) and (p==3 or p==2):
                    s_2=2
                    dict_N[q+1-a]=a
                    print("There exists a supersingular elliptic curve for a="+str(a)+" with N="+str(q+1-a)+" element(s).")
                    print("There exists a supersingular elliptic curve for a="+str(-a)+" with N="+str(q+1+a)+" element(s).")
                s_3=s_1+s_2
            total_2=total+s_3
            print("In total there exist "+str(total_2)+" elliptic curves, with "+str(s_3)+" of them to be supersingular.")
        s_4, s_5, s_6 = 0,0,0
        if n%2==0: #Checking CASE 3 when the natural number n is even
            for a in list_of_integers:
                if a==0 and p%4!=1:
                    s_4=1
                    dict_N[q+1-a]=a
                    print("There exists a supersingular elliptic curve for a="+str(a)+" with N="+str(q+1-a)+" element(s).")
                if a==2*math.sqrt(q) or a==-2*math.sqrt(q):
                    s_5=2
                    dict_N[q+1-a]=a
                    print("There exists a supersingular elliptic curve for a="+str(a)+" with N="+str(q+1-a)+" element(s).")
                if (a==math.sqrt(q) or a==-math.sqrt(q)) and p%3!=1:
                    s_6=2
                    dict_N[q+1-a]=a
                    print("There exists a supersingular elliptic curve for a="+str(a)+" with N="+str(q+1-a)+" element(s).")
                s_10=s_4+s_5+s_6
            total_3=total+s_10
            """We summarize the isogeny classes"""
            print("In total there exist "+str(total_3)+" elliptic curves, with "+str(s_10)+" of them to be supersingular.")          
        
        break
N_1=int(input("Give me the number #E(Fq) you want to search for the finite field Fq: #E(Fq)=")) 
if N_1 in dict_N.keys():
    print("There exists an elliptic curve over F"+str(q)+" with "+str(N_1)+" elements for a="+str(dict_N[N_1])+".")
else:
    print("There does not exist an elliptic curve over F"+str(q)+" with "+str(N_1)+" elements")

    


# 

# In[ ]:





#!/usr/bin/env python
# -*- coding: utf-8 -*-
sum=0
i=0
count=0
while i<36:
	sum=630.42*(1+0.03/12)**i+sum
	count=count+1
	##print i,630.42*(1+0.03/12)**i
	i=i+1
print sum
print count
def p2p(principal,interest,monthly_paid,term):
    #p2p(20000,4,630.42,36)
    amt=0
    count=0
    interest=interest+0.0    ##to avide the round 
    while count<term:
        amt=monthly_paid*((1+interest/12/100)**count)+amt
        count=count+1
    return round(amt,2),str(round((amt-principal)/principal/(term/12)*100 ,2))+'%'
        
    

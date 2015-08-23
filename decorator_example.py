#!/usr/bin/python

def dekorator(f):
	def wrapper(*args,**kwargs):
		a=1+f(*args,**kwargs)
		return a
	return wrapper

@dekorator
def add(a,b):
	return a+b
print add(1,1)

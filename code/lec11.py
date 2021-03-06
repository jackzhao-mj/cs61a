import sys
import operator

def counting(s, value):
	total, index = 0, 0
	while(index < len(s)):
		if s[index] == value:
			total = total + 1
		index = index + 1
	return total

def counting2(s, value):
	total = 0
	for k in s:
		if k == value:
			total = total + 1
	"""print(k) Python会把return value直接打印出来
	如果想打印某个value 直接return就行
	而且可以一次return多个值
	k会bound到s的最后一个值"""
	return total, k

def coutning3(s, value1, value2):
	total = 0
	for e1, e2 in s:
		if e1 == value1 and e2 == value2:
			total = total + 1
	return total

# this is the test funcition of list comprehension
testList = [1,2,3,4]
def mul2(x):
  print (x * 2)
a = [mul2(i) for i in testList]

#print: a = [None, None, None, None]
# 但是会把testlist中每个元素用mul2 作用一遍

# list comprehension example 2:
odds = [1, 3, 5, 7]
evens = [print(x + 3) for x in odds]

def devisiors(n):
	return [x for x in range(1, n) if n % x == 0]

def width(area, length):
	assert area % length == 0
	# this is the useage of "assert" !!!!!!
	return area // length 
def perimeter(width, length):
	return 2 * (width + length)

def min_perimeter(area):
	lengths = devisiors(area)
	perimeters = [perimeter(width(area, l), l) for l in lengths]
	return min(perimeters)

def reduce(reduce_fn, s, initial):
	reduced = initial
	for x in s:
		reduced = reduce_fn(reduced, x)
	return reduced

# using higher order function to find perfect number:
def keep_if(filter_fn, s):
        return [x for x in s if filter_fn(x)]
# 这里是函数式编程，把filter_fn当成一个对象

def devisior_of(n):
	divides_n = lambda x: n % x == 0
	return keep_if(divides_n, range(1, n))

def sum_of_devisiors(n):
	return reduce(add, devisior_of(n), 0)

def perfect(n):
	return sum_of_devisiors(n) == n

# print (keep_if(perfect, range(1, 1000)))

'''This is My own Module

Date：2011-09-07
Author：Chris Mao

This is description information'''

class TestClass:
    '''This is TestClass' DocStrings'''
    def func1():
        '''this is func1's DocStrings'''
        pass

def func2():
    '''this is func2'''
    print ("this is func2")
    print (func2.__doc__)


#!/usr/bin/env python
#coding=utf-8
def split(index,value,database):
	left=[]
	right=[]
	for data in database:
		if data[index] < value:
			left.append(data)
		else:
			right.append(data)
	return left,right

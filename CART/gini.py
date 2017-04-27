#!/usr/bin/env python 
#coding:utf-8
def gini_index(groups,class_values=[0,1]):
	'''输入一组分类后得到的向量和类，计算分类的基尼系数：1为最差分类，0为最优分类'''
	gini=0
	for class_value in class_values:
		for group in groups:
			if len(group) == 0:
				continue
			mark=0
			for num in group:
				if num[-1] == class_value:
					mark=mark+1
			proportion=mark*1.0/len(group)
			gini=gini+proportion*(1-proportion)
	return gini


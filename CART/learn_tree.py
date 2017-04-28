#!/usr/bin/env python
#coding=utf-8
from learn import learn
from class_value import class_value
def learn_tree(node,max_depth,min_size,depth):
	'node是一个字典，通过初始赋值或者learn函数得到，其包含：groups（经learn函数分类后得到含有两个向量的向量组），left（左向量，若left可再分，则作为下一个node，若不可再分，则获得判断），right（同左向量）'
	#将左右向量分别取出进行判断
	print depth
	left,right = node['groups']
	print left,right
	print node['index'],node['value']
	del(node['groups'])							#数据本身并不重要，我们关注的是对数据划分的方法（分类点），当前node已经保存了上一个数据的分类点，我们现在关注的是是否继续划分
	#若左右向量有一个为空，则说明learn函数不能将数据进行划分，则停止递归
	if not left or not right:
		print 'empty voctor'
		node['left'] = node['right'] = class_value(left+right)
		return 										#说起来你可能不信：这个函数有很多return，但这确实是一个没有返回值的函数
	#若达到最大深度，则不再延伸枝叶（递归）		最大深度如何得到？玄学！
	if depth >= max_depth:
		print 'max depth'
		node['left'],node['right'] = class_value(left),class_value(right)
		return
	#若某个向量小于最小划分程度，则不再延伸枝叶（划分）	递归亦是对某一侧向量的进一步划分
	if len(left) <= min_size:
		print 'left min size'
		node['left'] = class_value(left)
	#若满足继续划分的条件，则将某侧向量通过learn函数变为下一个node	learn函数既是对向量组的划分，亦可将一个向量组变为一个node
	else :
		print 'left'
		node['left'] = learn(left)	#生成某侧向量的下一节点
		learn_tree(node['left'],max_depth,min_size,depth+1)
	if len(right) <= min_size:
		print 'right min size'
		node['right'] = class_value(right)
	else :
		print 'right'
		node['right'] = learn(right)
		learn_tree(node['right'],max_depth,min_size,depth+1)
		

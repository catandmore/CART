#!/usr/bin/env python
#acoding=utf-8
def predict(data,node):
	if data[node['index']] <= node['value'] :
		print data[node['index']],node['value']
		print 'left'
		if isinstance(node['left'],dict) :
			return predict(data,node['left'])
		else :
			return node['left']
	if data[node['index']] > node['value'] :
		print 'right'
		print data[node['index']],node['value']
		if isinstance(node['right'],dict) :
			return predict(data,node['right'])
		else :
			return node['right']

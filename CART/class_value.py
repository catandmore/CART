#!/usr/bin/env python
#coding=utf-8
def class_value(groups):
	value=[group[-1] for group in groups]
	return max(set(value),key=value.count)	#unkowen

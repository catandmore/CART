#!/usr/bin/env python
#coding=utf-8
from learn import learn
from learn_tree import learn_tree
def build_tree(dataset,max_depth,min_size,depth=1):
	root = learn(dataset)
	learn_tree(root,max_depth,min_size,depth)
	return root

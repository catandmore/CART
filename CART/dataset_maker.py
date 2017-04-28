#!/use/bin/env python
#coding=utf-8
from csv import reader
def dataset_maker(filename):
	f = open(filename)
	lines = reader(f)
	dataset = list(lines)
	for raw in dataset:
		for i in xrange(len(raw)):
			raw[i] = float(raw[i])
	return dataset

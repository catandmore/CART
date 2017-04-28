#!/usr/bin/env python
#conding=utf-8
from gini import gini_index
from split import split
def learn(database):
	index = 0
	value = 0
	gini = 1
	for i in xrange(len(database[0])-1):
		for group in database:
			L_R = split(i,group[i],database)
			m_gini = gini_index(L_R)
			if m_gini < gini:
				gini = m_gini
				index = i
				value = group[i]
				groups = L_R
	return {'index' :index,'value':value,'groups':groups}

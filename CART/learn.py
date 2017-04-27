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
			result = split(i,group[i],database)
			m_gini = gini_index(result)
			if m_gini < gini:
				gini = m_gini
				index = i
				value = group[i]
	print 'gini=%d index=%d value=%d'%(gini,index,value)

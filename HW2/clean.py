#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# This is for problem 2 in the homework #2
# __author__ = 'Cabbage'

import os

for root, dirs, files in os.walk('./life'):
	for name in files:
		Path = os.path.join(root, name)
		if Path.find('~') != -1:
			if os.path.isfile(Path[0:-1]) != True:
				os.remove(Path)

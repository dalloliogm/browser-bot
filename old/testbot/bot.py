#!/usr/bin/env python
# python script by Giovanni Dall'Olio
"""
a bot to test some website I need to test

"""
import logging
from config import url, username, password


def login(br):
	"""
	log to the forum.

	Input:
	- the browser object
	"""
	# select the login form, which is the only one available from the main page
	br.select_form(nr=0)

	br['loginUsername'] = username
	br['loginPassword'] = password

	resp = br.submit()








def _test():
	"""test the current module with doctest"""
	import doctest
	doctest.testmod()

if __name__ == '__main__':
	_test()


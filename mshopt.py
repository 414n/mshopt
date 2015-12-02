#!/usr/bin/env python

import sys
import re
from BeautifulSoup import BeautifulSoup

def print_usage ():
	print '''
	Usage: mshopt file.html

	Cleans up the given html file from MS-specific classes and inline styles.
	The output file is file.html.BS.html
	'''.strip()

def processHTML (soup):
#	search = soup.find('p', "class='MsoNormal'")
	print len(soup.findAll('p', class_='MsoNormal'))


def main (argv):
	for arg in argv:
		with open(arg, 'r') as infile:
			fr = infile.read()
			soup = BeautifulSoup(fr)
			outSoup = processHTML(soup)
			with open (arg +'BS.html', 'w') as outfile:
				outfile.write(soup.prettify())

if __name__ == "__main__":
	if len (sys.argv) <= 1:
		print_usage()
	else:
		main(sys.argv[1:])

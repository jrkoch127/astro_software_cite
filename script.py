import os.path
import re
#import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
#...................#

#VERSION 6 - 8/30/18 
#THIS WORKS - prints all AJ files where search matches, prints paper publication date, and line matches

rootDir = '/Users/jenniferkoch/Documents/astro_software_cite/AJ/'

searchstring = '(.*)(c|C)(i|I)(a|A)(o|O)|(.*)(c|C)handra\b|(.*)(s|S)(h|H)(e|E)(r|R)(p|P)(a|A)|(.*)(a|A)stro(\s*)(b|B)lend|(.*)(d|D)(s|S)9\b|(.*)(SAO)(\s*)Image|(.*)(h|H)oudini|(.*)(a|A)stro(\s*)(p|P)y|(.*)(s|S)pec2(d|D)|(.*)(p|P)lasma(\s*)(p|P)y'
patterns = re.compile(searchstring)

for dirName, subdirList, fileList in os.walk(rootDir):
	print('Found directory: %s' % dirName)

	for xmlfile in fileList:
		if xmlfile.endswith(".xml"):

			textfile = open(dirName+'/'+xmlfile, 'r')
			contents = textfile.read()

			f = contents.splitlines()
			for line in f:
				match = re.match(patterns, line)
				if match:
					soup = BeautifulSoup(contents, "lxml")
					print('\033[1m','\n---> Pattern found in',xmlfile,'\033[0m')
					#x = soup.article.findAll(string=patterns)
					#print(x)
					
					date = soup.article.find("pub-date")
					title = soup.article.find("title")
					print('--Paper pub-year:',date.year)
						#--needs revision; retrieves only first title 'ABSTRACT':
					print('--Section title: ',title) 
					print('--Match found:   ',line)
					
						#--Attempt to use BeautifulSoup to look for section title
					#section_title = soup.article.find(searchstring)
					#section_title.find_parents("p", class="title")
					
			textfile.close()
		else:
			print('No match found in', xmlfile)
	else:
		print('File not xml')
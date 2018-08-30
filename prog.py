import os.path
import re
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
#..................#
"""
#VERSION 1 - JUN 2018
#THIS WORKS - opens single xml file, prints tags and lines where search matches

	#1. Input file and RegEx search string

xmlfile=('/Users/jenniferkoch/Documents/astro_software_cite/AJ/0134/10.1086_521925.xml')
searchstring=("(.*)Astron")
print('\n')
print('File input =',xmlfile, '\n', 'Search input =',searchstring, '\n')

	#2. Open, read file

textfile = open(xmlfile, 'r')
filetext = textfile.read()

	#3. Print search matches

matches = re.findall(searchstring, filetext)
print('Matches =',matches,'\n')
#print(filetext)
f = filetext.splitlines()
#print(type(f))

	#4. Print lines where search matches
	
#print(f)
for line in f:
	if re.match(searchstring, line):
		print('\n',line)
	#print(filetext)

	#5. Close file
	
textfile.close()


#...................#

#VERSION 2 - JUL 2018
#THIS WORKS - prints all AJ files where search matches

rootDir = '/Users/jenniferkoch/Documents/astro_software_cite/AJ/'
searchstring = "(.*)Chicago"

for dirName, subdirList, fileList in os.walk(rootDir):
	print('Found directory: %s' % dirName)

	for xmlfile in fileList:
		if xmlfile.endswith(".xml"):
			print('\t%s' % xmlfile)
			textfile = open(dirName+'/'+xmlfile, 'r')
			filetext = textfile.read()
			matches = re.findall(searchstring, filetext)
			#print(matches)
			for line in textfile:
				if re.match(searchstring, line):
					print(line)
			#print(filetext)
			textfile.close()
		else:
			print('File is not xml')
			

#...................#

#VERSION 3 - 7/10/18 
#THIS WORKS - prints all AJ files where search matches, prints line matches

rootDir = '/Users/jenniferkoch/Documents/astro_software_cite/AJ/'

searchstring = '((.*)(c|C)(i|I)(a|A)(o|O))|((.*)(c|C)handra)|((.*)(s|S)(h|H)(e|E)(r|R)(p|P)(a|A))|(.*)(a|A)stro(b|B)lend|(.*)(a|A)stro (b|B)lend'
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
					#soup = BeautifulSoup(contents, "lxml")
					#x = soup.article.findAll(string=patterns)

					#these next two statement will print out the file the match was found in and then each relevant line	
					print('\n','     -- Pattern found in',xmlfile)
					print(line)
					
			textfile.close()
					
		else:
			print('No match found in', xmlfile)

	else:
		print('File not xml')

#...................#

#VERSION 4 - 7/25/18 

rootDir = '/Users/jenniferkoch/Documents/astro_software_cite/AJ/'

searchstring = '((.*)(c|C)(i|I)(a|A)(o|O))|((.*)(c|C)handra)|((.*)(s|S)(h|H)(e|E)(r|R)(p|P)(a|A))|(.*)(a|A)stro(b|B)lend|(.*)(a|A)stro (b|B)lend'
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
					x = soup.article.findAll(string=patterns)
					
					print('\n','     -- Pattern found in',xmlfile,)
					
					i = 0
					while i < len(x):
						print('#',(i+1),'of',len(x),':', line, '\n')
						i = i + 1
					
		else:
			print('No match found in', xmlfile)		
					
		textfile.close()

	else:
		print('File not xml')
"""
#...................#

#VERSION 5 - 7/25/18 
#THIS WORKS - prints all AJ files where search matches, prints paper publication date, and line matches

rootDir = '/Users/jenniferkoch/Documents/astro_software_cite/AJ/'

searchstring="(.*)(c|C)(i|I)(a|A)(o|O)|(.*)(c|C)handra\b|(.*)(s|S)(h|H)(e|E)(r|R)(p|P)(a|A)|(.*)(a|A)stro(\s*)(b|B)lend|(.*)(d|D)(s|S)9|(.*)(SAO)(\s*)Image|(.*)(h|H)oudini|(.*)(a|A)stro(\s*)(p|P)y|(.*)(s|S)pec2(d|D)|(.*)(p|P)lasma(\s*)(p|P)y"
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
					print('\n---> Pattern found in',xmlfile)
					#x = soup.article.findAll(string=patterns)
					#print(x)
					date = soup.article.find("pub-date")
					print('--Paper pub-year:',date.year)
					print('--Match found:   ',line)
			textfile.close()
		else:
			print('No match found in', xmlfile)
	else:
		print('File not xml')
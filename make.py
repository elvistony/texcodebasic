import os
from modules.latex_modules import *

final = r''
ch = 1

STATUS = {
	"Title":'',
	"Authors":'',
	"Titlesection":'',
	"Abstract":'',
	"Keywords":'',
	"Sections":'0'
}

while (ch!=0):
	os.system('clear')
	ch=int(input('''
		OPTIONS

		-TITLE-
1.Make Paper Title 				-'''+STATUS['Title']+'''
2.Make Authors					-'''+STATUS['Authors']+'''
3.--Terminate Titles 				-'''+STATUS['Titlesection']+'''

		-FIXED SECTIONS-
4.Make Abstract					-'''+STATUS['Abstract']+'''
5.Make Keyword Section 				-'''+STATUS['Keywords']+'''

		-FREE SECTIONS-
6.Make Section 					-['''+STATUS['Sections']+''' Sections]
7.Make SubSection
8.Make Content-Data

		-END DOC-
9.--End Document
		'''))

	if (ch==1):
		final = initialize()
		STATUS['Title']="DONE"
	elif (ch==2):
		final += makeauthor()
		STATUS['Authors'] = 'DONE'
	elif (ch==3):
		final += maketitle()
		STATUS['Titlesection'] = 'DONE'
	elif (ch==4):
		final += makeabstract()
		STATUS['Abstract'] = 'DONE'
	elif (ch==5):
		final += makekeywords()
		STATUS['Keywords'] = 'DONE'
	elif (ch==6):
		final += makeSection()
		STATUS['Sections'] = str(int(STATUS['Sections'])+1)
	elif (ch==7):
		final += makeSubSection()
	elif (ch==8):
		final += contentData()
	elif (ch==9):
		final += endDoc()
		producecode(final)
		break
	else:
		break
print(final)  

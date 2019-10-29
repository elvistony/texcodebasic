def makeauthor():
	no_of_members = int(input("Enter No. of Members: "))
	block = r''
	for x in range(no_of_members):
		block += "\n"+r'\and'
		name = input("Enter the "+str(x)+"th Member Name : ")
		dept = input("Enter the "+str(x)+"th Department : ")
		org = input("Enter the "+str(x)+"th Organization : ")
		block += r'\IEEEauthorblockN{'+str(x+1)+'.'+name+r'}\IEEEauthorblockA{\textit{'+'\n'+dept+r'} \textit{'+'\n'+org+r'}\\}'
	block +='}'
	return block

def initialize():
	title = input("Enter Title for Paper:")
	subtitle = input("Enter sub-title for Paper:")
	head = r'''
\documentclass[conference]{IEEEtran}
\IEEEoverridecommandlockouts
\usepackage{cite}
\usepackage{amsmath,amssymb,amsfonts}
\usepackage{algorithmic}
\usepackage{graphicx}
\usepackage{textcomp}
\usepackage{xcolor}
\def\BibTeX{{\rm B\kern-.05em{\sc i\kern-.025em b}\kern-.08em
    T\kern-.1667em\lower.7ex\hbox{E}\kern-.125emX}}
\begin{document}

\title{'''+title+r'''\\
{\footnotesize \textsuperscript{*}'''+subtitle+r'''}
}
\author{
	'''
	return head

def maketitle():
	return r'\maketitle'

def makeabstract():
	data = r'\begin{abstract}'
	print("Enter Paragraph and Terminate Input with Newline along with '.'\n")
	buffer = []
	while 1:
	    print("> ", end="")
	    line = input()
	    if line == ".":
	        break
	    buffer.append(line)
	multiline_string = "\n".join(buffer)
	data +=multiline_string
	data += r"\end{abstract}"
	return data

def makekeywords():
	block = r'\begin{IEEEkeywords}'
	block += input("Enter Keywords with ',' :\n")
	block+= r'\end{IEEEkeywords}'
	return block

def makeSection():
	block = r'\section{'
	block += input("Enter Section Title: ")
	block += r'}'
	return block

def makeSubSection():
	block = r'\subsection{'
	block += input("Enter SubSection Title: ")
	block += r'}'
	return block

def contentData():
	buffer = []
	print("Enter Paragraph and Terminate Input with Newline along with '.'\n")
	while 1:
	    print("> ", end="")
	    line = input()
	    if line == ".":
	        break
	    buffer.append(line)
	multiline_string = "\n".join(buffer)
	return multiline_string

def endDoc():
	return r'\end{document}'


def producecode(str):
	f = open("ieee.tex","w")
	f.write(str)
	f.close() 

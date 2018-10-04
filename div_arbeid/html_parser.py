__author__ = 'mariukri'
__email__ = 'mariukri@nmbu.no'

import numpy as np

def file_in(filename):
	infile = np.loadtxt(filename, 'r')
	for line in infile:
		rules(line)
	pass


def rules(textline):
	if textline[0] == '#':
		outline = "<h1>" +  textline + "</h1>"
	elif textline[0] == "##":
		outline = "<h2>" + textline + "</h2>"
	elif textline[0] == "###":
		outline = "<h3>" + textline + "</h3>"

	pass


def addhead(outfile):
	topoffile = "<!DOCTYPE html>"
	link_css = "<link rel='stylesheet.css' type='css/text' />"
	title = __author__
	head_a = "<head>"
	head_b = "</head>"
	out = [topoffile, head_a, link_css, title, head_b]
	for a in out:

	pass

def addbody(outfile):
	body_a = "<body>"
	body_b = "</body>"
	[body_a, body_b]

	pass
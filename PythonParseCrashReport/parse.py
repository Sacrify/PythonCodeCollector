#!/usr/bin/python
# -*- coding: UTF-8 -*- 

# -a archtecture
# -o ./dSYMs/xxx.dSYM/Contents/Resources/DWARF/xxx
# -f crash file
# -d dylib file path, usually under ~/Library/Developer/Xcode/iOS\ DeviceSupport/

import os, sys, getopt, fileinput, re, subprocess

architecture = ""
executable = ""
executableArr = []
executableName = ""
crashFile = ""
dylibPath = ""
dylibDict = {}


def searchDylib(dylibName):
	if dylibName == executableName:
		return executable

	for root, dirs, files in os.walk(dylibPath, topdown = False):
		try:
			files.index(dylibName) 
			if dylibName == "UIKit" and root.find("AccessibilityBundles") != -1:
				continue
			return os.path.join(root, dylibName)
		except:
			continue
	return ""


# main
opts, args = getopt.getopt(sys.argv[1:], "a:o:f:d:")

# Handle input
for op, value in opts:
	if op == "-a":
		architecture = value
	if op == "-o":
		executable = value
		executableArr = executable.split('/')
		executableName = executableArr[len(executableArr) - 1]
	if op == "-f":
		crashFile = value
	if op == "-d":
		dylibPath = value


# File Operation
crashFileHandler = open(crashFile)
pattern = re.compile(r'^\s*\d+\s+([^\s]*)\s+(0x[0-9a-f]*)\s+');

for line in crashFileHandler: 
	m = pattern.search(line)
	if m:
		dName = m.group(1)
		dAddr = m.group(2)
		dFullPath = "" 

		#print "FOUND name: " + dName + " addr:" + dAddr
		
		if dName in dylibDict:
			dFullPath = dylibDict[dName]

		if dFullPath == "":
			dFullPath = searchDylib(dName)
			if dFullPath != "":
				dylibDict[dName] = dFullPath

		if dFullPath == "":
			continue;

		dAddr = int(dAddr, 16)
		dAddr += 1

		command = "atos -arch " + repr(architecture) + " -o " + repr(dFullPath) + " -l " + "0x1" + " " + hex(dAddr)
		#print command
		p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		(stdoutput, erroutput) = p.communicate()
		print m.group(0) + stdoutput
	else:
		print line + "cann't parse"
crashFileHandler.close()







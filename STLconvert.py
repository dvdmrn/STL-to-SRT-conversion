"""
	Converts a .stl subtitle file into a .srt file
	HOW TO USE:
		Open a terminal window and type: `python STLconvert.py <YOUR_FILE_NAME>`
			>Example: python STLconvert.py myClosedCaptioningFile.srt
		Be sure to include the file extension!
"""


import sys
import io

print("Convert a .stl file to .srt")

filename = sys.argv[1]
inputList = []
outputList = []


def formatTC(timecode):
	timecode = timecode.replace(';',':')
	timecode = timecode+"0"
	Slist = list(timecode)
	Slist[8] = ","
	timecode = "".join(Slist)
	return timecode

def parsefile(filename):
	lineNumber = 0
	with open(filename) as inputfile:
	    for line in inputfile:
	        inputList.append(line.strip().split(','))

	for line in inputList:
		if ';' in line[0]:
			lineNumber += 1
			line[0].replace(";",":")
			TCin = line[0][:11]
			TCout = line[0][12:23]
			TCin = formatTC(TCin)
			TCout = formatTC(TCout)
			TCline = TCin+" --> "+TCout
			print TCline

			outputList.append([lineNumber])
			outputList.append([TCline])
		else:
			outputList.append(line)

	with open(filename[:-4]+'_converted.srt','w') as outputFile:
		for e in outputList:
			outputFile.write("%s\n" % e[0])

def main(filename):
	parsefile(filename)

main(filename)